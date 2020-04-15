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
# - Improve scan description: take into account radius being able to change
# - Benchmark access 3 slices in 2k**3 dataset: hdf5, zarr, caterva... disk, ssd, ram, memcached
# - Support live update of the 3D stack
# - When dragging line markers, they are not exactly synchronized
# - Issue of zoom level upon resize, it seems to need an extra sync
# - Handle the colormap correctly with the min/max of the stack, not of the image
# - Add a tool to set the colormap from a ROI (should go into silx)
# - When volume is loading, add a mode  showing the latest slice in the top view

# - 2nd widget for huge 2D data images + photo layer

# From feedbacks
# - Add select the right detector when drawing a ROI
# - Check usage of float16
# - Change up/down of the volume (??)
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
import typing
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

class BaseDraggableROI(qt.QObject):
    """A moveable ROI that can be dragged by its center.

    :param QObject parent:
    """

    changed = qt.Signal()
    """Signal emitted each time the item is changed"""

    dragged = qt.Signal(float, float)
    """Signal emitted when the item is changed by a direct user interaction.

    It provides the x and y data coordinates of the currently dragged position.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__visible = True

        self._centerMarker = items.Marker()
        self._centerMarker.setPosition(0, 0)
        self._centerMarker.setName(self._legend('center_marker'))
        self._centerMarker._setDraggable(True)
        self._centerMarker.setSymbol('o')
        self._centerMarker.sigItemChanged.connect(self.__markerChanged)
        self._items = [self._centerMarker]

        self.setColor('pink')

    def __del__(self):
        for item in self._items:
            plot = item.getPlot()
            if plot is not None:
                plot.removeItem(item)

    def _setVisible(self, visible: bool) -> None:
        """Set the visibility of contained items"""
        for item in self._items:
            item.setVisible(visible)

    def _legend(self, suffix: str) -> str:
        """Generates legends to use internally"""
        return '_'.join((self.__class__.__name__, str(id(self)), suffix))

    def addToPlot(self, plot):
        for item in self._items:
            assert item.getPlot() is None
        for item in self._items:
            plot.addItem(item)

    def setLineWidth(self, width: float) -> None:
        """Set the width of the line"""
        for item in self._items:
            if isinstance(item, items.LineMixIn):
                item.setLineWidth(width)

    def setLineStyle(self, linestyle: str) -> None:
        """Set the style of the line of the ROI"""
        for item in self._items:
            if isinstance(item, items.LineMixIn):
                item.setLineStyle(linestyle)

    def setColor(self, color) -> None:
        """Set the color of the marker

        :param color: The color description
        """
        for item in self._items:
            if isinstance(item, items.ColorMixIn):
                item.setColor(color)

    def __markerChanged(self, event) -> None:
        """Handle marker changed events"""
        if event == items.ItemChangedType.POSITION:
            self._update()
            marker = self.sender()
            if marker.isBeingDragged():
                self.dragged.emit(*marker.getPosition())

    def _update(self) -> None:
        """Update the displayed shape and send event"""
        self.changed.emit()

    def setCenter(self, x: float, y: float) -> None:
        """Set the center of the ROI"""
        self._centerMarker.setPosition(x, y)

    def getCenter(self) -> typing.Tuple[float]:
        """Returns the center (cx, cy) of the ROI"""
        return self._centerMarker.getPosition()


class CircularROI(BaseDraggableROI):
    """A moveable and resizable circular ROI.

    :param QWidget parent:
    """

    _CIRCLE_NB_POINTS = 100
    """Number of points in the circle"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__radius = 0.
        self.__handleMarkerChanged = True

        self._circle = items.Shape('polygon')
        self._circle.setName(self._legend('rectangle'))
        self._circle.setOverlay(True)
        self._circle.setLineWidth(2)
        self._items.append(self._circle)

        self._leftMarker = items.Marker()
        self._leftMarker.setPosition(0, 0)
        self._leftMarker.setName(self._legend('left_marker'))
        self._leftMarker._setDraggable(True)
        self._leftMarker.setSymbol('s')
        self._leftMarker._setConstraint(
            WeakMethodProxy(self.__leftConstraint))
        self._leftMarker.sigItemChanged.connect(self.__markerChanged)
        self._items.append(self._leftMarker)

        self.setColor('pink')

    def __leftConstraint(self, x: float, y: float) -> None:
        """Constraint applied on the left anchor"""
        cx, cy = self.getCenter()
        return max(x, cx), cy

    def __markerChanged(self, event) -> None:
        """Handle changes in markers"""
        if event == items.ItemChangedType.POSITION and self.__handleMarkerChanged:
            self.setRadius(
                abs(self._leftMarker.getXPosition() - self.getCenter()[0]))
            marker = self.sender()
            self.dragged.emit(*marker.getPosition())

    def _update(self) -> None:
        """Update the displayed shape and send event"""
        self.__handleMarkerChanged = False
        self._leftMarker.setPosition(
            self.getCenter()[0] + self.getRadius(),
            self._leftMarker.getYPosition())
        coords = numpy.linspace(0, 2*numpy.pi, self._CIRCLE_NB_POINTS)
        points = numpy.transpose((numpy.cos(coords), numpy.sin(coords)))
        self._circle.setPoints(self.getCenter() + self.getRadius() * points)
        super()._update()
        self.__handleMarkerChanged = True

    def setRadius(self, radius: float) -> None:
        """Set the radius of the ROI"""
        if radius != self.__radius:
            self.__radius = radius
            self._update()

    def getRadius(self) -> float:
        """Returns the radius of the ROI"""
        return self.__radius


