# coding: utf-8
# /*##########################################################################
# Copyright (C) 2019-2020 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ############################################################################*/
"""Prototype of online 3D stack visualization"""

# TODOs
# - Add some constraint on the 3D ROI to represent the limit of the sample stage displacement
# - Benchmark access 3 slices in 2k**3 dataset: hdf5, zarr, caterva... disk, ssd, ram, memcached
# - Support live update of the 3D stack
# - When dragging line markers, they are not exactly synchronized
# - Issue of zoom level upon resize, it seems to need an extra sync
# - Handle the colormap correctly with the min/max of the stack, not of the image
# - Add a tool to set the colormap from a ROI (should go into silx)
# - When volume is loading, add a mode  showing the latest slice in the top view

# - 2nd widget for huge 2D data images + photo layer

# From feedbacks
# - Add ROI by drawning and selecting the right detector
# - Horizontal ROI should be circular
# - Check usage of float16
# - Change up/down of the volume (??)
# - When changing the height of the ROI, move the horizontal slice at the same time
# - Add some constraints horizontal/vertical on panning (with modifier keys)
# - Modifier key to change diameter of circle remaining centered
# - colormap: add per-slice autoscale
# - Option to have one slice as full screen

# From feedbacks, optional
# - 3D view with isosurface
# - Reload at full resolution (or make an extra view with it)


# Ideas/Question
# - Idea: Mode to draw a rectangle on a slide to select the right scan and create the proper ROI

# silx
# - Update silx ROIs and use it (that would bring the display of the name along with the ROI)
# - Fix silx issue with axes sync
# - Make silx plot action work for multiple plots at once
# - colormap: sqrt and gamma

from collections import namedtuple
import functools
import logging
import os
import sys
import threading
import time
import weakref

import numpy
import h5py

from silx.utils.weakref import WeakMethodProxy, WeakList

from silx.gui import qt, plot, icons
from silx.gui.colors import Colormap, rgba
from silx.gui.utils import blockSignals
from silx.gui.utils.concurrent import submitToQtMainThread
from silx.gui.widgets.FrameBrowser import HorizontalSliderWithBrowser

from silx.gui.plot.ColorBar import ColorBarWidget
from silx.gui.plot.utils.axis import SyncAxes
from silx.gui.plot import actions as plot_actions
from silx.gui.plot import items


if sys.version_info < (3, 6):
    # Require dict being ordered
    class NonSenseError(BaseException): pass
    raise NonSenseError("Python >= 3.6 is required!")


logger = logging.getLogger(__name__)

# Define scan parameters

class Scan:
    """Description of a tomo scan with a detector.

    It gives the constraints of the size of the reconstructed volume.

    :param List[float] bin_resolution: Size of a pixel in meters (vertical, horizontal)
    :param int slice_size: Size in pixels of the reconstructed slices
    :param height_range: Range in pixels of the height of the reconstructed volume (min, max)
    :param str name: name of the scan
    """

    def __init__(self, bin_resolution=(0., 0.), slice_size=0, height_range=(1, None), name=''):
        self.__bin_resolution = float(bin_resolution[0]), float(bin_resolution[1])
        self.__slice_size = int(slice_size)
        min_, max_= height_range
        self.__height_range = int(min_), None if max_ is None else int(max_)

        self.__name = str(name)

    def name(self):
        """Returns the name of the scan.

        :rtype: str
        """
        return self.__name

    def bin_resolution(self):
        """Returns bin resolution (in meters) (vertical, horizontal)

        :rtype: List[float]
        """
        return self.__bin_resolution

    def slice_size(self, unit='pixel'):
        """Returns the size of a horizontal slice.

        :param str unit: Unit of the returned value, either 'pixel' or 'meter'
        :rtype: Union[int,float]
        :raises ValueError: If unit is not supported
        """
        if unit == 'pixel':
            return self.__slice_size
        elif unit == 'meter':
            return self.__slice_size * self.bin_resolution()[1]
        else:
            raise ValueError("Unsupported unit")

    def height_range(self, unit='pixel'):
        """Returns the range of height of the reconstructed volume (min, max)

        :param str unit: Unit of the returned values, either 'pixel' or 'meter'
        :rtype: List[Union[int,float,None]]
        :raises ValueError: If unit is not supported
        """
        if unit == 'pixel':
            return self.__height_range
        elif unit == 'meter':
            res = self.bin_resolution()[0]
            min_, max_ = self.__height_range
            return min_ * res, None if max_ is None else max_ * res
        else:
            raise ValueError("Unsupported unit")


# ROI

class DraggableRectangle(qt.QObject):

    changed = qt.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__visible = True

        self._size = numpy.array((0, 0), dtype=numpy.float)  # (width, height)

        self._rectangle = items.Shape('polygon')
        self._rectangle.setName(self._legend('rectangle'))
        self._rectangle.setOverlay(True)
        self._rectangle.setLineWidth(2)

        self._center_marker = items.Marker()
        self._center_marker.setPosition(0, 0)
        self._center_marker.setName(self._legend('center_marker'))
        self._center_marker._setDraggable(True)
        self._center_marker.setSymbol('o')
        self._center_marker.sigItemChanged.connect(self.__marker_changed)

        self._plot_items = [self._rectangle, self._center_marker]

        self.setColor('pink')

    def __del__(self):
        for item in self._plot_items:
            plot = item.getPlot()
            if plot is not None:
                plot.removeItem(item)

    def _setVisible(self, visible):
        for item in self._plot_items:
            item.setVisible(visible)

    def _legend(self, suffix):
        return '_'.join((self.__class__.__name__, str(id(self)), suffix))
        
    def addToPlot(self, plot):
        for item in self._plot_items:
            assert item.getPlot() is None
        for item in self._plot_items:
            plot.addItem(item)

    def setLineWidth(self, width):
        for item in self._plot_items:
            if isinstance(item, items.LineMixIn):
                item.setLineWidth(width)

    def setLineStyle(self, linestyle):
        for item in self._plot_items:
            if isinstance(item, items.LineMixIn):
                item.setLineStyle(linestyle)

    def setColor(self, color):
        for item in self._plot_items:
            if isinstance(item, items.ColorMixIn):
                item.setColor(color)

    def __marker_changed(self, event):
        if event == items.ItemChangedType.POSITION:
            self._update()

    def _update(self):
        square = numpy.array(((-0.5, -0.5), (-0.5, 0.5), (0.5, 0.5), (0.5, -0.5)))
        self._rectangle.setPoints(self.getCenter() + self.getSize() * square)
        self.changed.emit()

    def setCenter(self, x, y):
        self._center_marker.setPosition(x, y)

    def getCenter(self):
        return numpy.array(self._center_marker.getPosition())
    
    def setSize(self, width, height):
        size = width, height
        if not numpy.array_equal(size, self._size):
            self._size = size
            self._update()

    def getSize(self):
        return self._size


