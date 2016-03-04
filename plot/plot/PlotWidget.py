# -*- coding: utf-8 -*-
# /*##########################################################################
#
# Copyright (c) 2016 European Synchrotron Radiation Facility
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
# ###########################################################################*/
"""Qt-based plot widget.

This widget provides plot functionnalities.
This is the PyMca's plot API.
"""

__authors__ = ["V.A. Sole", "T. Vincent"]
__license__ = "MIT"
__date__ = "11/02/2016"


from collections import OrderedDict
import logging

from PyQt4 import QtCore, QtGui

from .plot import Plot
from .backend_mpl import BackendMPL
from . import items


logging.basicConfig()
logger = logging.getLogger(__name__)


# API changes from PyMca:
# - Remove **kw in methods

class PlotWidget(QtGui.QMainWindow):
    def __init__(self, parent=None,
                 windowFlags=QtCore.Qt.Widget, backend=None):
        self._invertYAxis = False
        self._curves = OrderedDict()

        super(PlotWidget, self).__init__(parent, windowFlags)
        self._plot = Plot()
        self._backend = BackendMPL(self._plot)
        self.setCentralWidget(self._backend)

        self._plot.axes.left.visible = True
        self._plot.axes.right.visible = False

    ################
    # Plot content #
    ################

    # Add
    # - addImage add interpolation

    def addCurve(self, x, y, legend=None, info=None,
                 replace=False, replot=True,
                 color=None, symbol=None, linewidth=None, linestyle=None,
                 xlabel=None, ylabel=None, yaxis=None,
                 xerror=None, yerror=None, z=1, selectable=True, **kw):
        if kw:
            logger.warning(
                "addCurve extra arguments deprecated")

        if replace:
            self.remove(kind='curve')

        if color is None:
            color = (0., 0., 0.)  # TODO

        assert yaxis in ('left', 'right', None)
        yaxis = 'left' if yaxis in (None, 'left') else 'right'

        # if a curve with the same name exists, remove it
        if legend in self._curves:
            oldCurve = self._curves.pop(legend)
            self._plot.removeItem(oldCurve)

        curve = items.Curve(x, y,
                            xerror=xerror, yerror=yerror, color=color,
                            copy=True,
                            marker=symbol,
                            linewidth=linewidth,
                            linestyle=linestyle,
                            z=z, selectable=selectable)
        curve.info = info
        curve.legend = legend
        curve.xlabel = xlabel
        curve.ylabel = ylabel
        curve.yaxis = yaxis

        if yaxis == 'left':
            self._plot.addItem(curve)
        else:
            self._plot.axes.right.addItem(curve)

        # TODO active curve handling

        if replot:
            self.resetZoom()

        return curve

    def addImage(self, data, legend=None, info=None,
                 replace=True, replot=True,
                 xScale=(0., 1.), yScale=(0., 1.), z=0,
                 selectable=False, draggable=False,
                 colormap=None, **kw):
        if kw:
            logger.warning(
                "addImage extra arguments deprecated")

        if replace:
            self.remove(kind='image')

        image = items.Image(data, copy=True,
                            colormap=colormap,
                            origin=(xScale[0], yScale[0]),
                            scale=(xScale[1], yScale[1]),
                            z=z,
                            selectable=selectable, draggable=draggable)
        image.legend = legend
        image.info = info
        self._plot.addItem(image)

        # TODO active image handling

        if replot:
            self.resetZoom()

        return image

    def addItem(self, xList, yList, legend=None, info=None,
                replace=False, replot=True,
                shape="polygon", fill=True, **kw):
        if kw:
            logger.warning(
                "addItem extra arguments deprecated")

        if replace:
            self.remove(kind='item')

        # TODO

        if replot:
            self.replot()

        return None

    def addMarker(self, x, y, legend=None, text=None, color='k',
                  selectable=False, draggable=False, replot=True,
                  symbol=None, constraint=None):
        # TODO
        return None

    # Remove

    def clear(self):
        pass

    def remove(self, legend=None, kind=None):
        pass

    # Get
    # TODO: getImages? getMarkers?

    def getAllCurves(self, just_legend=False):
        pass

    def getCurve(self, legend):
        pass

    def getImage(self, legend):
        pass

    def getMonotonicCurves(self):
        pass

    # Show/hide
    # TODO: usage? replace by OO.visible

    def hideCurve(self, legend, replot=True):
        if replot:
            self.replot()

    def hideImage(self, legend, replot=True):
        if replot:
            self.replot()

    def isCurveHidden(self, legend):
        pass

    def isImageHidden(self, legend):
        pass

    def showCurve(self, legend, replot=True):
        if replot:
            self.replot()

    def showImage(self, legend, replot=True):
        if replot:
            self.replot()

    ##############
    # Plot setup #
    ##############

    # Labels

    def getGraphTitle(self):
        return self._plot.title

    def setGraphTitle(self, title=""):
        self._plot.title = title

    def getGraphXLabel(self):
        return self._plot.axes.left.xlabel

    def setGraphXLabel(self, label="X"):
        self._plot.xlabel = label

    def getGraphYLabel(self):
        return self._plot.axes.left.ylabel

    def setGraphYLabel(self, label="Y"):
        self._plot.ylabel = label

    # Axes

    def isYAxisInverted(self):
        return self._invertYAxis

    def invertYAxis(self, flag=True):
        self._invertYAxis = bool(flag)
        for axes in self._plot.axes:
            begin, end = axes.ylimits
            axes.ylimits = end, begin

    def isXAxisLogarithmic(self):
        pass

    def setXAxisLogarithmic(self, flag=True):
        pass

    def isYAxisLogarithmic(self):
        pass

    def setYAxisLogarithmic(self, flag):
        pass

    def isDefaultBaseVectors(self):
        pass

    def getBaseVectors(self):
        pass

    def setBaseVectors(self, x=(1., 0.), y=(0., 1.)):
        pass

    # Limits

    # TODO check interaction with autoscale and aspect ratio

    def getGraphXLimits(self):
        start, end = self._plot.xlimits
        return min(start, end), max(start, end)

    def setGraphXLimits(self, xmin, xmax):
        self._plot.xlimits = xmin, xmax

    def getGraphYLimits(self, axis="left"):
        assert axis in ('left', 'right')
        if axis == 'left':
            axes = self._plot.axes.left
        else:
            axes = self._plot.axes.right
        start, end = axes.ylimits
        return min(start, end), max(start, end)

    def setGraphYLimits(self, ymin, ymax, axis="left"):
        assert axis in ('left', 'right')
        if axis == 'left':
            axes = self._plot.axes.left
        else:
            axes = self._plot.axes.right
        axes.ylimits = (ymax, ymin) if self._invertYAxis else (ymin, ymax)

    def setLimits(self, xmin, xmax, ymin, ymax):
        self.setGraphXLimits(xmin, xmax)
        self.setGraphYLimits(ymin, ymax)

    def isXAxisAutoScale(self):
        pass

    def setXAxisAutoScale(self, flag=True):
        pass

    def isYAxisAutoScale(self):
        pass

    def setYAxisAutoScale(self, flag=True):
        pass

    def resetZoom(self, dataMargins=None):
        pass

    def replot(self):
        pass

    # plot

    def isKeepDataAspectRatio(self):
        pass

    def keepDataAspectRatio(self, flag=True):
        pass

    def showGrid(self, flag=True):
        pass

    def getDataMargins(self):
        pass

    def setDataMargins(self, xMinMargin=0., xMaxMargin=0.,
                       yMinMargin=0., yMaxMargin=0.):
        pass

    ############
    # Defaults #
    ############
    # TODO: add getDefaultPlotPoints, getDefaultPlotLines
    # def setDefaults(self, colormap, symbol, linestyle, linewidth, colors)
    # def getDefaults(self) -> dict

    def getSupportedColormaps(self):
        pass

    def getDefaultColormap(self):
        pass

    def setDefaultColormap(self, colormap=None):
        pass

    def setDefaultPlotPoints(self, flag):
        pass

    def setDefaultPlotLines(self, flag):
        pass

    #########
    # Utils #
    #########

    def dataToPixel(self, x=None, y=None, axis="left"):
        pass

    def pixelToData(self, x=None, y=None, axis="left"):
        pass

    def getWidgetHandle(self):
        return self

    #############
    # Selection #
    #############
    # TODO:
    # - rename enableActiveCurveHandling -> setActiveCurveHandling
    # - missing activeImage handling + combine with active curve

    def isActiveCurveHandlingEnabled(self):
        pass

    def enableActiveCurveHandling(self, flag=True):
        pass

    def setActiveCurveColor(self, color="#000000"):
        pass

    def getActiveCurve(self, just_legend=False):
        pass

    def setActiveCurve(self, legend, replot=True):
        if replot:
            self.replot()

    def getActiveImage(self, just_legend=False):
        pass

    def setActiveImage(self, legend, replot=True):
        if replot:
            self.replot()

    ###############
    # Interaction #
    ###############
    # TODO:
    # - getDrawMode + isDrawModeEnabled
    # - Issue: setDrawMode/setZoomMode have interactions

    def getGraphCursor(self):
        pass

    def setGraphCursor(self, flag=None, color=None,
                       linewidth=None, linestyle=None):
        pass

    def isDrawModeEnabled(self):
        pass

    def getDrawMode(self):
        pass

    def setDrawModeEnabled(self, flag=True, shape="polygon", label=None,
                           color=None, **kw):
        pass

    def isZoomModeEnabled(self):
        pass

    def setZoomModeEnabled(self, flag=True, color=None):
        pass

    def isPanWithArrowKeys(self):
        pass

    def setPanWithArrowKeys(self, pan=False):
        pass

    #########
    # Misc. #
    #########

    def saveGraph(self, fileName, fileFormat='svg', dpi=None, **kw):
        pass

    def printGraph(self, width=None, height=None, xOffset=0.0, yOffset=0.0,
                   units="inches", dpi=None, printer=None,
                   dialog=True, keepAspectRatio=True, **kw):
        pass

    def setCallback(self, callbackFunction):
        pass

    ##############

    def insertMarker(self, x, y, legend=None, text=None, color='k',
                     selectable=False, draggable=False, replot=True,
                     symbol=None, constraint=None, **kw):
        logger.warning('insertMarker deprecated, use addMarker instead')
        return self.addMarker(x, y, legend, text, color,
                              selectable, draggable, replot,
                              symbol, constraint)

    def insertXMarker(self, x, legend=None, text=None, color='k',
                      selectable=False, draggable=False, replot=True,
                      **kw):
        logger.warning(
            'insertXMarker deprecated, use addMarker with y=None instead')
        return self.addMarker(x, None, legend, text, color,
                              selectable, draggable, replot,
                              None, None)

    def insertYMarker(self, y, legend=None, text=None, color='k',
                      selectable=False, draggable=False, replot=True,
                      **kw):
        logger.warning(
            'insertYMarker deprecated, use addMarker with x=None instead')
        return self.addMarker(None, y, legend, text, color,
                              selectable, draggable, replot,
                              None, None)

    def clearCurves(self):
        logger.warning(
            "clearCurves deprecated, use remove(kind='curve') instead")
        self.remove(kind='curve')

    def clearImages(self):
        logger.warning(
            "clearCurves deprecated, use remove(kind='image') instead")
        self.remove(kind='image')

    def clearMarkers(self):
        logger.warning(
            "clearCurves deprecated, use remove(kind='markers') instead")
        self.remove(kind='markers')

    def removeCurve(self, legend, replot=True):
        logger.warning(
            "removeCurve deprecated, use remove instead")
        self.remove(legend, kind='curve')
        if replot:
            self.replot()

    def removeImage(self, legend, replot=True):
        logger.warning(
            "removeImage deprecated, use remove instead")
        self.remove(legend, kind='image')
        if replot:
            self.replot()

    def removeItem(self, legend, replot=True):
        logger.warning(
            "removeItem deprecated, use remove instead")
        self.remove(legend, kind='item')
        if replot:
            self.replot()

    def removeMarker(self, legend, replot=True):
        logger.warning(
            "removeMarker deprecated, use remove instead")
        self.remove(legend, kind='marker')
        if replot:
            self.replot()