class DraggableRectangle(BaseDraggableROI):
    """A rectangular ROI that can be dragged with an anchor at its center.

    :param QWidget parent:
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__size = 0, 0  # (width, height)

        self._rectangle = items.Shape('polygon')
        self._rectangle.setName(self._legend('rectangle'))
        self._rectangle.setOverlay(True)
        self._rectangle.setLineWidth(2)
        self._items.append(self._rectangle)

        self.setColor('pink')

    def _update(self) -> None:
        """Update the displayed shape and send event"""
        square = numpy.array(((-0.5, -0.5), (-0.5, 0.5), (0.5, 0.5), (0.5, -0.5)))
        self._rectangle.setPoints(self.getCenter() + self.getSize() * square)
        super()._update()

    def setSize(self, width: float, height: float) -> None:
        """Set the size of the ROI."""
        size = width, height
        if size != self.__size:
            self.__size = size
            self._update()

    def getSize(self) -> typing.Tuple[float]:
        """Returns the size (width, height) of the ROI."""
        return self.__size


class ExtendableRectangle(DraggableRectangle):
    """ROI that can be moved and extended vertically by anchors.

    :param QWidget parent:
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self._bottomMarker = items.Marker()
        self._bottomMarker.setPosition(0, 0)
        self._bottomMarker.setName(self._legend('bottom_marker'))
        self._bottomMarker._setDraggable(True)
        self._bottomMarker.setSymbol('s')
        self._bottomMarker._setConstraint(
            WeakMethodProxy(self.__bottomConstraint))
        self._bottomMarker.sigItemChanged.connect(self.__markerChanged)
        self._items.append(self._bottomMarker)

        self._topMarker = items.Marker()
        self._topMarker.setPosition(0, 0)
        self._topMarker.setName(self._legend('top_marker'))
        self._topMarker._setDraggable(True)
        self._topMarker.setSymbol('s')
        self._topMarker._setConstraint(WeakMethodProxy(self.__topConstraint))
        self._topMarker.sigItemChanged.connect(self.__markerChanged)
        self._items.append(self._topMarker)

        self.__handleMarkerChanged = True

        self.setColor('pink')

    def __topConstraint(self, x: float, y: float) -> None:
        """Constraint applied on the top anchor"""
        cx, cy = self.getCenter()
        return cx, max(y, cy)

    def __bottomConstraint(self, x: float, y: float) -> None:
        """Constraint applied on the bottom anchor"""
        cx, cy = self.getCenter()
        return cx, min(y, cy)

    def __markerChanged(self, event) -> None:
        """Handle changes in markers"""
        if event == items.ItemChangedType.POSITION and self.__handleMarkerChanged:
            width, _ = self.getSize()
            cx, _ = self.getCenter()
            ybottom = self._bottomMarker.getYPosition()
            ytop = self._topMarker.getYPosition()
            height = abs(ytop - ybottom)
            cy = 0.5 * (ybottom + ytop)
            self.setCenter(cx, cy)
            self.setSize(width, height)
            marker = self.sender()
            self.dragged.emit(*marker.getPosition())

    def _update(self) -> None:
        """Update the displayed shape and send event"""
        self.__handleMarkerChanged = False
        cx, cy = self.getCenter()
        _, height = self.getSize()
        self._topMarker.setPosition(cx, cy + height / 2.)
        self._bottomMarker.setPosition(cx, cy - height / 2.)
        super()._update()
        self.__handleMarkerChanged = True