class ExtendableRectangle(DraggableRectangle):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._bottom_marker = items.Marker()
        self._bottom_marker.setPosition(0, 0)
        self._bottom_marker.setName(self._legend('bottom_marker'))
        self._bottom_marker._setDraggable(True)
        self._bottom_marker.setSymbol('s')
        self._bottom_marker._setConstraint(
            WeakMethodProxy(self._bottom_constraint))
        self._bottom_marker.sigItemChanged.connect(self._marker_changed)
        self._plot_items.append(self._bottom_marker)

        self._top_marker = items.Marker()
        self._top_marker.setPosition(0, 0)
        self._top_marker.setName(self._legend('top_marker'))
        self._top_marker._setDraggable(True)
        self._top_marker.setSymbol('s')
        self._top_marker._setConstraint(
            WeakMethodProxy(self._top_constraint))
        self._top_marker.sigItemChanged.connect(self._marker_changed)
        self._plot_items.append(self._top_marker)

        self.__handle_marker_changed = True

        self.setColor('pink')

    def _top_constraint(self, x, y):
        cx, cy = self.getCenter()
        return cx, max(y, cy)

    def _top_marker_changed(self, event):
        if event == items.ItemChangedType.POSITION:
            width, _ = self.getSize()
            _, cy = self.getCenter()
            y = self._top_marker.getYPosition()
            newHeight = abs(cy - y) * 2.
            self.setSize(width, newHeight)

    def _bottom_constraint(self, x, y):
        cx, cy = self.getCenter()
        return cx, min(y, cy)

    def _marker_changed(self, event):
        if event == items.ItemChangedType.POSITION and self.__handle_marker_changed:
            width, _ = self.getSize()
            cx, _ = self.getCenter()
            ybottom = self._bottom_marker.getYPosition()
            ytop = self._top_marker.getYPosition()
            height = abs(ytop - ybottom)
            cy = 0.5 * (ybottom + ytop)
            self.setCenter(cx, cy)
            self.setSize(width, height)

    def _update(self):
        self.__handle_marker_changed = False
        cx, cy = self.getCenter()
        _, height = self.getSize()
        self._top_marker.setPosition(cx, cy + height / 2.)
        self._bottom_marker.setPosition(cx, cy - height / 2.)
        super()._update()
        self.__handle_marker_changed = True


class ROI3D(qt.QObject):

    SCAN_CHANGED = 'scanChanged'
    """Event emitted when the scan info has changed"""

    NAME_CHANGED = 'nameChanged'
    """Event emitted when the name has changed"""

    sigItemChanged = qt.Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__currentSlices = 0, 0, 0
        self.__name = ''
        self.__visible = True
        self.__scan = None

        self.__width = 0
        self.__height = 0
        self.__center = 0., 0., 0.

        self.__rois = {}
        self.__rois['top'] = DraggableRectangle()
        self.__rois['top'].changed.connect(self.__topChanged)

        self.__rois['front'] = ExtendableRectangle()
        self.__rois['front'].changed.connect(self.__frontChanged)

        self.__rois['side'] = ExtendableRectangle()
        self.__rois['side'].changed.connect(self.__sideChanged)

        self.__update()
        self.setScan(Scan())

    def getName(self):
        return self.__name

    def setName(self, name):
        name = str(name)
        if name != self.__name:
            self.__name = name
            self.sigItemChanged.emit(self.NAME_CHANGED)

    def isVisible(self):
        return self.__visible

    def setVisible(self, visible):
        visible = bool(visible)
        if visible != self.__visible:
            self.__visible = visible
            for rect in self.__rois.values():
                rect._setVisible(visible)
            self.sigItemChanged.emit(items.ItemChangedType.VISIBLE)

    def getScan(self):
        return self.__scan

    def setScan(self, scan):
        if scan != self.__scan:
            self.__scan = scan
            # Update ROI3D
            self.setWidth(scan.slice_size(unit='meter'))
            self.setHeight(
                numpy.clip(self.getHeight(), *scan.height_range(unit='meter')))
            self.sigItemChanged.emit(self.SCAN_CHANGED)

    def getROI(self, face):
        return self.__rois[face]

    def setLineWidth(self, width):
        for roi in self.__rois.values():
            roi.setLineWidth(width)

    def setCurrentSlicePosition(self, x, y, z):
        self.__currentSlices = x, y, z
        ox, oy, oz = self.getOriginCorner()
        fx, fy, fz = self.getFarthestCorner()
        in_color = 'pink'
        out_color = rgba(in_color)[:3] + (0.75,)
        in_style = '-'
        out_style = '--'

        self.__rois['side'].setColor(in_color if ox <= x <= fx else out_color)
        self.__rois['side'].setLineStyle(in_style if ox <= x <= fx else out_style)

        self.__rois['front'].setColor(in_color if oy <= y <= fy else out_color)
        self.__rois['front'].setLineStyle(in_style if oy <= y <= fy else out_style)

        self.__rois['top'].setColor(in_color if oz <= z <= fz else out_color)
        self.__rois['top'].setLineStyle(in_style if oz <= z <= fz else out_style)

    def getCurrentSlicePosition(self):
        return self.__currentSlices

    def __topChanged(self):
        cx, cy = self.__rois['top'].getCenter()
        cz = self.getCenter()[2]
        self.setCenter(cx, cy, cz)

    def __frontChanged(self):
        cx, cz = self.__rois['front'].getCenter()
        cy = self.getCenter()[1]

        self.setHeight(self.__rois['front'].getSize()[1])
        self.setCenter(cx, cy, cz)

    def __sideChanged(self):
        cy, cz = self.__rois['side'].getCenter()
        cx = self.getCenter()[0]
        self.setHeight(self.__rois['side'].getSize()[1])
        self.setCenter(cx, cy, cz)

    def __update(self):
        cx, cy, cz = self.getCenter()

        self.__rois['top'].setSize(self.getWidth(), self.getWidth())
        self.__rois['top'].setCenter(cx, cy)
        self.__rois['front'].setSize(self.getWidth(), self.getHeight())
        self.__rois['front'].setCenter(cx, cz)
        self.__rois['side'].setSize(self.getWidth(), self.getHeight())
        self.__rois['side'].setCenter(cy, cz)

        self.setCurrentSlicePosition(*self.getCurrentSlicePosition())  # sync color

        self.sigItemChanged.emit(items.ItemChangedType.POSITION)

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        if width != self.__width:
            self.__width = width
            self.__update()

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        if height != self.__height:
            self.__height = height
            self.__update()

    def getCenter(self):
        return self.__center

    def setCenter(self, cx, cy, cz):
        center = cx, cy, cz
        if not numpy.array_equal(center, self.__center):
            self.__center = center
            self.__update()

    def getOriginCorner(self):
        cx, cy, cz = self.getCenter()
        width, height = self.getWidth(), self.getHeight()
        return cx - width / 2., cy - width / 2., cz - height / 2.

    def getFarthestCorner(self):
        cx, cy, cz = self.getCenter()
        width, height = self.getWidth(), self.getHeight()
        return cx + width / 2., cy + width / 2., cz + height / 2.