class ROI3D(qt.QObject):

    SCAN_CHANGED = 'scanChanged'
    """Event emitted when the scan info has changed"""

    sigItemChanged = qt.Signal(object)
    """Signal emitted when the ROI has changed"""

    sigMarkerDragged = qt.Signal(float)
    """Signal emitted when a marker was dragged"""

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
        self.__rois['axial'] = CircularROI()
        self.__rois['axial'].changed.connect(self.__topChanged)

        self.__rois['front'] = ExtendableRectangle()
        self.__rois['front'].changed.connect(self.__frontChanged)
        self.__rois['front'].dragged.connect(self.__markerDragged)

        self.__rois['side'] = ExtendableRectangle()
        self.__rois['side'].changed.connect(self.__sideChanged)
        self.__rois['side'].dragged.connect(self.__markerDragged)

        self.__update()
        self.setScan(Scan())

    def getName(self):
        return self.__name

    def setName(self, name):
        name = str(name)
        if name != self.__name:
            self.__name = name
            self.sigItemChanged.emit(items.ItemChangedType.NAME)

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

        self.__rois['axial'].setColor(in_color if oz <= z <= fz else out_color)
        self.__rois['axial'].setLineStyle(in_style if oz <= z <= fz else out_style)

    def getCurrentSlicePosition(self):
        return self.__currentSlices

    def __topChanged(self):
        cx, cy = self.__rois['axial'].getCenter()
        cz = self.getCenter()[2]
        self.setWidth(2 * self.__rois['axial'].getRadius())
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

    def __markerDragged(self, x, y):
        self.sigMarkerDragged.emit(y)

    def __update(self):
        cx, cy, cz = self.getCenter()

        self.__rois['axial'].setRadius(self.getWidth() / 2)
        self.__rois['axial'].setCenter(cx, cy)
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

        elif event == items.ItemChangedType.NAME:
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

class SliceModel(qt.QObject):
    """Handle current state of a slice"""

    sigCurrentIndexChanged = qt.Signal(int)
    """Signal emitted when slice index changed"""

    AXIAL = dict(title='Axial',
                 axis='Z',
                 xaxis='X',
                 yaxis='Y')

    FRONT = dict(title='Front',
                 axis='Y',
                 xaxis='X',
                 yaxis='Z')

    SIDE = dict(title='Side',
                axis='X',
                xaxis='Y',
                yaxis='Z')

    def __init__(
            self, title='Slice', axis='Index', xaxis='X', yaxis='Y', unit='mm',
            origin=(0., 0.), scale=(1., 1.),
            range_=(0, 0), normalization=(0., 1.),
            dataProvider=None):
        super().__init__()
        self.__title = title
        self.__axis = axis
        self.__xaxis = xaxis
        self.__yaxis = yaxis
        self.__unit = unit
        self.__origin = origin
        self.__scale = scale
        self.__range = range_
        self.__normalization = normalization
        self.__dataProvider = dataProvider
        self.__index = min(range_)

    # Static information

    def getTitle(self) -> str:
        """Returns the main title prefix"""
        return self.__title

    def getAxisName(self) -> str:
        """Returns the name of the axis perpendicular to the slice"""
        return self.__axis

    def getXAxisName(self) -> str:
        """Returns the name of the X axis"""
        return self.__xaxis

    def getYAxisName(self) -> str:
        """Returns the name of the Y axis"""
        return self.__yaxis

    def getUnit(self) -> str:
        """Returns the unit in use"""
        return self.__unit

    def getSliceOrigin(self):
        """Returns the origin of the slice.

        :returns: (ox, oy)
        """
        return self.__origin

    def getSliceScale(self):
        """Returns the scale factor on each axis.

        :returns: (sx, sy)
        """
        return self.__scale

    def getIndexRange(self):
        """Returns the range of the slice indices.

        :returns: (min, max)
        """
        return self.__range

    def getNormalization(self):
        """Returns the origin and scale along the axis perpendicular to the slices.

        :returns: (origin, scale factor)
        """
        return self.__normalization

    def getXAxisTitle(self) -> str:
        """Returns the title to use for the plot X axis"""
        return '%s (%s)' % (self.getXAxisName(), self.getUnit())

    def getYAxisTitle(self) -> str:
        """Returns the title to use for the plot Y axis"""
        return '%s (%s)' % (self.getYAxisName(), self.getUnit())

    # Dynamic information

    def setCurrentIndex(self, index: int) -> None:
        """Set the index of the slice to display.

        :param int index: Index of the slice (clipped to slice range)
        """
        min_, max_ = self.getIndexRange()
        index = numpy.clip(int(index), min_, max_)
        if index != self.__index:
            self.__index = index
            self.sigCurrentIndexChanged.emit(index)

    def getCurrentIndex(self) -> int:
        """Returns the current slice index."""
        return self.__index

    def setSlicePosition(self, position: float) -> None:
        """Set the index of the slice from its normalized position"""
        origin, scale = self.getNormalization()
        self.setCurrentIndex(int((position - origin) / scale))

    def getSlicePosition(self) -> int:
        """Returns the position of the slice with normalization"""
        origin, scale = self.getNormalization()
        return origin + self.getCurrentIndex() * scale

    def getData(self):
        """Returns the current slice data"""
        provider = self.__dataProvider
        if provider is None:
            data = numpy.empty((0, 0), dtype=numpy.float32)
        else:
            data = provider(self.getCurrentIndex())
            if data is None:
                data = numpy.empty((0, 0), dtype=numpy.float32)
        return data

    def getPlotTitle(self) -> str:
        """Returns title to use for plot"""
        return '%s %g %s (slice %d)' % (
            self.getTitle(),
            self.getSlicePosition(),
            self.getUnit(),
            self.getCurrentIndex())