# 3D ROI table widget

class ROI3DTableWidgetTypeItemDelegate(qt.QStyledItemDelegate):

    def __init__(self, parent=None, items={}):
        super().__init__(parent)
        self.__items = items

    def createEditor(self, parent, option, index):
        combobox = qt.QComboBox(parent)
        combobox.setAutoFillBackground(True)

        for text, item in self.__items.items():
            combobox.addItem(text, item)

        roi = index.data(qt.Qt.UserRole)
        itemIndex = combobox.findData(roi.getScan())
        if itemIndex == -1:  # Add an item
            text = index.data(qt.Qt.EditRole)
            combobox.addItem(text, data)
            itemIndex = combobox.count() - 1

        combobox.setCurrentIndex(itemIndex)
        combobox.currentIndexChanged.connect(self._commit)

        return combobox

    def _commit(self, *args):
        """Commit data to the model from editors"""
        sender = self.sender()
        self.commitData.emit(sender)


class ROI3DTableWidget(qt.QTableWidget):
    """Table widget of 3D ROIs"""

    NAME_COL, TYPE_COL, Z_COL, CENTER_COL, WIDGETS_COL = range(5)

    sigCenter = qt.Signal(float, float, float)

    def __init__(self, parent=None, types={}):
        super().__init__(parent)

        self._types = types

        headers = ['Name', 'Type', 'Vertical Range', 'Rotation Center', '']
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)

        horizontalHeader = self.horizontalHeader()
        horizontalHeader.setDefaultAlignment(qt.Qt.AlignLeft)
        horizontalHeader.setSectionResizeMode(self.NAME_COL, qt.QHeaderView.Interactive)
        horizontalHeader.setSectionResizeMode(self.TYPE_COL, qt.QHeaderView.ResizeToContents)
        horizontalHeader.setSectionResizeMode(self.Z_COL, qt.QHeaderView.Stretch)
        horizontalHeader.setSectionResizeMode(self.CENTER_COL, qt.QHeaderView.Stretch)
        horizontalHeader.setSectionResizeMode(self.WIDGETS_COL, qt.QHeaderView.ResizeToContents)

        verticalHeader = self.verticalHeader()
        verticalHeader.setVisible(False)

        self.setSelectionBehavior(qt.QAbstractItemView.SelectRows)
        self.setSelectionMode(qt.QAbstractItemView.SingleSelection)
        self.setFocusPolicy(qt.Qt.NoFocus)

        self.__delegate = ROI3DTableWidgetTypeItemDelegate(items=self._types)
        self.setItemDelegateForColumn(self.TYPE_COL, self.__delegate)

        self.itemChanged.connect(self.__itemChanged)
        self.currentCellChanged.connect(self.__currentCellChanged)

    def __currentCellChanged(self, currentRow, currentColumn, previousRow, previousColumn):
        if previousRow != -1:
            roi = self.getROI3D()[previousRow]
            roi.setLineWidth(2)

        if currentRow != -1:
            roi = self.getROI3D()[currentRow]
            roi.setLineWidth(4)

    def __itemChanged(self, item):
        """Handle item updates"""
        column = item.column()
        roi = item.data(qt.Qt.UserRole)
        if roi is None:
            return  # Only item with user role are handled

        if column == self.NAME_COL:
            roi.setVisible(item.checkState() == qt.Qt.Checked)
            roi.setName(item.text())
        elif column == self.TYPE_COL:
            scanName = item.data(qt.Qt.EditRole)
            scan = self._types.get(scanName)
            if scan is not None:
                roi.setScan(scan)
        else:
            logger.error('Unhandled column %d', column)

    def _updateDescription(self, roi):
        cx, cy, cz = roi.getCenter()
        height = roi.getHeight()
        z_min = cz - height / 2.
        z_max = z_min + height

        row = self.getROI3D().index(roi)
        item = self.item(row, self.Z_COL)
        item.setText('[%g, %g]' % (z_min, z_max))
        item = self.item(row, self.CENTER_COL)
        item.setText('(%g, %g)' % (cx, cy))

    def setCurrentSlicePosition(self, x, y, z):
        for roi in self.getROI3D():
            roi.setCurrentSlicePosition(x, y, z)

    def __roiChanged(self, event):
        """Handle 3D ROI updates"""
        roi = self.sender()

        if event == items.ItemChangedType.POSITION:
            self._updateDescription(roi)

        elif event == ROI3D.NAME_CHANGED:
            row = self.getROI3D().index(roi)
            item = self.item(row, self.NAME_COL)
            item.setText(roi.getName())

        elif event == ROI3D.SCAN_CHANGED:
            row = self.getROI3D().index(roi)
            item = self.item(row, self.TYPE_COL)
            item.setText(roi.getScan().name())

        elif event == items.ItemChangedType.VISIBLE:
            row = self.getROI3D().index(roi)
            item = self.item(row, self.NAME_COL)
            item.setCheckState(
                qt.Qt.Checked if roi.isVisible() else qt.Qt.Unchecked)

    def getROI3D(self):
        """Returns the list of 3D ROIs in the table.

        :rtype: List[ROI3D]
        """
        items = (self.item(row, self.NAME_COL) for row in range(self.rowCount()))
        return [item.data(qt.Qt.UserRole) for item in items if item is not None]

    def removeROI3D(self, roi):
        """Remove the given 3D ROI from the table.

        :param ROI3D roi:
        """
        row = self.getROI3D().index(roi)
        self.removeRow(row)
        roi.sigItemChanged.disconnect(self.__roiChanged)

    def __centerROI3D(self, roi):
        """Center plots on roi center

        :param ROI3D roi:
        """
        cx, cy, cz = roi.getCenter()
        self.sigCenter.emit(cx, cy, cz)

    def addROI3D(self, roi):
        """Append a 3D ROI to the table.

        :param ROI3D roi:
        :raises ValueError: If the ROI is already in the table
        """
        if roi in self.getROI3D():
            raise ValueError("ROI already in the table")

        # Create row
        row = self.rowCount()
        self.insertRow(row)

        baseFlags = qt.Qt.ItemIsSelectable | qt.Qt.ItemIsEnabled

        # Populate row
        # Name and visible
        item = qt.QTableWidgetItem(roi.getName())
        item.setFlags(
            baseFlags | qt.Qt.ItemIsEditable | qt.Qt.ItemIsUserCheckable)
        item.setData(qt.Qt.UserRole, roi)
        item.setCheckState(
            qt.Qt.Checked if roi.isVisible() else qt.Qt.Unchecked)
        self.setItem(row, self.NAME_COL, item)

        # Type
        item = qt.QTableWidgetItem(roi.getScan().name())
        item.setFlags(baseFlags | qt.Qt.ItemIsEditable)
        item.setData(qt.Qt.UserRole, roi)
        self.setItem(row, self.TYPE_COL, item)
        self.openPersistentEditor(item)

        # Info
        item = qt.QTableWidgetItem()
        item.setFlags(baseFlags)
        self.setItem(row, self.Z_COL, item)

        item = qt.QTableWidgetItem()
        item.setFlags(baseFlags)
        self.setItem(row, self.CENTER_COL, item)

        self._updateDescription(roi)

        # Buttons: Pointing and delete
        centerBtn = qt.QToolButton()
        centerBtn.setIcon(icons.getQIcon('normal'))
        centerBtn.setToolTip("Center the plots on the center of the ROI")
        centerBtn.clicked.connect(functools.partial(self.__centerROI3D, roi))

        delBtn = qt.QToolButton()
        delBtn.setIcon(icons.getQIcon('remove'))
        delBtn.setToolTip("Remove this ROI")
        delBtn.clicked.connect(functools.partial(self.removeROI3D, roi))

        self.__addWidget(row, self.WIDGETS_COL, centerBtn, delBtn)

        # Here to update the size of the columns
        horizontalHeader = self.horizontalHeader()
        horizontalHeader.reset()

        # Using queued connection to avoid sender() returning the table model
        roi.sigItemChanged.connect(self.__roiChanged, qt.Qt.QueuedConnection)

    def __addWidget(self, row, column, *widgets):
        cellWidget = qt.QWidget(self)
        layout = qt.QHBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(0)
        cellWidget.setLayout(layout)
        layout.addStretch(1)
        for widget in widgets:
            layout.addWidget(widget)
        layout.addStretch(1)
        self.setCellWidget(row, column, cellWidget)