class SlicePlot(plot.PlotWidget):
    """Bundles a plot and slider to handle states"""

    def __init__(self, parent, backend, model):
        super().__init__(parent=parent, backend=backend)

        self.setPanWithArrowKeys(False)
        self.setFocusPolicy(qt.Qt.StrongFocus)
        self.setFocus(qt.Qt.OtherFocusReason)

        self.setDataBackgroundColor('white')
        self.setKeepDataAspectRatio(True)
        self.setInteractiveMode('pan')

        self.__model = None
        self.setModel(model)

    def focusInEvent(self, event):
        self.setBackgroundColor((237, 251, 255, 255))
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.setBackgroundColor('white')

    def keyPressEvent(self, event):
        model = self.getModel()
        if model is not None:
            index = model.getCurrentIndex()

            key = event.key()
            if key in (qt.Qt.Key_Left, qt.Qt.Key_Down):
                model.setCurrentIndex(index - 1)
                return
            elif key in (qt.Qt.Key_Right, qt.Qt.Key_Up):
                model.setCurrentIndex(index + 1)
                return
            elif key == qt.Qt.Key_PageDown:
                model.setCurrentIndex(index - 10)
                return
            elif key == qt.Qt.Key_PageUp:
                model.setCurrentIndex(index + 10)
                return

        # Only call base class implementation when key is not handled.
        # See QWidget.keyPressEvent for details.
        super(SlicePlot, self).keyPressEvent(event)

    def setModel(self, model):
        """Set the model to associate to this slider

        :param SliceModel model:
        """
        if self.__model is not None:
            self.__model.sigCurrentIndexChanged.disconnect(
                self.__sliceIndexChanged)

        self.__model = model

        if model is None:
            xlabel, ylabel = '', ''
        else:
            xlabel = model.getXAxisTitle()
            ylabel = model.getYAxisTitle()

            model.sigCurrentIndexChanged.connect(self.__sliceIndexChanged)
            self.__sliceIndexChanged(model.getCurrentIndex())

        self.getXAxis().setLabel(xlabel)
        self.getYAxis().setLabel(ylabel)

    def getModel(self):
        """Returns the :class:`SliceModel` associated to this plot"""
        return self.__model

    def __sliceIndexChanged(self, index: int) -> None:
        """Handle change of slice index"""
        model = self.getModel()
        self.addImage(model.getData(),
                      scale=model.getSliceScale(),
                      origin=model.getSliceOrigin(),
                      legend='image',
                      resetzoom=False,
                      copy=False)
        self.setGraphTitle(model.getPlotTitle())

    def addXMarkerItem(self, *args, **kwargs):
        """Same as :meth:`addXMarker` but returns an item"""
        return self._getMarker(self.addXMarker(*args, **kwargs))

    def addYMarkerItem(self, *args, **kwargs):
        """Same as :meth:`addYMarker` but returns an item"""
        return self._getMarker(self.addYMarker(*args, **kwargs))

    def addShapeItem(self, xdata, ydata, legend=None, **kwargs):
        """Same as :meth:`addShape` but returns an item"""
        self.addShape(xdata, ydata, legend, **kwargs)
        for item in self.getItems():
            if isinstance(item, items.Shape) and item.getName() == legend:
                return item

    def centerSlice(self, cx, cy):
        """Center a slice to a give position.

        :param float cx:
        :param float cy:
        """
        xmin, xmax = self.getXAxis().getLimits()
        ymin, ymax = self.getYAxis().getLimits()
        half_width = 0.5 * abs(xmax - xmin)
        half_height = 0.5 * abs(ymax - ymin)
        self.getXAxis().setLimits(cx - half_width, cx + half_width)
        self.getYAxis().setLimits(cy - half_height, cy + half_height)


class SliceBrowser(HorizontalSliderWithBrowser):
    """Frame browser and slider associated to a slice model

    :param QWidget parent:
    :param SliceModel model:
    """

    def __init__(self, parent, model=None):
        super().__init__(parent)
        self.__model = None
        self.setModel(model)

    def setModel(self, model):
        """Set the model associated to this slider

        :param SliceModel model:
        """
        if self.__model is not None:
            self.__model.sigCurrentIndexChanged.disconnect(self.setValue)
            self.valueChanged.disconnect(self.__model.setCurrentIndex)

        self.__model = model

        if model is not None:
            self.setRange(*model.getIndexRange())
            self.setValue(model.getCurrentIndex())
            model.sigCurrentIndexChanged.connect(self.setValue)
            self.valueChanged.connect(model.setCurrentIndex)

    def getModel(self):
        """Returns the :class:`SliceModel` associated to this plot"""
        return self.__model


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
        self.__data = None

        self.__handleMarker = True
        self.__newROIShape = None

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
        self._createROIAction.triggered.connect(self.__createROIActionTriggered)

        # Slice model
        self._topSlice, self._frontSlice, self._sideSlice = None, None, None

        # frame browsers
        self._topBrowser = SliceBrowser(self, self._topSlice)
        self._frontBrowser = SliceBrowser(self, self._frontSlice)
        self._sideBrowser = SliceBrowser(self, self._sideSlice)

        # Plot widgets
        self.__markers = []

        self._topPlot = SlicePlot(
            parent=self, backend=backend, model=self._topSlice)
        self._topPlot.setDefaultColormap(self._colormap)
        self.__markers.extend([
            self._topPlot.addXMarkerItem(0, legend='side-marker', text='side'),
            self._topPlot.addYMarkerItem(0, legend='front-marker', text='front')])

        self._frontPlot = SlicePlot(
            parent=self, backend=backend, model=self._frontSlice)
        self._frontPlot.setDefaultColormap(self._colormap)
        self.__markers.extend([
            self._frontPlot.addXMarkerItem(0, legend='side-marker', text='side'),
            self._frontPlot.addYMarkerItem(0, legend='axial-marker', text='axial')])

        self._sidePlot = SlicePlot(
            parent=self, backend=backend, model=self._sideSlice)
        self._sidePlot.setDefaultColormap(self._colormap)
        self.__markers.extend([
            self._sidePlot.addXMarkerItem(0, legend='front-marker', text='front'),
            self._sidePlot.addYMarkerItem(0, legend='axial-marker', text='axial')])

        # Sync
        self._topPlot.sigInteractiveModeChanged.connect(
            self.__topPlotInteractiveModeChanged)

        for plot in (self._topPlot, self._frontPlot, self._sidePlot):
            plot.sigPlotSignal.connect(self.__plotChanged)

        for marker in self.__markers:
            dim = ('axial', 'front', 'side').index(marker.getText())
            marker._setConstraint(functools.partial(self.__lineMarkerConstraint, dim))
            marker._setDraggable(True)
            marker.setColor('pink')
            marker.setLineStyle('--')
            marker.sigItemChanged.connect(self.__lineMarkerChanged)

        self.__update()  # Update models

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
        title = "%s (along %s)" % (self._topSlice.getTitle(),
                                   self._topSlice.getAxisName())
        form.addRow(title, self._topBrowser)

        title = "%s (along %s)" % (self._frontSlice.getTitle(),
                                   self._frontSlice.getAxisName())
        form.addRow(title, self._frontBrowser)

        title = "%s (along %s)" % (self._sideSlice.getTitle(),
                                   self._sideSlice.getAxisName())
        form.addRow(title, self._sideBrowser)
        
        # Toolbars
        toolbar = qt.QToolBar(self)
        self.addToolBar(qt.Qt.TopToolBarArea, toolbar)

        action = plot_actions.mode.ZoomModeAction(
            parent=self, plot=self._topPlot)
        toolbar.addAction(action)

        action = plot_actions.mode.PanModeAction(
            parent=self, plot=self._topPlot)
        toolbar.addAction(action)

        toolbar.addAction(self._createROIAction)

        toolbar.addSeparator()

        action = plot_actions.control.ResetZoomAction(
            parent=self, plot=self._topPlot)
        action.triggered.connect(self.__resetZoom)
        toolbar.addAction(action)

        toolbar.addAction(plot_actions.control.ColormapAction(
            parent=self, plot=self._topPlot))

    def __topPlotInteractiveModeChanged(self, source):
        """Synchronize interactive mode between plots"""
        if source is not self._createROIAction:  # Sync create ROI action
            self._createROIAction.setChecked(False)

        mode = self._topPlot.getInteractiveMode()
        for plot in (self._frontPlot, self._sidePlot):
            plot.setInteractiveMode(source=source, **mode)

    def __resetZoom(self, checked):
        self._frontPlot.resetZoom()
        self._sidePlot.resetZoom()

    def __lineMarkerChanged(self, event):
        if self.__handleMarker and event is items.ItemChangedType.POSITION:
            marker = self.sender()
            face = marker.getLegend().split('-')[0]

            x, y = marker.getPosition()
            position = y if x is None else x
            if face == 'side':
                self._sideSlice.setSlicePosition(position)
            elif face == 'front':
                self._frontSlice.setSlicePosition(position)
            elif face == 'axial':
                self._topSlice.setSlicePosition(position)

    def __lineMarkerConstraint(self, dim, x, y):
        min_ = self.getOrigin()[dim]
        data = self.getData()
        max_ = 0 if data is None else data.shape[dim]
        max_ = min_ + self.getResolution()[dim] * max_
        return numpy.clip(x, min_, max_), numpy.clip(y, min_, max_)

    def __createROIActionTriggered(self, checked=False):
        """Handle create ROI Action"""
        if checked:
            self._topPlot.setInteractiveMode(
                mode='select-draw',
                color=(0., 0., 0., 0.),
                shape='polylines',
                label='drawroi',
                zoomOnWheel=True,
                source=self._createROIAction)

    def __plotChanged(self, event):
        """Handle signal from the plots"""
        if not self._createROIAction.isChecked():
            return

        if event['event'] == 'drawingProgress':
            plot = self.sender()
            self.__newROIShape = plot.addShapeItem(
                xdata=event['xdata'],
                ydata=event['ydata'],
                legend='new roi contour',
                shape='polygon',
                color='red',
                fill=False,
                overlay=True)

        if event['event'] == 'drawingFinished':
            plot = self.sender()
            if self.__newROIShape is not None:
                plot.removeItem(self.__newROIShape)
                self.__newROIShape = None
            if plot is self._topPlot:
                coords = numpy.transpose((
                    event['xdata'],
                    event['ydata'],
                    self._topSlice.getSlicePosition() * numpy.ones(len(event['xdata']))))
            elif plot is self._frontPlot:
                coords = numpy.transpose((
                    event['xdata'],
                    self._frontSlice.getSlicePosition() * numpy.ones(len(event['xdata'])),
                    event['ydata']))
            else:  # plot is self._sidePlot
                coords = numpy.transpose((
                    self._sideSlice.getSlicePosition() * numpy.ones(len(event['xdata'])),
                    event['xdata'],
                    event['ydata']))

            self.__addROI3DFromSelection(coords)

    def __addROI3DFromSelection(self, points):
        """Create a ROI from a selection done with a set of points.

        :param numpy.ndarray points: Nx3 array of points (x, y, z)
        """
        # TODO select right scan
        scan = self._scanComboBox.currentData()

        center = 0.5 * (numpy.max(points, axis=0) + numpy.min(points, axis=0))
        radius = numpy.max(numpy.linalg.norm(points[:, :2] - center[:2], axis=1))
        if radius < 0.01: # TODO make constraints
            radius = 0.01
        height = numpy.max(points[:, 2]) - numpy.min(points[:, 2])
        if height == 0:
            height = 2 * radius  # Fallback for top slice selection

        roi = ROI3D()
        roi.setName('%03d' % self.__roi_index)
        self.__roi_index += 1
        roi.setScan(scan)
        roi.setWidth(2 * radius)
        roi.setHeight(height)
        roi.setCurrentSlicePosition(
            self._sideSlice.getSlicePosition(),
            self._frontSlice.getSlicePosition(),
            self._topSlice.getSlicePosition())
        roi.setCenter(*center)

        roi.getROI('axial').addToPlot(self._topPlot)
        roi.getROI('front').addToPlot(self._frontPlot)
        roi.getROI('side').addToPlot(self._sidePlot)
        self._roitable.addROI3D(roi)

        roi.sigMarkerDragged.connect(self._topSlice.setSlicePosition)

    def __sliceChanged(self, face, value):
        """Handle slice change

        :param str face:
        :param int value:
        """
        assert face in ('axial', 'front', 'side')
        self.__handleMarker = False

        model = self.sender()
        position = model.getSlicePosition()
        for marker in self.__markers:
            if marker.getLegend() == face + '-marker':
                marker.setPosition(position, position)

        self._roitable.setCurrentSlicePosition(
            self._sideSlice.getSlicePosition(),
            self._frontSlice.getSlicePosition(),
            self._topSlice.getSlicePosition())

        self.__handleMarker = True

    def __update(self, resetZoom=True):
        """Update the SliceModels because information has changed

        :param bool resetZoom:
        """
        res_z, res_y, res_x = self.getResolution()
        oz, oy, ox = self.getOrigin()
        unit = self.getUnit()

        if self.getData() is None:
            depth, height, width = 0, 0, 0

            topDataProvider = None
            frontDataProvider = None
            sideDataProvider = None

        else:
            depth, height, width = numpy.array(self.__data.shape) - 1

            def topDataProvider(index):
                return self.getData()[index, :, :]

            def frontDataProvider(index):
                return self.getData()[:, index, :]

            def sideDataProvider(index):
                return self.getData()[:, :, index]

        self._topSlice = SliceModel(
            origin=(ox, oy),
            scale=(res_x, res_y),
            range_=(0, depth),
            normalization=(oz, res_z),
            dataProvider=topDataProvider,
            unit=unit,
            **SliceModel.AXIAL)
        self._topSlice.sigCurrentIndexChanged.connect(
            functools.partial(self.__sliceChanged, 'axial'))
        self._topSlice.setCurrentIndex(depth // 2)
        self._topPlot.setModel(self._topSlice)
        self._topBrowser.setModel(self._topSlice)

        self._frontSlice = SliceModel(
            origin=(ox, oz),
            scale=(res_x, res_z),
            range_=(0, height),
            normalization=(oy, res_y),
            dataProvider=frontDataProvider,
            unit=unit,
            **SliceModel.FRONT)
        self._frontSlice.sigCurrentIndexChanged.connect(
            functools.partial(self.__sliceChanged, 'front'))
        self._frontSlice.setCurrentIndex(height // 2)
        self._frontPlot.setModel(self._frontSlice)
        self._frontBrowser.setModel(self._frontSlice)

        self._sideSlice = SliceModel(
            origin=(oy, oz),
            scale=(res_y, res_z),
            range_=(0, width),
            normalization=(ox, res_x),
            dataProvider=sideDataProvider,
            unit=unit,
            **SliceModel.SIDE)
        self._sideSlice.sigCurrentIndexChanged.connect(
            functools.partial(self.__sliceChanged, 'side'))
        self._sideSlice.setCurrentIndex(width // 2)
        self._sidePlot.setModel(self._sideSlice)
        self._sideBrowser.setModel(self._sideSlice)

        if resetZoom:
            self._topPlot.resetZoom()
            self._frontPlot.resetZoom()
            self._sidePlot.resetZoom()

    def updateSlices(self):
        """Update plotted data"""
        self.__update(resetZoom=False)

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
        """Set the resolution in units per pixel.

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
        """Set the offset from origin of the dataset in units

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
        self._sideSlice.setSlicePosition(cx)
        self._sidePlot.centerSlice(cy, cz)

        self._frontSlice.setSlicePosition(cy)
        self._frontPlot.centerSlice(cx, cz)

        self._topSlice.setSlicePosition(cz)
        self._topPlot.centerSlice(cx, cy)

    def setData(self, data):
        """The data to view, no copy is made.

        :param Union[None,numpy.ndarray,h5py.Dataset] data:
            3D volume, dimension convention is: (depth, row, column).
        """
        self.__data = data
        self.__update()

    def getData(self):
        """Returns the data currently viewed, no copy is made.

        :rtype: Union[None,numpy.ndarray,h5py.Dataset]
        """
        return self.__data
 

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