# Main window

class Plot(plot.PlotWidget):
    """Plot widget with focus feedback"""

    sigSliceChanged = qt.Signal(int)
    """Signal emitted when arrow keys are pressed.

    It provides a direction information: 1 or -1.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setPanWithArrowKeys(False)
        self.setFocusPolicy(qt.Qt.StrongFocus)
        self.setFocus(qt.Qt.OtherFocusReason)

        self.setDataBackgroundColor('white')
        self.setKeepDataAspectRatio(True)
        self.setInteractiveMode('pan')

    def focusInEvent(self, event):
        self.setBackgroundColor((237, 251, 255, 255))
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.setBackgroundColor('white')

    def keyPressEvent(self, event):
        key = event.key()
        if key in (qt.Qt.Key_Left, qt.Qt.Key_Down):
            self.sigSliceChanged.emit(-1)

        elif key in (qt.Qt.Key_Right, qt.Qt.Key_Up):
            self.sigSliceChanged.emit(1)

        elif key == qt.Qt.Key_PageDown:
            self.sigSliceChanged.emit(-10)

        elif key == qt.Qt.Key_PageUp:
            self.sigSliceChanged.emit(10)

        else:
            # Only call base class implementation when key is not handled.
            # See QWidget.keyPressEvent for details.
            super(Plot, self).keyPressEvent(event)


class SlicePlotManager(object):
    """Bundles a plot and slider to handle states"""

    Mode = namedtuple('Mode', ['title', 'axis', 'xaxis', 'yaxis', 'unit'])

    DEFAULT = Mode(title='Slice',
                   axis='Index',
                   xaxis='X',
                   yaxis='Y',
                   unit='mm')

    AXIAL = Mode(title='Axial',
                 axis='Z',
                 xaxis='X',
                 yaxis='Y',
                 unit='mm')

    FRONT = Mode(title='Front',
                 axis='Y',
                 xaxis='X',
                 yaxis='Z',
                 unit='mm')

    SIDE = Mode(title='Side',
                axis='X',
                xaxis='Y',
                yaxis='Z',
                unit='mm')

    def __init__(self, parent, backend, mode=DEFAULT):
        self.__range = 0, 0
        self.__index = 0
        self.__data = numpy.empty((0, 0))
        self.__origin = 0., 0.
        self.__scale = 1., 1.
        self.__normalization = 0., 1.
        self.__mode = mode

        self.__plotWidget = Plot(parent, backend)
        self.__slider = HorizontalSliderWithBrowser(parent)
        self.__slider.setRange(0, 0)

        self.__plotWidget.sigSliceChanged.connect(self.__plotSliceChanged)

        self.__plotWidget.getXAxis().setLabel(
            '%s (%s)' % (self.__mode.xaxis, self.__mode.unit))
        self.__plotWidget.getYAxis().setLabel(
            '%s (%s)' % (self.__mode.yaxis, self.__mode.unit))

        self.__updatePlotTitle()

    def __plotSliceChanged(self, step):
        """Handle update of slice index from the plot.

        :param int step:
        """
        self.__slider.setValue(self.__slider.value() + step)

    def getPlotWidget(self):
        """Returns the managed :class:`PlotWidget`.

        :rtype: PlotWidget
        """
        return self.__plotWidget

    def getHorizontalSliderWithBrowser(self):
        """Returns the managed :class:`HorizontalSliderWithBrowser`.

        :rtype: HorizontalSliderWithBrowser
        """
        return self.__slider

    def setIndexRange(self, min_, max_):
        """Set the range of the slice indices.

        :param int min_:
        :param int max_:
        """
        min_, max_ = int(min_), int(max_)
        assert min_ <= max_
        assert min_ <= self.getIndex() <= max_
        self.__range = min_, max_
        self.__slider.setRange(*self.__range)

    def getIndexRange(self):
        """Returns the range of the slice indices.

        :returns: (min, max)
        """
        return self.__range

    def setSlice(self, data, index, copy=True):
        """Set the slice to display.

        :param numpy.ndarray data: Data of the slice
        :param int index: Index of the slice (must be within slice range)
        :param bool copy: True to copy the data, False to use as is.
        """
        index = int(index)
        min_, max_ = self.getIndexRange()
        assert min_ <= index <= max_
        self.__index = index
        self.__data = numpy.array(data, copy=copy)
        self.__updatePlotTitle()

    def getIndex(self):
        """Returns the current slice index.

        :rtype: int
        """
        return self.__index

    def getData(self, copy=True):
        """Returns the data of the current slice.

        :param bool copy:
            True to get a copy of data, False to get internal data.
        """
        return numpy.array(self.__data, copy=copy)

    def setSliceOrigin(self, ox, oy):
        """Set origin to use for the slice.

        :param float ox:
        :param float oy:
        """
        self.__origin = float(ox), float(oy)

    def getSliceOrigin(self):
        """Returns the origin of the slice.

        :returns: (ox, oy)
        """
        return self.__origin

    def setSliceScale(self, sx, sy):
        """Set the scale factors of the slice.

        :param float sx:
        :param float sy:
        """
        self.__scale = float(sx), float(sy)

    def getSliceScale(self):
        """Returns the scale factor on each axis.

        :returns: (sx, sy)
        """
        return self.__scale

    def setNormalization(self, origin, scale):
        """Set the origin and scale along the axis perpendicular to the slices.

        :param float origin:
        :param float scale:
        """
        self.__normalization = float(origin), float(scale)

    def getNormalization(self):
        """Returns the origin and scale along the axis perpendicular to the slices.

        :returns: (origin, scale factor)
        """
        return self.__normalization

    def getMode(self):
        """Returns the mode in use.

        :rtype: Mode
        """
        return self.__mode

    def __updatePlotTitle(self):
        """Update the plot title"""
        plot = self.getPlotWidget()
        mode = self.getMode()
        index = self.getIndex()
        origin, scale = self.getNormalization()
        position = origin + index * scale

        plot.setGraphTitle(
            '%s %f%s (%d)' % (mode.title, position, mode.unit, index))


class VolumeView(qt.QMainWindow):
    """3D volume slice viewer
    
    :param QWidget parent:
    :param Union[str,None] backend: The plot backend to use
    """

    def __init__(self, parent=None, backend=None, scans=()):
        super().__init__(parent)

        self.__scans = tuple(scans)

        self.__roi_index = 0
        self.__resolution = 1., 1., 1.
        self.__origin = 0., 0., 0.
        self._data = None

        self.__handleMarker = True

        # Shared colormap
        self._colormap = Colormap()
        self._colormap.setVRange(0., 4.)  # TODO make autoscale according to whole stack, not image

        # Create ROI action
        self._createROIAction = qt.QAction()
        self._createROIAction.setIcon(icons.getQIcon('add-shape-point'))
        self._createROIAction.setText("Add Selections")
        self._createROIAction.setToolTip('Create a new selection by clicking on a slice')
        self._createROIAction.setCheckable(True)
        self._createROIAction.setChecked(False)

        # Plot widgets
        self._topPlot = Plot(parent=self, backend=backend)
        self._topPlot.setDefaultColormap(self._colormap)
        self._topPlot.setKeepDataAspectRatio(True)
        self._topPlot.setGraphTitle("Axial")
        self._topPlot.getXAxis().setLabel("X")
        self._topPlot.getYAxis().setLabel("Y")
        self._topPlot.setInteractiveMode('pan')
        self._topPlotMarkers = (
            self._topPlot._getMarker(self._topPlot.addXMarker(
                0, legend='side-marker', text='side')),
            self._topPlot._getMarker(self._topPlot.addYMarker(
                0, legend='front-marker', text='front'))
            )
        self._topPlot.sigPlotSignal.connect(self.__plotChanged)
        self._topPlot.sigSliceChanged.connect(self.__topPlotSliceChanged)
        
        self._frontPlot = Plot(parent=self, backend=backend)
        self._frontPlot.setDefaultColormap(self._colormap)
        self._frontPlot.setKeepDataAspectRatio(True)
        self._frontPlot.setGraphTitle("Front")
        self._frontPlot.getXAxis().setLabel("X")
        self._frontPlot.getYAxis().setLabel("Z")
        self._frontPlot.setInteractiveMode('pan')
        self._frontPlotMarkers = (
            self._frontPlot._getMarker(self._frontPlot.addXMarker(
                0, legend='side-marker', text='side')),
            self._frontPlot._getMarker(self._frontPlot.addYMarker(
                0, legend='top-marker', text='top'))
            )
        self._frontPlot.sigPlotSignal.connect(self.__plotChanged)
        self._frontPlot.sigSliceChanged.connect(self.__frontPlotSliceChanged)

        self._sidePlot = Plot(parent=self, backend=backend)
        self._sidePlot.setDefaultColormap(self._colormap)
        self._sidePlot.setKeepDataAspectRatio(True)
        self._sidePlot.setGraphTitle("Side")
        self._sidePlot.getXAxis().setLabel("Y")
        self._sidePlot.getYAxis().setLabel("Z")
        self._sidePlot.setInteractiveMode('pan')
        self._sidePlotMarkers = (
            self._sidePlot._getMarker(self._sidePlot.addXMarker(
                0, legend='front-marker', text='front')),
            self._sidePlot._getMarker(self._sidePlot.addYMarker(
                0, legend='top-marker', text='top'))
            )
        self._sidePlot.sigPlotSignal.connect(self.__plotChanged)
        self._sidePlot.sigSliceChanged.connect(self.__sidePlotSliceChanged)

        for markers in (self._topPlotMarkers, self._frontPlotMarkers, self._sidePlotMarkers):
            for marker in markers:
                dim = ('top', 'front', 'side').index(marker.getText())
                marker._setConstraint(functools.partial(self.__lineMarkerConstraint, dim))
                marker._setDraggable(True)
                marker.setColor('pink')
                marker.setLineStyle('--')
                marker.sigItemChanged.connect(self.__lineMarkerChanged)

        # Axes constraints
        self._constraints = [
            SyncAxes(axes, syncLimits=False, syncScale=True,
                     syncDirection=True, syncCenter=True, syncZoom=True)
            for axes in (
                [self._topPlot.getXAxis(), self._frontPlot.getXAxis()],
                [self._frontPlot.getYAxis(), self._sidePlot.getYAxis()],
                [self._topPlot.getYAxis(), self._sidePlot.getXAxis()])
            ]

        # colorbar
        self._colorbar = ColorBarWidget(parent=self)
        #self._colorbar.setColormap(self._colormap)
        self._colorbar.setPlot(self._topPlot)
        self._colorbar.setLegend("Data")

        # Make ColorBarWidget background white by changing its palette
        self._colorbar.setAutoFillBackground(True)
        palette = self._colorbar.palette()
        palette.setColor(qt.QPalette.Background, qt.Qt.white)
        palette.setColor(qt.QPalette.Window, qt.Qt.white)
        self._colorbar.setPalette(palette)

        # frame browsers
        self._topBrowser = HorizontalSliderWithBrowser(self)
        self._frontBrowser = HorizontalSliderWithBrowser(self)
        self._sideBrowser = HorizontalSliderWithBrowser(self)
        for browser in (self._topBrowser, self._frontBrowser, self._sideBrowser):
            browser.setRange(0, 0)
            browser.valueChanged.connect(self._browserChanged)

        # ROI group

        types = dict([(scan.name(), scan) for scan in self.getScans()])
        self._roitable = ROI3DTableWidget(types=types)
        self._roitable.sigCenter.connect(self.__centerPlots)

        createROIBtn = qt.QToolButton()
        createROIBtn.setToolButtonStyle(qt.Qt.ToolButtonTextBesideIcon)
        createROIBtn.setDefaultAction(self._createROIAction)

        self._scanComboBox = qt.QComboBox()
        self._scanComboBox.setToolTip(
            'Select the default scan to use for new selections')
        for scan in self.getScans():
            self._scanComboBox.addItem(scan.name(), scan)

        roiGroupBox = qt.QGroupBox('Scan selection')
        layout = qt.QVBoxLayout(roiGroupBox)
        layout.addWidget(self._roitable)
        hlayout = qt.QHBoxLayout()
        hlayout.addWidget(createROIBtn)
        hlayout.addWidget(qt.QLabel('Default:'))
        hlayout.addWidget(self._scanComboBox)
        hlayout.addStretch(1)
        layout.addLayout(hlayout)

        # Top-right quadrant
        options_layout = qt.QHBoxLayout()
        options_layout.addWidget(self._colorbar)
        options_layout.addWidget(roiGroupBox, stretch=1)

        # Widget layout
        centralWidget = qt.QWidget(self)
        self.setCentralWidget(centralWidget)
        layout = qt.QGridLayout(centralWidget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self._topPlot, 0, 0)
        layout.addLayout(options_layout, 0, 1, qt.Qt.AlignLeft)
        #layout.addWidget(self._colorbar, 0, 1, qt.Qt.AlignLeft)
        layout.addWidget(self._frontPlot, 1, 0)
        layout.addWidget(self._sidePlot, 1, 1)

        form = qt.QFormLayout()
        layout.addLayout(form, 3, 0, 1, 2)
        form.addRow("Axial (along Z)", self._topBrowser)
        form.addRow("Front (along Y)", self._frontBrowser)
        form.addRow("Side (along X)", self._sideBrowser)
        
        # Toolbars
        toolbar = qt.QToolBar(self)
        self.addToolBar(qt.Qt.TopToolBarArea, toolbar)

        action = plot_actions.mode.ZoomModeAction(
            parent=self, plot=self._topPlot)
        action.triggered.connect(self.__zoomMode)
        toolbar.addAction(action)

        action = plot_actions.mode.PanModeAction(
            parent=self, plot=self._topPlot)
        action.triggered.connect(self.__panMode)
        toolbar.addAction(action)

        toolbar.addAction(self._createROIAction)

        toolbar.addSeparator()

        action = plot_actions.control.ResetZoomAction(
            parent=self, plot=self._topPlot)
        action.triggered.connect(self.__resetZoom)
        toolbar.addAction(action)

        toolbar.addAction(plot_actions.control.ColormapAction(
            parent=self, plot=self._topPlot))

    def __topPlotSliceChanged(self, direction):
        self._topBrowser.setValue(self._topBrowser.value() + direction)

    def __frontPlotSliceChanged(self, direction):
        self._frontBrowser.setValue(self._frontBrowser.value() + direction)

    def __sidePlotSliceChanged(self, direction):
        self._sideBrowser.setValue(self._sideBrowser.value() + direction)

    def __panMode(self, checked):
        action = self.sender()
        self._frontPlot.setInteractiveMode('pan', source=action)
        self._sidePlot.setInteractiveMode('pan', source=action)

    def __zoomMode(self, checked):
        action = self.sender()
        self._frontPlot.setInteractiveMode('zoom', source=action)
        self._sidePlot.setInteractiveMode('zoom', source=action)

    def __resetZoom(self, checked):
        self._frontPlot.resetZoom()
        self._sidePlot.resetZoom()

    def __lineMarkerChanged(self, event):
        if self.__handleMarker and event is items.ItemChangedType.POSITION:
            marker = self.sender()
            face = marker.getLegend().split('-')[0]
            res_z, res_y, res_x = self.getResolution()
            oz, oy, ox = self.getOrigin()

            x, y = marker.getPosition()
            position = y if x is None else x
            if face == 'side':
                index = int((position - ox) / res_x)
                self._sideBrowser.setValue(index)
            elif face == 'front':
                index = int((position - oy) / res_y)
                self._frontBrowser.setValue(index)
            elif face == 'top':
                index = int((position - oz) / res_z)
                self._topBrowser.setValue(index)

    def __lineMarkerConstraint(self, dim, x, y):
        min_ = self.getOrigin()[dim]
        data = self.getData()
        max_ = 0 if data is None else data.shape[dim]
        max_ = min_ + self.getResolution()[dim] * max_
        return numpy.clip(x, min_, max_), numpy.clip(y, min_, max_)

    def __plotChanged(self, event):
        """Handle signal from the plots"""
        if not self._createROIAction.isChecked():
            return

        if event['event'] == 'mouseClicked' and event['button'] == 'left':
            plot = self.sender()
            x, y = event['x'], event['y']
            self.__addROI3DFromClick(plot, x,y)

    def __addROI3DFromClick(self, plot, clicked_x, clicked_y):
        scan = self._scanComboBox.currentData()

        roi = ROI3D()
        roi.setName('%03d' % self.__roi_index)
        self.__roi_index += 1
        roi.setScan(scan)
        roi.setHeight(roi.getWidth())  # Use a cube as default

        res_z, res_y, res_x = self.getResolution()
        oz, oy, ox = self.getOrigin()
        browser_x = ox + res_x * self._sideBrowser.value()
        browser_y = oy + res_y * self._frontBrowser.value()
        browser_z = oz + res_z * self._topBrowser.value()
        roi.setCurrentSlicePosition(browser_x, browser_y, browser_z)

        if plot is self._topPlot:
            cx, cy, cz = clicked_x, clicked_y, browser_z
        elif plot is self._frontPlot:
            cx, cy, cz = clicked_x, browser_y, clicked_y
        elif plot is self._sidePlot:
            cx, cy, cz = browser_x, clicked_x, clicked_y
        roi.setCenter(cx, cy, cz)

        roi.getROI('top').addToPlot(self._topPlot)
        roi.getROI('front').addToPlot(self._frontPlot)
        roi.getROI('side').addToPlot(self._sidePlot)
        self._roitable.addROI3D(roi)

    def _browserChanged(self, value):
        """Handle frame browsers change

        :param int value:
        """
        self.__handleMarker = False

        browser = self.sender()
        res_z, res_y, res_x = self.getResolution()
        oz, oy, ox = self.getOrigin()

        if browser is self._topBrowser:
            face = 'top'
            position = oz + res_z * value
        elif browser is self._frontBrowser:
            face = 'front'
            position = oy + res_y * value
        elif browser is self._sideBrowser:
            face = 'side'
            position = ox + res_x * value
        else:
            raise RuntimeError('Unhandled signal sender')

        for markers in (self._topPlotMarkers, self._frontPlotMarkers, self._sidePlotMarkers):
            for marker in markers:
                if marker.getLegend() == face + '-marker':
                    marker.setPosition(position, position)

        self.updateSlices(face)

        x = self._sideBrowser.value()
        y = self._frontBrowser.value()
        z = self._topBrowser.value()
        self._roitable.setCurrentSlicePosition(
            ox + res_x * x, oy + res_y * y, oz + res_z * z)

        self.__handleMarker = True

    def __update(self):
        self.setData(self.getData())  # TODO use a better way to trigger refresh

    def getUnit(self):
        """Returns the unit in use

        :rtype: str
        """
        return 'mm'

    def getScans(self):
        """Returns the list of available scans

        :rtype: List[Scan]
        """
        return self.__scans

    def setResolution(self, depth=1., row=1., column=1.):
        """Set the resolution as meter per pixel.

        :param float depth: Vertical resolution
        :param float row: Slice row resolution
        :param float column: Slice column resolutio
        """
        resolution = float(depth), float(row), float(column)
        if resolution != self.__resolution:
            self.__resolution = resolution
            self.__update()

    def getResolution(self):
        """Returns the resolution information (depth, row, column)

        :rtype: List[float]
        """
        return self.__resolution

    def setOrigin(self, z=0., y=0., x=0.):
        """Set the offset from origin in meter of the dataset

        :param float z:
        :param float y:
        :param float x:
        """
        origin = float(z), float(y), float(x)
        if origin != self.__origin:
            self.__origin = origin
            self.__update()

    def getOrigin(self):
        """Returns the origin (z, y, x) of the datset

        :rtype: List[float]
        """
        return self.__origin

    def __centerPlots(self, cx, cy, cz):
        """Change slice and pan plots to center to given position

        :param float cx:
        :param float cy:
        :param float cz:
        """
        res_z, res_y, res_x = self.getResolution()
        oz, oy, ox = self.getOrigin()

        x = int((cx - ox) / res_x)
        y = int((cy - oy) / res_y)
        z = int((cz - oz) / res_z)

        data = self.getData()
        if data is None:
            depth, height, width = 0, 0, 0
        else:
            depth, height, width = numpy.array(data.shape) - 1

        x = numpy.clip(x, 0, width)
        y = numpy.clip(y, 0, height)
        z = numpy.clip(z, 0, depth)

        self._sideBrowser.setValue(x)
        self._frontBrowser.setValue(y)
        self._topBrowser.setValue(z)

        # change plot limits to center without changing the zoom
        xmin, xmax = self._topPlot.getXAxis().getLimits()
        ymin, ymax = self._topPlot.getYAxis().getLimits()
        half_width = 0.5 * abs(xmax - xmin)
        half_height = 0.5 * abs(ymax - ymin)
        self._topPlot.getXAxis().setLimits(cx - half_width, cx + half_width)
        self._topPlot.getYAxis().setLimits(cy - half_height, cy + half_height)

        xmin, xmax = self._frontPlot.getXAxis().getLimits()
        ymin, ymax = self._frontPlot.getYAxis().getLimits()
        half_width = 0.5 * abs(xmax - xmin)
        half_height = 0.5 * abs(ymax - ymin)
        self._frontPlot.getXAxis().setLimits(cx - half_width, cx + half_width)
        self._frontPlot.getYAxis().setLimits(cz - half_height, cz + half_height)

        xmin, xmax = self._sidePlot.getXAxis().getLimits()
        ymin, ymax = self._sidePlot.getYAxis().getLimits()
        half_width = 0.5 * abs(xmax - xmin)
        half_height = 0.5 * abs(ymax - ymin)
        self._sidePlot.getXAxis().setLimits(cy - half_width, cy + half_width)
        self._sidePlot.getYAxis().setLimits(cz - half_height, cz + half_height)

    def setData(self, data):
        """The data to view, no copy is made.

        :param Union[None,numpy.ndarray,h5py.Dataset] data:
            3D volume, dimension convention is: (depth, row, column).
        """
        self._data = data

        if self._data is None:
            self._topPlot.remove('image')
            self._topPlot.setGraphTitle("Axial")
            self._frontPlot.remove('image')
            self._frontPlot.setGraphTitle("Front")
            self._sidePlot.remove('image')
            self._sidePlot.setGraphTitle("Side")
            
            self._topBrowser.setRange(0, 0)
            self._frontBrowser.setRange(0, 0)
            self._sideBrowser.setRange(0, 0) 

        else:
            depth, height, width = numpy.array(self._data.shape) - 1
            self._topBrowser.setRange(0, depth)
            self._topBrowser.setValue(depth // 2)
            self._frontBrowser.setRange(0, height)
            self._frontBrowser.setValue(height // 2)
            self._sideBrowser.setRange(0, width)
            self._sideBrowser.setValue(width // 2)

            self.updateSlices()

            self._topPlot.resetZoom()
            self._frontPlot.resetZoom()
            self._sidePlot.resetZoom()

    def getData(self):
        """Returns the data currently viewed, no copy is made.

        :rtype: Union[None,numpy.ndarray,h5py.Dataset]
        """
        return self._data

    def updateSlices(self, *faces):
        """Update plotted slices"""
        if not faces:
            faces = 'top', 'front', 'side'

        res_z, res_y, res_x = self.getResolution()
        oz, oy, ox = self.getOrigin()
        unit = self.getUnit()

        if 'top' in faces:
            z = self._topBrowser.value()
            zpos = oz + z * res_z
            image = self._data[z, :, :]
            self._topPlot.setGraphTitle("Axial %g%s (%d)" % (zpos, unit, z))
            self._topPlot.addImage(image, scale=(res_x, res_y), origin=(ox, oy),
                legend='image', resetzoom=False, copy=False)

        if 'front' in faces:
            y = self._frontBrowser.value()
            ypos = oy + y * res_y
            image = self._data[:, y, :]
            self._frontPlot.setGraphTitle("Front %g%s (%d)" % (ypos, unit, y))
            self._frontPlot.addImage(image, scale=(res_x, res_z), origin=(ox, oz),
                legend='image', resetzoom=False, copy=False)

        if 'side' in faces:
            x = self._sideBrowser.value()
            xpos = ox + x * res_x
            image = self._data[:, :, x]
            self._sidePlot.setGraphTitle("Side %g%s (%d)" % (xpos, unit, x))
            self._sidePlot.addImage(image, scale=(res_y, res_z), origin=(oy, oz),
                    legend='image', resetzoom=False, copy=False)
 

class H5LoadingThread(threading.Thread):

    def __init__(self, filename, dataset_name, progress=None):
        self._filename = filename
        self._dataset_name = dataset_name
        self._progress = progress

        self.loaded_index = 0
        with h5py.File(self._filename, 'r') as f:
            dset = f[self._dataset_name]
            self.data = numpy.full(dset.shape, numpy.nan, dtype=dset.dtype)

            super().__init__()

    def run(self):
        with h5py.File(self._filename, 'r') as f:
            dset = f[self._dataset_name]
            length = len(dset)
            for index in range(length):
                data = dset[index]
                self.data[index] = data
                self.loaded_index = index
                self._progress(self.loaded_index, length)
                # Give a chance for main thread to run as h5py do not release the GIL
                time.sleep(0.01)

if __name__ == "__main__":
    import sys
    from silx.io.url import DataUrl

    app = qt.QApplication([])

    scan_20um = Scan(
        name="2k_20um",
        bin_resolution=[20 * 10e-6] * 2,
        slice_size=2048)

    scan_2um = Scan(
        name="2k_2um",
        bin_resolution=[2 * 10e-6] * 2,
        slice_size=2048)

    scans = [scan_20um, scan_2um]
    window = VolumeView(backend='gl', scans=scans)
    window.show()

    print('Loading')
    url = DataUrl(sys.argv[1])

    if url.data_path() is None:
        data_view = numpy.load(url.file_path(), mmap_mode='r+')

    else:
        last_time = - float('inf')
        future_result = None

        def progress(index, total):
            global last_time, future_result
            t = time.time()
            if t - last_time >= 2.:  # Update at most every second
                print('update', index)
                if future_result is None or future_result.done():
                    last_time = t
                    future_result = submitToQtMainThread(window.updateSlices)

        loader = H5LoadingThread(
            filename=url.file_path(),
            dataset_name=url.data_path(),
            progress=progress)
        data_view = loader.data
        loader.start()

    print('Loaded', data_view.shape)

    window.setOrigin(1, 2, 3)
    window.setResolution(50*10e-5, 50*10e-5, 50*10e-5)
    #window.setResolution(50*10e-6, 50*10e-6, 50*10e-6)
    window.setData(data_view)

    sys.exit(app.exec_())

