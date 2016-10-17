# coding: utf-8
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
"""Interactive test script for silx/PyMca PlotWindow

Script options:

- pymca: To use PyMca PlotWindow (default is using silx)
- gl: To use OpenGL backend (only with PyMca, default is matplotlib)
"""


# import ######################################################################

import logging
import sys
import time

import numpy as np
from uuid import uuid4

logging.basicConfig()
logger = logging.getLogger()

# import PySide

if hasattr(sys, 'argv') and 'pymca' in sys.argv:
    BACKEND = 'pymca'
    logger.warning('Using PyMca PlotWindow')
    from PyMca5.PyMcaGui import PyMcaQt as qt
    from PyMca5.PyMcaGui.plotting.PlotWindow import PlotWindow
else:
    BACKEND = 'silx'
    logger.warning('Using silx PlotWindow')
    from silx.gui import qt
    from silx.gui.plot import PlotWindow

    # logging.getLogger('silx.gui.plot.Plot').setLevel(logging.ERROR)


# TestWindow ##################################################################

class TestWindow(PlotWindow):
    _COLORS = 'black', 'red', 'green', 'blue', None  # 'video inverted'

    def __init__(self, parent, backend):
        self._colorIndex = 0
        self.__grid = 0
        self.__activeCurve = True

        if BACKEND == 'silx':
            super(TestWindow, self).__init__(
                parent=parent, backend=backend,
                control=True,
                position=[('X', lambda x, y: x),
                          ('Y', lambda x, y: y),
                          ('Value', self._getValue)])
            from silx.gui.plot import PlotTools
            self.profileToolBar = PlotTools.ProfileToolBar(self)
            self.addToolBar(self.profileToolBar)
        else:
            super(TestWindow, self).__init__(
                parent=parent, backend=backend, aspect=True, colormap=True,
                control=True, position=True, roi=True)

        self._initMenuBar()
        self.show()

        # self.sigPlotSignal.connect(self._plotCallback)
        testImage(self) #testLog(self)
        self.setPanWithArrowKeys(True)

    def _getValue(self, x, y):
        image = self.getActiveImage()
        if image is None:
            return 'No image'
        else:
            data, params = image[0], image[4]
            try:
                row = int((y - params['origin'][1]) / params['scale'][1])
                col = int((x - params['origin'][0]) / params['scale'][0])
            except ValueError:
                return '-'
            try:
                value = data[row, col]
            except IndexError:
                return '-'
            else:
                return row, col, data[row, col]

    def doReplot(self, *args, **kwargs):
        """Only calls replot when using PyMca, it is useless with silx."""
        if BACKEND == 'pymca':
            super(TestWindow, self).replot(*args, **kwargs)

    def _plotCallback(self, eventDict=None):
        if eventDict['event'] != 'mouseMoved':
            print(eventDict)
        if eventDict['event'] == 'curveClicked':
            print('setActiveCurve', eventDict['label'])
            self.setActiveCurve(eventDict['label'])
        if eventDict['event'] == 'drawingFinished':
            shape = eventDict['type']
            if shape in ['polygon', 'rectangle']:
                self.addItem(
                    xdata=eventDict['xdata'],
                    ydata=eventDict['ydata'],
                    legend=str(uuid4()), info=None,
                    replace=False,
                    shape=eventDict['type'], fill=True,
                    color="#000000")
            elif shape in ['hline', 'vline', 'line']:
                self.addItem(
                    xdata=eventDict['xdata'],
                    ydata=eventDict['ydata'],
                    legend=str(uuid4()), info=None,
                    replace=False,
                    shape=eventDict['type'], fill=False,
                    color="#0000FF")

    def _initMenuBar(self):
        # Menu VIEW
        menu = self.menuBar().addMenu('View')
        menu.addAction('resetZoom()', self.resetZoom)

        def resetDataMargins():
            self.setDataMargins()
        menu.addAction('setDataMargins()', resetDataMargins)

        def setDataMargins():
            self.setDataMargins(0.1, 0.2, 0.3, 0.4)
        menu.addAction('setDataMargins(.1, .2, .3, .4)', setDataMargins)

        def resetZoom():
            self.resetZoom((0.4, 0.3, 0.2, 0.1))
        menu.addAction('resetZoom(0.4, 0.3, 0.2, 0.1)', resetZoom)

        def toggleAutoScaleX():
            self.setXAxisAutoScale(not self.isXAxisAutoScale())
            self.statusBar().showMessage('Axis autoscale X: %s, Y: %s' %
                                         (self.isXAxisAutoScale(),
                                          self.isYAxisAutoScale()))
        menu.addAction('Toggle Autoscale X', toggleAutoScaleX)

        def toggleAutoScaleY():
            self.setYAxisAutoScale(not self.isYAxisAutoScale())
            self.statusBar().showMessage('Axis autoscale X: %s, Y: %s' %
                                         (self.isXAxisAutoScale(),
                                          self.isYAxisAutoScale()))
        menu.addAction('Toggle Autoscale Y', toggleAutoScaleY)

        def keepAspectRatio():
            self.keepDataAspectRatio(not self.isKeepDataAspectRatio())
            # Ugly workaround Plot not forwarding isKeepDataAspectRatio
        menu.addAction('Keep aspect ratio', keepAspectRatio)

        def invertYAxis():
            self.invertYAxis(not self.isYAxisInverted())
            self.doReplot()
        menu.addAction('Invert Y axis', invertYAxis)

        def changeGrid():
            self.__grid = (self.__grid + 1) % 4
            self.showGrid(self.__grid)
            self.statusBar().showMessage('Grid mode: %d' % self.__grid)
        menu.addAction('Change Grid', changeGrid)

        def toggleCursor():
            cursor = self.getGraphCursor()
            if cursor is None:
                self.setGraphCursor(True, color='red', linewidth=1)
            else:
                self.setGraphCursor(False)
            self.statusBar().showMessage('Cursor mode: %s' %
                                         str(self.getGraphCursor()))
        menu.addAction('Toggle Cursor', toggleCursor)

        def toggleLogX():
            self.setXAxisLogarithmic(not self.isXAxisLogarithmic())
            self.doReplot()
            self.statusBar().showMessage('Log Scale X: %s, Y: %s' %
                                         (self.isXAxisLogarithmic(),
                                          self.isYAxisLogarithmic()))
        menu.addAction('Toggle Log X', toggleLogX)

        def toggleLogY():
            self.setYAxisLogarithmic(not self.isYAxisLogarithmic())
            self.doReplot()
            self.statusBar().showMessage('Log Scale X: %s, Y: %s' %
                                         (self.isXAxisLogarithmic(),
                                          self.isYAxisLogarithmic()))
        menu.addAction('Toggle Log Y', toggleLogY)

        def toggleLogY():
            self.setYAxisLogarithmic(not self.isYAxisLogarithmic())
            self.doReplot()
            self.statusBar().showMessage('Log Scale X: %s, Y: %s' %
                                         (self.isXAxisLogarithmic(),
                                          self.isYAxisLogarithmic()))
        menu.addAction('Toggle Log Y', toggleLogY)

        def toggleActiveCurve():
            self.enableActiveCurveHandling(
                not self.isActiveCurveHandlingEnabled())
            self.doReplot()
            self.statusBar().showMessage('Active curve handling: %s' %
                self.isActiveCurveHandlingEnabled())
        menu.addAction('Toggle Active Curve Handling', toggleActiveCurve)

        def changeBaseVectors():
            baseVectors = self._plot.getBaseVectors()
            if baseVectors == ((1., 0.), (0., 1.)):
                baseVectors = (1., 0.5), (0.3, 1.)
            else:
                baseVectors = (1., 0.), (0., 1.)
            self.setBaseVectors(*baseVectors)
            self.doReplot()
        menu.addAction('Change base vectors', changeBaseVectors)

        # Menu INTERACTION
        menu = self.menuBar().addMenu('Interaction')

        def zoomMode():
            self._colorIndex = (self._colorIndex + 1) % len(self._COLORS)
            color = self._COLORS[self._colorIndex]
            self.statusBar().showMessage('Enable zoom, color: %s' % color)
            self.setZoomModeEnabled(True, color)
        menu.addAction('Zoom Mode', zoomMode)

        def drawPolygon():
            self.setDrawModeEnabled(True, 'polygon', label='mask',
                                    color='red')
        menu.addAction('Draw Polygon', drawPolygon)

        def drawRect():
            self.setDrawModeEnabled(True, 'rectangle', label='mask')
        menu.addAction('Draw Rectangle', drawRect)

        def drawLine():
            self.setDrawModeEnabled(True, 'line', label='LINE')
        menu.addAction('Draw Line', drawLine)

        def drawHLine():
            self.setDrawModeEnabled(True, 'hline', label='HORIZONTAL')
        menu.addAction('Draw Horiz. Line', drawHLine)

        def drawVLine():
            self.setDrawModeEnabled(True, 'vline', label='VERTICAL')
        menu.addAction('Draw Vert. Line', drawVLine)

        def toggleActiveCurve():
            self.__activeCurve = not self.__activeCurve
            self.enableActiveCurveHandling(self.__activeCurve)
            self.statusBar().showMessage(
                'Active curve handling: %s' % self.__activeCurve)
        menu.addAction('Toggle active curve', toggleActiveCurve)

        def panMode():
            if hasattr(self, 'setInteractiveMode'):  # silx
                self.setInteractiveMode('pan')
            else:  # matplotlib OpenGL backend
                self._plot.setInteractiveMode('pan')
        action = menu.addAction('Pan Mode', panMode)
        if (not hasattr(self, 'setInteractiveMode') and
                not hasattr(self._plot, 'setInteractiveMode')):
            action.setEnabled(False)

        # Menu DATA
        menu = self.menuBar().addMenu('Data')

        def clear():
            self.resetTimer()
            self.clear()
        menu.addAction('Clear', self.clear)

        def saveAsSvg():
            filename = 'testSaveGraph.svg'
            self.saveGraph(filename, 'svg')
            self.statusBar().showMessage('Saved as %s' % filename)
        menu.addAction('Save as svg', saveAsSvg)

        def toggleRightAxis():
            curve = self.getCurve("rightTest")
            if curve is None:
                data = np.arange(1000., dtype=np.float32)
                self.addCurve(data, np.sqrt(data), legend="rightTest",
                              replace=False, replot=True, z=5,
                              color='black', linestyle="-",
                              selectable=True,
                              xlabel="Right X", ylabel="Right Y",
                              yaxis="right")
            else:
                self.removeCurve("rightTest")
        menu.addAction('Right axis data', toggleRightAxis)

        def setUInt16Data():
            dataUInt16 = np.arange(1024*1024, dtype=np.uint16)
            dataUInt16.shape = 1024, -1

            colormap2 = {'name': 'temperature', 'normalization': 'linear',
                         'autoscale': False,
                         'vmin': 1.0, 'vmax': dataUInt16.max(),
                         'colors': 256}
            self.addImage(dataUInt16, legend="image 2",
                          xScale=(0, 1.0), yScale=(100., 1.0),
                          replace=False, replot=True,
                          colormap=colormap2, alpha=0.5)
        menu.addAction('DataSet uint16 1', setUInt16Data)

        def setUInt16Data2():
            dataUInt16 = np.arange(1024*1024, dtype=np.uint16) + 10000
            dataUInt16.shape = 1024, -1

            colormap2 = {'name': 'temperature', 'normalization': 'linear',
                         'autoscale': False, 'vmin': 1.0,
                         'vmax': dataUInt16.max(),
                         'colors': 256}
            self.addImage(dataUInt16, legend="image 2",
                          xScale=(0, 1.0), yScale=(0., 1.0),
                          replace=False, replot=True,
                          colormap=colormap2)
        menu.addAction('DataSet uint16 2', setUInt16Data2)

        def testEverythingAction():
            self.resetTimer()
            self.clear()
            self.resetZoom()
            testEverything(self)
        menu.addAction('Test everything', testEverythingAction)

        def testLogAction():
            self.resetTimer()
            self.clear()
            self.resetZoom()
            testLog(self)
        menu.addAction('Test Log', testLogAction)

        def testErrorBarsAction():
            self.resetTimer()
            self.clear()
            self.resetZoom()
            testErrorBars(self)
        menu.addAction('Test Error Bars', testErrorBarsAction)

        def testReversedImagesAction():
            self.resetTimer()
            self.clear()
            self.resetZoom()
            testReversedImages(self)
        menu.addAction('Test Reversed Images', testReversedImagesAction)

        def testMarkersAction():
            self.resetTimer()
            self.clear()
            self.resetZoom()
            testMarkers(self)
        menu.addAction('Test Markers', testMarkersAction)

        def testScatterAction():
            self.resetTimer()
            self.clear()
            self.resetZoom()
            testScatter(self)
        menu.addAction('Test Scatter', testScatterAction)

        def testImageAction():
            self.resetTimer()
            self.clear()
            self.resetZoom()
            testImage(self)
            # self.menuBar().hide()
        menu.addAction('Test Image', testImageAction)

        def testStreamingAction():
            self.resetTimer()
            self.clear()
            self.streaming()
            self.resetZoom()
            self.useTimer(self.streaming, 100)
        menu.addAction('Test Streaming', testStreamingAction)

    def streaming(self):
        data = np.asarray(np.random.random(512*512), dtype=np.float32)
        data.shape = 512, 512
        # resetzoom=False to avoid resetZoom
        self.addImage(data, replace=False, replot=False)
        self.doReplot()

    def useTimer(self, callback, timeoutMS):
        self.timer = qt.QTimer()
        self.timer.timeout.connect(callback)
        self.timer.start(timeoutMS)

    def resetTimer(self):
        if hasattr(self, 'timer'):
            self.timer.stop()
            del self.timer

    def keyPressEvent(self, event):
        """Forward key events to plot widget...

        Find a better way to do it
        """
        super(TestWindow, self).keyPressEvent(event)


# test ########################################################################

# Testing Latin-1 characters with python 2.x
# title = u'Title !#$%&\'()*+,-./¡¢£¤¥¦§¨©ª«¬-®¯'
# xLabel = u'Rows ÐÑÒÓÔÕÖ×ØÙÚÛÜuÝÞß'
# yLabel = u'Columns ðñòóôõö÷øùúûüýþÿ'

# Testing Latin-1 characters with python 3.x
# title = 'Title !#$%&\'()*+,-./¡¢£¤¥¦§¨©ª«¬-®¯'
# xLabel = 'Rows ÐÑÒÓÔÕÖ×ØÙÚÛÜuÝÞß'
# yLabel = 'Columns ðñòóôõö÷øùúûüýþÿ'

title = 'Title'
xLabel = 'Rows'
yLabel = 'Columns'


def testEverything(w):
    """Dummy test of many stuff."""
    w.setXAxisLogarithmic(False)
    w.setYAxisLogarithmic(False)

    w.setGraphTitle(title)
    w.setGraphXLabel(xLabel)
    w.setGraphYLabel(yLabel)

    norm = 'log'

    size = 1024
    data = np.arange(float(size)*size, dtype=np.float32)
    data.shape = size, size

    dataUInt16 = np.array(data, dtype=np.uint16)
    dataUInt8 = np.array(data, dtype=np.uint8)

    w.addItem(
        xdata=np.array((0, 0, 200, 200)),
        ydata=np.array((0, 200, 200, 0)),
        legend="test", info=None,
        replace=False,
        shape="polygon", fill=True, color='blue')
    w.addItem(
        xdata=np.array((200, 200, 400, 400)),
        ydata=np.array((200, 400, 400, 200)),
        legend="test2", info=None,
        replace=False,
        shape="polygon", fill=False, color='green')
    w.addItem(
        xdata=np.array((1300, 1600, 1900, 1300, 1900)),
        ydata=np.array((-700, -200, -700, -300, -300)),
        legend="star", info=None,
        replace=False,
        shape="polygon", fill=True, color='#000000')

    colormap = {'name': 'temperature', 'normalization': 'linear',
                'autoscale': True, 'vmin': 0.0, 'vmax': 1.0,
                'colors': 256}
    w.addImage(data, legend="image 1",
               xScale=(25, 1.0), yScale=(-size, 1.0),
               replot=False, colormap=colormap, z=2)

    colormap2 = {'name': 'temperature', 'normalization': norm,
                 'autoscale': False, 'vmin': 1.0, 'vmax': dataUInt16.max(),
                 'colors': 256}
    w.addImage(dataUInt16, legend="image 2",
               xScale=(0, 1.0), yScale=(0., 1.0),
               replace=False,
               replot=False, colormap=colormap2)

    colormap3 = {'name': 'red', 'normalization': 'linear',
                 'autoscale': True, 'vmin': 0.0, 'vmax': 1.0,
                 'colors': 256}
    w.addImage(dataUInt8, legend="image 3",
               xScale=(size, 1.0), yScale=(-size/2, 1.0),
               replace=False,
               replot=False, colormap=colormap3)

    rgbData = np.array((((0, 0, 0), (128, 0, 0), (255, 0, 0)),
                        ((0, 128, 0), (0, 128, 128), (0, 128, 256))),
                       dtype=np.uint8)
    w.addImage(rgbData, legend="rgb",
               xScale=(-30, 10), yScale=(-20, 10),
               replace=False, replot=False)

    rgbaData = np.array((((0, 0, 0, .5), (.5, 0, 0, 1), (1, 0, 0, .5)),
                         ((0, .5, 0, 1), (0, .5, .5, 1), (0, 1, 1, .5))),
                        dtype=np.float32)
    w.addImage(rgbaData, legend="rgba",
               xScale=(-5, 10), yScale=(200, 10),
               replace=False, replot=False)

    size = 2000
    data2 = np.arange(float(size)*3, dtype=np.dtype(np.float32))
    data2.shape = 3, size
    w.addImage(data2, legend="image 4",
               xScale=(100, 1.0), yScale=(-200., 200.0),
               replace=False,
               replot=False, colormap=colormap3,
               selectable=True, draggable=False)

    # curves
    xData = np.arange(1000)
    yData = np.random.random(1000)
    colorData = np.array(np.random.random(3 * 1000), dtype=np.float32)
    colorData.shape = 1000, 3

    w.addCurve(xData, -50 + 10 * np.sin(xData), legend="curve 1",
               replace=False, replot=False, linestyle="", symbol="s", z=3,
               xlabel="Curve 1 X", ylabel="Curve 1 Y")  # , fill=True)
    w.addCurve(xData + 1000, xData - 1000 + 200 * yData, legend="curve 2",
               replace=False, replot=False,
               color='green',  # color=colorData,
               linestyle="-", symbol='o', selectable=True,
               xlabel="Curve 2 X", ylabel="Curve 2 Y")

    # markers
    w.insertXMarker(1000, 'testX', None, color='pink',
                    selectable=False, draggable=True)
    w.insertYMarker(-600, 'testY', 'markerY', color='black',
                    selectable=False, draggable=True)

    w.insertMarker(1000, 500, 'constraintV', 'constraint Vert', color='black',
                   selectable=False, draggable=True, symbol='o',
                   constraint='v')
    w.insertMarker(1000, 600, 'constraintH', 'constraint Horiz', color='blue',
                   selectable=False, draggable=True, symbol='d',
                   constraint='h')

    def squareConstraint(x, y):
        return min(1500, max(x, 900)), min(800, max(y, 200))

    w.insertMarker(1000, 700, 'constraint', 'constraint', color='red',
                   selectable=False, draggable=True, symbol='+',
                   constraint=squareConstraint)

    w.insertMarker(-100, 500, 'testS', 'markerSelect', color='black',
                   selectable=True, draggable=False)
    w.insertXMarker(500, 'test', 'marker', color='black',
                    selectable=False, draggable=False)

    w.resetZoom()


# test ########################################################################

def testMarkers(w):
    # markers
    w.insertXMarker(1000, 'testX', None, color='pink',
                    selectable=False, draggable=True)
    w.insertYMarker(600, 'testY', 'markerY', color='black',
                    selectable=False, draggable=True)

    w.insertMarker(1000, 500, 'constraintV', 'constraint Vert', color='black',
                   selectable=False, draggable=True, symbol='o',
                   constraint='v')
    w.insertMarker(1000, 600, 'constraintH', 'constraint Horiz', color='blue',
                   selectable=False, draggable=True, symbol='d',
                   constraint='h')

    def squareConstraint(x, y):
        return min(1500, max(x, 900)), min(800, max(y, 200))

    w.insertMarker(1000, 700, 'constraint', 'constraint', color='red',
                   selectable=False, draggable=True, symbol='*',
                   constraint=squareConstraint)

    w.insertMarker(100, 500, 'testS', 'markerSelect', color='black',
                   selectable=True, draggable=False)
    w.insertXMarker(500, 'test', 'marker', color='black',
                    selectable=False, draggable=False)

    # Add one curve
    data = np.array((1., 2000.))
    w.addCurve(x=data, y=data)

    w.resetZoom()


# test ########################################################################

def testLog(w):
    w.keepDataAspectRatio(False)
    w.setXAxisLogarithmic(True)
    w.setYAxisLogarithmic(True)

    # Items
    w.addItem(
        np.array((200, 200, 400, 400)),
        np.array((200, 40000, 40000, 200)),
        legend="test2", info=None,
        replace=False,
        shape="polygon", color='green')  # , fill=False

    # Image
    # size = 1024
    # data = np.arange(float(size)*size, dtype=np.float32)
    # data.shape = size,size
    # colormap = {'name': 'gray', 'normalization':'linear',
    #            'autoscale':True, 'vmin':0.0, 'vmax':1.0,
    #            'colors':256}
    # w.addImage(data, legend="image 1",
    #           xScale=(1.0, 1.0) , yScale=(1.0, 1.0),
    #           replot=False, colormap=colormap)

    # curves
    xData = np.arange(1000.) + 1.

    # print('add curve right')
    # w.addCurve(xData, 1./xData ** 8, legend="curve right",
    #           #color='#FF000080',
    #           replace=False, replot=False, linestyle="-", symbol="o",
    #           xlabel="curve Right X", ylabel="curve Right Y",
    #           #selectable=True,
    #           yaxis="right") #fill=True)
    # w.setActiveCurve("curve right", False)

    w.addCurve(xData, xData ** 8, legend="curve 2", z=2,
               # color='#0000FF80',
               replace=False, replot=False, linestyle="-", symbol="o",
               xlabel="curve 2 X", ylabel="curve 2 Y",
               linewidth=3,
               # selectable=True,
               yaxis="left")  # fill=True)

    w.addCurve(xData, (xData - 100.) ** 7, legend="curve minus", z=1,
               # color='#0000FF80',
               replace=False, replot=False, linestyle="--", symbol="o",
               xlabel="curve Minus X", ylabel="curve Minus Y",
               # selectable=True,
               yaxis="left")

    w.addCurve(xData, xData ** 7, legend="curve 1", z=1,
               # color='#0000FF80',
               replace=False, replot=False, linestyle=":", symbol="o",
               xlabel="curve Minus X", ylabel="curve Minus Y",
               # selectable=True,
               yaxis="left")
    # markers
    # w.insertXMarker(1000, 'testX', 'markerX', color='pink',
    #                selectable=False, draggable=True)
    # w.insertYMarker(1000, 'testY', 'markerY', color='black',
    #                selectable=False, draggable=True)
    # w.insertMarker(1000, 500, 'testXY', 'markerPt', color='black',
    #               selectable=False, draggable=True)

    w.resetZoom()


# test ########################################################################

def testErrorBars(w):
    w.enableActiveCurveHandling(False)
    w.keepDataAspectRatio(False)
    w.setXAxisLogarithmic(False)
    w.setYAxisLogarithmic(False)

    # curves
    xData = np.arange(100.) + 1.
    yData = xData
    xError = (np.arange(100.), 100. - np.arange(100.))
    yError = np.ones((100,)) * 0.5
    w.addCurve(xData, yData, legend="curve error bars",
               color='red',
               replace=False, replot=False, linestyle="-", symbol="o",
               xlabel="X", ylabel="Y",
               xerror=xError, yerror=yError,
               # selectable=True,
               yaxis="left")  # fill=True)

    size = 100
    x = np.random.random(size) * size
    y = np.random.random(size) * size
    color = np.random.random(size * 3).reshape(size, -1)

    w.addCurve(x, y, legend='scatter', color=color,
               symbol='o', linestyle=' ', xerror=1., yerror=2.)

    w.resetZoom()


# test ########################################################################

def testReversedImages(w):
    """Dummy reversed image [x|y]Scale."""
    w.setXAxisLogarithmic(False)
    w.setYAxisLogarithmic(False)

    w.setGraphTitle(title)
    w.setGraphXLabel(xLabel)
    w.setGraphYLabel(yLabel)

    size = 1024
    data = np.arange(float(size)*size, dtype=np.float32)
    data.shape = size, size
    trans = np.array(data.T, copy=True)

    w.addImage(data, legend="image1",
               xScale=(1025.0, -1.0), yScale=(513.0, -0.5),
               replace=False, replot=False, draggable=True)
    w.addImage(trans, legend="image2",
               xScale=(1025.0, -1.0), yScale=(1025.0, -0.5),
               replace=False, replot=False)

    # Workaround matplotlib inverting X axis with image with xScale < 0
    # w.setGraphXLimits(*w.getGraphXLimits())
    w.resetZoom()


# test ########################################################################

def testScatter(w):
    """Scatter plot."""
    w.setXAxisLogarithmic(False)
    w.setYAxisLogarithmic(False)

    w.setGraphTitle('Test Scatter')
    w.enableActiveCurveHandling(False)

    size = 512
    x = np.arange(size, dtype=np.float32)
    y = np.random.random(size)
    color = np.random.random(size * 3).reshape(size, -1)

    w.addCurve(x, y, legend='scatter', color=color,
               symbol='o', linestyle=' ')

    x = np.arange(size, dtype=np.float32)
    y = np.random.random(size) + 1.
    color = np.random.random(size * 3).reshape(size, -1)

    w.addCurve(x, y, legend='scatter 2', color=color,
               symbol='o', linestyle='-')

    w.resetZoom()


# test ########################################################################

def testImage(w):
    """Small image."""
    w.setXAxisLogarithmic(False)
    w.setYAxisLogarithmic(False)

    w.enableActiveCurveHandling(False)

    w.addImage(TEST_DATA, colormap={
        'name': 'temperature',
        'normalization': 'linear',
        'autoscale': True, 'vmin': 0., 'vmax': 1.})

    w.resetZoom()

# attic #######################################################################

def attic():
    # Second plot
    w2 = PlotWindow.PlotWindow(parent=None, backend=backend)
    w2.setGraphTitle('Title 2')
    w2.setGraphXLabel('Rows 2')
    w2.setGraphYLabel('Columns 2')

    size = 500
    dataList = [np.arange(float(size)*size, dtype=np.dtype(np.float32)),
                np.random.random_sample(size*size).astype(np.float32)]
    dataList[0].shape = size, size
    dataList[1].shape = size, size
    dataList[1].dtype = np.dtype(np.float32)
    xData = np.arange(2000)
    yData = [np.random.random(2000) * 500, np.random.random(2000) * 500]
    counter = 0
    times = []

    def timerTest():
        global counter, times
        colormap = {'name': 'temperature', 'normalization': 'linear',
                    'autoscale': True, 'vmin': 0.0, 'vmax': 1.0,
                    'colors': 256}
        w2.addImage(dataList[counter % len(dataList)], legend="image",
                    xScale=(0, 1.0), yScale=(0, 1.0),
                    replace=False,
                    replot=True, colormap=colormap)
        w2.addCurve(xData, yData[counter % len(yData)], legend="curve",
                    replace=False, replot=True, color='black')
        counter += 1
        if len(times) < 10:
            times.append(time.time())
        else:
            times.append(time.time())
            # fps = len(times) / (times[-1] - times[0])
            times.pop(0)
            # print('FPS', fps)

    timer = qt.QtCore.QTimer()
    qt.QtCore.QObject.connect(timer, qt.QtCore.SIGNAL("timeout()"), timerTest)

    timer.start(1000)

    w2.getWidgetHandle().show()


TEST_DATA = np.array((
    226, 228, 242, 241, 235, 239, 198, 219, 248, 224, 248, 216, 226, 257, 208, 223, 216, 221, 218, 229, 248, 238, 216, 259, 234, 231, 217, 229, 235, 204, 225, 240, 238, 235, 213, 225, 245, 214, 240, 232, 254, 235, 245, 233, 254, 234, 227, 215, 227, 249, 236, 237, 226, 220, 241, 219, 213, 225, 258, 191, 236, 224, 214, 206, 238, 255, 217, 225, 240, 249, 237, 214, 214, 241, 220, 244, 241, 239, 249, 224, 231, 214, 246, 231, 211, 239, 221, 226, 224, 225, 235, 204, 236, 222, 243, 229, 226, 213, 232, 237, 220, 206, 211, 220, 225, 249, 260, 230, 238, 228, 206, 210, 223, 229, 223, 223, 246, 254, 235,
    207, 212, 250, 223, 222, 240, 241, 237, 233, 229, 234, 190, 236, 242, 240, 209, 229, 207, 230, 240, 234, 208, 216, 233, 234, 226, 256, 237, 247, 225, 210, 224, 257, 237, 251, 237, 220, 243, 206, 222, 240, 264, 230, 213, 247, 238, 234, 225, 240, 260, 228, 214, 225, 219, 259, 248, 247, 245, 254, 229, 229, 242, 227, 244, 240, 214, 235, 217, 246, 246, 217, 236, 216, 215, 212, 200, 233, 263, 231, 253, 222, 212, 199, 261, 232, 206, 228, 202, 195, 228, 230, 210, 209, 235, 213, 234, 249, 187, 200, 202, 211, 234, 225, 244, 226, 242, 240, 201, 227, 209, 231, 221, 245, 224, 199, 231, 227, 242, 236,
    214, 234, 242, 241, 233, 224, 226, 250, 188, 231, 221, 235, 234, 210, 232, 230, 191, 219, 248, 230, 220, 249, 195, 226, 224, 219, 217, 202, 254, 235, 212, 230, 237, 238, 234, 235, 223, 230, 211, 236, 242, 248, 246, 247, 250, 281, 253, 236, 218, 211, 231, 200, 224, 208, 237, 239, 222, 219, 212, 225, 226, 221, 227, 256, 245, 233, 224, 206, 224, 200, 247, 208, 227, 218, 196, 243, 236, 234, 215, 217, 224, 245, 225, 220, 247, 230, 247, 213, 246, 228, 233, 207, 224, 256, 201, 222, 211, 245, 218, 227, 240, 197, 256, 195, 208, 257, 230, 222, 239, 222, 203, 198, 225, 205, 235, 204, 264, 243, 231,
    235, 221, 258, 239, 216, 260, 237, 216, 238, 228, 226, 216, 243, 241, 216, 216, 222, 240, 226, 224, 205, 203, 230, 243, 212, 221, 239, 241, 241, 204, 201, 241, 217, 212, 237, 237, 233, 225, 239, 225, 229, 301, 397, 597, 587, 369, 275, 247, 238, 240, 227, 224, 230, 238, 230, 214, 211, 237, 243, 244, 228, 238, 206, 230, 215, 203, 216, 233, 239, 222, 252, 244, 254, 218, 222, 240, 202, 250, 197, 228, 207, 230, 205, 210, 247, 236, 248, 219, 271, 221, 227, 216, 227, 222, 215, 227, 216, 254, 235, 215, 242, 231, 230, 246, 215, 225, 233, 257, 225, 229, 227, 196, 220, 238, 228, 202, 211, 237, 229,
    215, 235, 186, 216, 240, 256, 228, 247, 238, 210, 245, 244, 213, 238, 234, 233, 203, 236, 223, 253, 236, 264, 216, 206, 239, 232, 201, 249, 242, 211, 231, 219, 197, 253, 235, 206, 234, 215, 233, 261, 240, 386, 1725, 5792, 5959, 3810, 965, 295, 251, 264, 256, 219, 247, 245, 221, 218, 222, 236, 219, 235, 210, 207, 259, 234, 212, 228, 226, 258, 199, 222, 220, 225, 222, 202, 242, 229, 234, 210, 229, 200, 241, 213, 240, 226, 226, 209, 227, 208, 254, 220, 219, 182, 206, 234, 227, 215, 217, 220, 213, 253, 216, 232, 208, 225, 232, 234, 225, 210, 203, 264, 237, 204, 221, 213, 258, 231, 215, 225, 244,
    223, 228, 217, 248, 226, 236, 201, 240, 207, 233, 215, 230, 231, 250, 219, 240, 205, 235, 221, 217, 222, 227, 251, 237, 224, 214, 235, 233, 255, 217, 235, 230, 233, 231, 233, 214, 236, 235, 270, 274, 499, 4198, 9829, 8252, 9536, 4991, 741, 252, 252, 228, 220, 235, 209, 222, 205, 228, 231, 264, 242, 236, 233, 248, 218, 251, 246, 220, 249, 234, 223, 225, 253, 224, 204, 225, 213, 226, 223, 206, 251, 249, 216, 216, 205, 203, 235, 231, 236, 202, 223, 235, 214, 238, 222, 240, 252, 220, 232, 242, 205, 229, 206, 226, 237, 211, 234, 220, 233, 255, 230, 209, 234, 220, 243, 183, 218, 236, 216, 232, 238,
    236, 220, 219, 234, 192, 210, 229, 255, 255, 220, 206, 222, 238, 241, 216, 237, 229, 225, 235, 249, 255, 223, 224, 234, 229, 215, 212, 240, 249, 222, 226, 238, 225, 236, 226, 221, 231, 256, 261, 255, 548, 3225, 8745, 6302, 7572, 14054, 4268, 547, 341, 271, 289, 259, 260, 239, 264, 240, 254, 231, 244, 222, 249, 222, 202, 218, 250, 221, 235, 217, 223, 214, 224, 210, 224, 250, 210, 240, 214, 235, 250, 198, 221, 217, 184, 237, 210, 204, 226, 233, 218, 211, 224, 209, 241, 257, 236, 224, 244, 235, 223, 223, 223, 266, 234, 238, 207, 223, 230, 221, 228, 226, 216, 205, 203, 239, 231, 215, 221, 225, 217,
    218, 224, 239, 224, 226, 241, 207, 240, 221, 222, 222, 224, 229, 236, 235, 215, 228, 243, 202, 216, 219, 231, 239, 227, 237, 225, 238, 246, 236, 264, 260, 262, 242, 252, 220, 285, 297, 382, 638, 1440, 3705, 6656, 6965, 6215, 13217, 9489, 2579, 1206, 1209, 1189, 1152, 1060, 964, 790, 585, 450, 347, 303, 227, 236, 202, 216, 245, 218, 230, 242, 233, 211, 215, 224, 227, 208, 223, 214, 224, 193, 248, 236, 236, 191, 233, 217, 243, 208, 221, 213, 222, 227, 239, 219, 253, 233, 228, 219, 234, 235, 235, 222, 239, 220, 211, 219, 211, 225, 226, 269, 192, 239, 234, 228, 230, 217, 234, 213, 214, 231, 209, 225, 218,
    173, 202, 234, 236, 217, 229, 203, 257, 224, 225, 214, 235, 227, 221, 233, 203, 209, 219, 228, 201, 266, 247, 232, 222, 244, 232, 265, 258, 275, 251, 241, 231, 313, 398, 527, 738, 1187, 1823, 2703, 3010, 3563, 4929, 6175, 7530, 8699, 10691, 5792, 1905, 1215, 1204, 1196, 1251, 1209, 1249, 1451, 1783, 1847, 1460, 799, 497, 319, 271, 209, 246, 214, 205, 213, 262, 237, 240, 240, 221, 243, 198, 232, 252, 209, 235, 194, 195, 223, 233, 227, 210, 225, 185, 222, 220, 226, 206, 253, 218, 241, 228, 238, 225, 211, 230, 200, 253, 223, 215, 217, 233, 217, 234, 220, 247, 239, 237, 242, 228, 254, 241, 232, 216, 259, 261, 208,
    219, 222, 214, 238, 223, 236, 236, 236, 221, 221, 216, 197, 231, 228, 233, 231, 229, 226, 226, 225, 228, 225, 230, 274, 267, 319, 284, 336, 376, 526, 887, 1386, 1875, 2044, 1917, 2102, 2440, 2905, 3546, 3773, 4548, 8639, 10594, 10138, 10459, 9246, 3735, 1792, 1508, 1325, 1307, 1111, 1039, 1166, 1132, 1290, 1414, 1485, 1550, 1632, 984, 449, 307, 243, 236, 224, 208, 243, 247, 218, 221, 238, 221, 212, 202, 229, 226, 242, 232, 239, 233, 231, 225, 220, 213, 212, 231, 218, 238, 237, 231, 238, 213, 245, 209, 236, 224, 215, 201, 200, 223, 203, 203, 231, 218, 224, 223, 200, 218, 228, 234, 212, 228, 234, 220, 227, 210, 226, 225,
    214, 220, 232, 227, 239, 233, 208, 239, 241, 241, 232, 246, 260, 233, 218, 237, 244, 256, 213, 235, 222, 265, 256, 286, 394, 964, 1304, 1664, 2538, 3115, 2939, 2589, 2205, 2295, 2774, 3467, 4305, 4756, 3716, 3318, 3136, 5070, 6165, 5558, 6656, 10540, 4836, 2040, 2092, 2524, 2900, 2764, 1983, 1444, 1190, 1161, 1146, 1402, 1603, 1625, 1429, 1434, 1350, 819, 379, 288, 241, 228, 242, 224, 254, 219, 262, 231, 205, 209, 235, 230, 218, 252, 229, 240, 243, 215, 203, 194, 224, 228, 200, 220, 220, 216, 211, 208, 218, 214, 243, 241, 212, 239, 231, 203, 205, 216, 210, 231, 198, 242, 232, 195, 227, 212, 234, 230, 209, 242, 219, 222, 208,
    229, 244, 228, 205, 246, 234, 231, 230, 221, 237, 225, 242, 238, 225, 212, 242, 205, 229, 218, 246, 238, 244, 297, 986, 5326, 11440, 14208, 10889, 8389, 6146, 5526, 5608, 6183, 7177, 7727, 7702, 7060, 6040, 4775, 3793, 3340, 3318, 3667, 4870, 7658, 6513, 2217, 1212, 1051, 1109, 1213, 1356, 1820, 2734, 2675, 1900, 1551, 1305, 1324, 1619, 1645, 1543, 1347, 1307, 1268, 572, 306, 246, 240, 234, 228, 214, 218, 222, 209, 227, 264, 201, 224, 214, 210, 222, 205, 220, 237, 205, 225, 213, 214, 222, 180, 235, 226, 255, 207, 249, 204, 222, 228, 213, 204, 224, 258, 207, 234, 232, 211, 237, 211, 216, 224, 207, 196, 233, 209, 221, 230, 240, 205,
    236, 201, 221, 223, 235, 248, 253, 198, 218, 253, 252, 215, 256, 211, 214, 230, 232, 230, 230, 237, 238, 237, 486, 3444, 8578, 9163, 9582, 10298, 10359, 10170, 9255, 9090, 8527, 7653, 6917, 6343, 4964, 4462, 3790, 2899, 2950, 2898, 2903, 4103, 5277, 5420, 2810, 961, 782, 755, 764, 774, 885, 937, 1085, 1593, 2554, 2801, 1932, 1475, 1423, 1336, 1353, 1217, 1381, 1524, 1097, 467, 287, 229, 228, 234, 230, 211, 234, 227, 230, 224, 213, 226, 194, 213, 220, 225, 233, 227, 210, 227, 209, 253, 207, 244, 223, 217, 207, 221, 220, 206, 238, 213, 216, 210, 208, 221, 238, 260, 215, 216, 206, 226, 210, 221, 232, 232, 216, 230, 224, 231, 220,
    204, 241, 221, 225, 206, 194, 229, 225, 217, 237, 201, 229, 234, 206, 220, 214, 216, 238, 226, 237, 250, 314, 1252, 5975, 7807, 8075, 8168, 9170, 7907, 8083, 7417, 6168, 6163, 5724, 5452, 5662, 5890, 4934, 4151, 3663, 2903, 3120, 3674, 3717, 3734, 4891, 4135, 1307, 797, 739, 653, 675, 671, 757, 799, 869, 917, 1076, 1422, 2703, 2721, 1794, 1420, 1264, 1000, 1106, 1313, 1434, 1154, 456, 265, 261, 249, 195, 207, 246, 209, 255, 217, 212, 214, 226, 256, 219, 228, 202, 215, 211, 228, 222, 220, 194, 255, 215, 227, 235, 219, 249, 242, 236, 240, 216, 212, 249, 249, 201, 213, 207, 211, 238, 231, 205, 207, 226, 249, 235, 215, 197, 227,
    204, 241, 218, 249, 218, 243, 238, 233, 258, 233, 230, 220, 243, 214, 225, 230, 218, 217, 231, 262, 371, 1671, 4440, 5789, 7201, 8389, 7752, 6504, 5903, 5115, 4379, 3689, 4388, 3916, 3912, 3899, 3860, 4101, 4699, 4286, 4542, 4202, 3610, 2967, 3690, 5294, 4768, 1477, 968, 875, 693, 605, 717, 683, 762, 781, 760, 792, 837, 1004, 1436, 2763, 2912, 1767, 1205, 985, 1011, 1319, 1393, 1350, 707, 355, 249, 246, 235, 226, 202, 217, 246, 195, 196, 197, 226, 199, 220, 222, 237, 200, 247, 227, 249, 214, 235, 228, 219, 210, 212, 218, 229, 246, 210, 221, 223, 229, 206, 246, 222, 228, 215, 212, 209, 224, 213, 251, 220, 234, 205, 256, 238,
    250, 204, 228, 231, 205, 228, 233, 231, 224, 205, 243, 221, 237, 224, 222, 239, 241, 245, 225, 243, 338, 1920, 4102, 4342, 4321, 4661, 4463, 3822, 5256, 4984, 3770, 2576, 3214, 3274, 2852, 3078, 3331, 3160, 3088, 3405, 4255, 4189, 4201, 4865, 3687, 3386, 6757, 5850, 1974, 1292, 1092, 810, 717, 858, 849, 848, 787, 637, 724, 740, 850, 937, 1189, 1905, 2795, 2208, 1252, 1009, 1054, 1138, 1305, 1276, 792, 366, 239, 203, 225, 208, 219, 236, 233, 199, 201, 229, 213, 228, 222, 233, 225, 263, 241, 213, 213, 226, 232, 216, 233, 222, 220, 221, 219, 229, 234, 236, 253, 213, 247, 195, 234, 213, 224, 234, 212, 201, 233, 209, 237, 187, 231,
    244, 218, 256, 237, 235, 229, 225, 221, 219, 224, 246, 258, 202, 208, 227, 221, 232, 232, 264, 357, 2275, 4047, 4073, 3666, 3365, 2446, 1858, 2143, 2759, 2035, 1756, 2473, 2403, 1578, 1480, 2254, 3951, 3259, 2489, 2087, 3028, 4867, 4646, 4240, 5130, 5119, 7501, 7040, 2605, 1673, 1157, 934, 878, 907, 994, 966, 866, 881, 731, 676, 789, 814, 899, 1061, 1606, 2504, 2434, 1453, 971, 869, 979, 1167, 1049, 859, 425, 233, 204, 237, 254, 213, 230, 227, 205, 202, 218, 230, 234, 240, 215, 210, 219, 211, 223, 232, 224, 244, 232, 218, 199, 198, 217, 217, 245, 226, 231, 240, 231, 216, 244, 202, 235, 235, 233, 225, 216, 209, 216, 203, 238,
    205, 240, 233, 192, 230, 198, 215, 229, 236, 209, 232, 213, 239, 240, 222, 215, 252, 253, 311, 1866, 4139, 3873, 3543, 3001, 1987, 1141, 1213, 1445, 1847, 2147, 1955, 1216, 772, 629, 641, 1022, 2632, 2184, 1273, 1483, 2651, 4010, 5380, 4387, 4490, 6689, 7376, 7479, 3814, 1993, 1109, 824, 836, 994, 1090, 1167, 1151, 1009, 880, 797, 815, 816, 805, 865, 1051, 1371, 2253, 2173, 1590, 902, 881, 874, 1127, 981, 861, 425, 241, 220, 210, 255, 215, 217, 231, 230, 204, 231, 219, 206, 215, 206, 222, 229, 221, 219, 208, 228, 218, 203, 220, 232, 197, 211, 176, 196, 222, 228, 222, 217, 238, 243, 192, 206, 219, 250, 219, 249, 230, 209, 215,
    214, 245, 194, 231, 230, 203, 228, 217, 220, 211, 227, 204, 236, 212, 219, 209, 239, 274, 607, 3429, 3608, 3472, 3041, 2109, 1303, 1255, 1176, 1034, 1129, 976, 965, 767, 672, 581, 566, 535, 1044, 2135, 1026, 1446, 1894, 3081, 4243, 5570, 5343, 5351, 6383, 7349, 6609, 3057, 1420, 881, 835, 929, 1220, 1351, 1388, 1279, 1161, 1025, 940, 819, 794, 691, 872, 1076, 1109, 1642, 2034, 1847, 1196, 883, 803, 854, 921, 881, 475, 287, 227, 223, 218, 219, 234, 216, 221, 222, 219, 203, 210, 232, 231, 227, 215, 196, 249, 238, 218, 180, 211, 216, 215, 218, 225, 216, 227, 205, 232, 211, 242, 228, 249, 219, 233, 206, 250, 223, 214, 206, 225,
    226, 222, 233, 211, 238, 219, 205, 241, 229, 231, 238, 261, 204, 201, 219, 210, 263, 267, 1327, 3855, 3536, 3165, 2334, 1494, 1263, 1170, 987, 1016, 1041, 1086, 1100, 849, 619, 495, 496, 553, 508, 794, 1267, 1505, 2003, 2371, 2984, 4712, 6219, 6349, 5224, 6024, 7875, 5625, 2095, 1276, 1112, 1040, 1241, 1430, 1534, 1496, 1385, 1307, 1131, 1041, 956, 845, 757, 822, 877, 977, 1191, 1919, 1920, 1546, 897, 731, 694, 810, 869, 592, 266, 233, 220, 231, 247, 196, 226, 217, 217, 217, 229, 225, 214, 209, 216, 212, 221, 231, 230, 257, 214, 227, 204, 254, 219, 221, 214, 233, 207, 206, 215, 230, 246, 198, 226, 228, 206, 224, 211, 239, 193,
    212, 233, 232, 205, 213, 229, 204, 204, 241, 219, 222, 260, 219, 255, 240, 249, 232, 484, 2790, 3645, 3311, 2445, 1846, 1451, 885, 971, 1046, 1204, 1175, 1155, 1119, 904, 555, 571, 516, 487, 428, 482, 799, 1459, 1875, 2128, 2249, 3145, 4265, 4765, 5698, 5407, 5484, 6546, 4362, 2043, 1580, 1536, 1497, 1551, 1675, 1624, 1720, 1511, 1384, 1207, 1129, 923, 822, 772, 760, 786, 873, 1034, 1486, 1869, 1746, 1008, 680, 657, 701, 869, 745, 300, 230, 251, 198, 198, 214, 220, 242, 213, 217, 233, 215, 251, 214, 222, 235, 229, 212, 261, 205, 233, 259, 228, 224, 213, 225, 210, 206, 203, 220, 229, 230, 230, 205, 218, 234, 245, 236, 222, 232,
    240, 231, 221, 214, 222, 215, 227, 209, 222, 215, 230, 248, 207, 225, 223, 266, 299, 1102, 3437, 3128, 2462, 2168, 1445, 934, 754, 972, 1242, 1305, 1280, 1107, 1115, 1096, 728, 463, 471, 533, 458, 437, 692, 1535, 1447, 1460, 1637, 1779, 2011, 2764, 3903, 5925, 5124, 5383, 5057, 3763, 2124, 1811, 1912, 2009, 1903, 1910, 1960, 1724, 1512, 1449, 1332, 1087, 905, 690, 764, 672, 740, 827, 841, 972, 1823, 1864, 1360, 724, 633, 695, 827, 832, 343, 238, 214, 210, 231, 240, 230, 222, 223, 218, 182, 218, 215, 206, 215, 218, 241, 219, 194, 200, 218, 226, 193, 221, 216, 241, 239, 214, 212, 204, 206, 213, 214, 207, 236, 231, 196, 230, 239,
    207, 241, 217, 216, 229, 216, 216, 230, 209, 218, 228, 226, 212, 229, 218, 252, 459, 1000, 2729, 2721, 2203, 1823, 1305, 913, 700, 856, 1099, 1222, 1191, 1178, 1124, 1113, 999, 666, 464, 463, 503, 474, 503, 859, 1349, 1408, 1389, 1576, 1451, 1539, 2246, 3507, 5175, 5337, 5357, 4724, 4494, 3830, 2380, 2346, 2461, 2423, 2390, 2304, 2005, 1812, 1550, 1274, 1154, 1009, 747, 670, 637, 658, 729, 757, 844, 1067, 1956, 1806, 1185, 683, 618, 744, 941, 524, 270, 222, 232, 217, 226, 223, 207, 226, 222, 239, 205, 206, 183, 200, 225, 243, 227, 209, 220, 221, 217, 196, 208, 208, 222, 232, 225, 194, 231, 198, 212, 229, 224, 204, 214, 214, 216,
    208, 238, 205, 216, 229, 229, 250, 216, 203, 215, 219, 221, 223, 235, 278, 506, 804, 1751, 2203, 1928, 1423, 957, 767, 695, 690, 943, 992, 1217, 1321, 1217, 1062, 938, 717, 423, 439, 447, 443, 448, 590, 777, 1252, 1447, 1441, 1645, 2065, 2191, 2197, 2536, 3962, 5049, 4674, 4839, 3109, 4561, 4011, 2558, 2495, 2655, 2722, 2714, 2055, 1788, 1680, 1566, 1282, 1043, 937, 874, 772, 693, 672, 672, 737, 816, 991, 1886, 1764, 1290, 759, 688, 818, 954, 387, 257, 235, 209, 226, 215, 228, 236, 223, 237, 231, 227, 222, 214, 222, 219, 228, 203, 211, 224, 208, 212, 241, 205, 221, 214, 226, 216, 216, 237, 212, 241, 219, 233, 206, 205, 222,
    207, 218, 236, 219, 202, 218, 229, 226, 230, 235, 240, 229, 208, 260, 309, 564, 722, 1837, 1892, 1304, 911, 627, 557, 533, 564, 785, 1063, 1204, 1413, 1370, 1113, 766, 576, 497, 432, 434, 474, 460, 471, 846, 988, 1552, 1495, 1616, 2314, 2786, 2771, 2577, 2982, 3835, 4552, 4702, 4577, 2866, 3666, 4750, 3103, 2637, 2688, 2665, 2679, 1911, 1742, 1610, 1509, 1468, 1128, 1050, 940, 859, 651, 677, 696, 703, 764, 969, 1613, 2091, 1659, 909, 739, 848, 915, 417, 256, 249, 228, 225, 236, 224, 219, 235, 195, 197, 229, 197, 217, 218, 260, 234, 227, 191, 209, 238, 209, 218, 201, 229, 222, 242, 218, 236, 213, 207, 241, 227, 217, 216, 219,
    226, 222, 219, 206, 216, 235, 219, 209, 242, 213, 244, 222, 228, 345, 559, 423, 823, 1780, 1275, 825, 600, 516, 488, 476, 518, 583, 843, 1025, 1149, 1156, 862, 639, 586, 606, 499, 444, 459, 492, 437, 557, 952, 1557, 1919, 2098, 2626, 2877, 3020, 3046, 3027, 2627, 3097, 4402, 5255, 5234, 3024, 2741, 4533, 3417, 2694, 2810, 2700, 2837, 2058, 1720, 1638, 1477, 1379, 1281, 1208, 1023, 828, 738, 760, 661, 709, 754, 975, 1364, 2311, 1795, 1000, 721, 830, 919, 458, 250, 225, 210, 214, 243, 197, 218, 235, 203, 208, 247, 223, 238, 229, 214, 219, 187, 228, 220, 202, 231, 209, 207, 231, 245, 241, 208, 212, 233, 252, 198, 236, 193, 219,
    216, 223, 243, 222, 202, 229, 227, 196, 245, 214, 233, 214, 337, 520, 450, 665, 1406, 1037, 776, 599, 508, 414, 494, 473, 485, 481, 559, 693, 684, 602, 535, 503, 617, 684, 614, 568, 569, 491, 511, 660, 913, 1789, 2085, 2470, 2489, 2277, 2277, 2441, 2331, 2544, 2714, 4415, 5151, 5442, 4120, 2383, 3194, 4160, 2965, 2646, 2579, 2817, 2480, 1828, 1559, 1591, 1584, 1618, 1555, 1378, 1258, 1012, 832, 671, 680, 734, 808, 1008, 1838, 2226, 1481, 947, 847, 868, 621, 275, 220, 237, 225, 211, 235, 239, 216, 216, 199, 211, 204, 214, 222, 219, 207, 213, 227, 221, 208, 249, 238, 233, 252, 225, 224, 229, 208, 214, 221, 199, 213, 219, 236,
    222, 237, 233, 226, 227, 227, 252, 203, 217, 255, 237, 251, 296, 393, 393, 677, 1226, 792, 688, 529, 465, 438, 490, 450, 478, 423, 439, 558, 564, 617, 553, 557, 687, 761, 822, 741, 603, 493, 580, 792, 1176, 1471, 1956, 1969, 2107, 1932, 1969, 2366, 3087, 3446, 3161, 3204, 4924, 5672, 5942, 4792, 2561, 3265, 4252, 2843, 2652, 2307, 2776, 2565, 1877, 1685, 1696, 1827, 2143, 1866, 1920, 1529, 1138, 865, 706, 658, 638, 845, 1029, 1716, 2352, 1584, 982, 871, 929, 475, 243, 253, 245, 247, 200, 248, 228, 205, 213, 239, 204, 203, 205, 217, 249, 221, 230, 209, 242, 207, 228, 220, 239, 187, 229, 229, 206, 247, 220, 226, 264, 226, 214,
    230, 199, 229, 208, 225, 234, 229, 250, 253, 213, 203, 263, 293, 260, 266, 815, 1068, 854, 635, 507, 477, 457, 500, 477, 475, 496, 469, 556, 552, 575, 591, 494, 622, 733, 869, 842, 741, 590, 702, 991, 1077, 1553, 2198, 2048, 2128, 2465, 2823, 2766, 3070, 3221, 3215, 2867, 3296, 5082, 5750, 6087, 5326, 3462, 3411, 4488, 3072, 2564, 2228, 2742, 2485, 1874, 1684, 1819, 2097, 2626, 1987, 2273, 1781, 1162, 843, 638, 617, 641, 705, 836, 1431, 2274, 1576, 945, 850, 926, 396, 241, 235, 211, 254, 196, 214, 248, 202, 230, 216, 213, 207, 207, 233, 196, 184, 234, 202, 206, 206, 219, 215, 222, 228, 237, 217, 200, 210, 206, 220, 224, 222,
    210, 234, 233, 231, 253, 210, 211, 216, 242, 247, 208, 275, 299, 234, 357, 1075, 904, 744, 610, 503, 476, 459, 497, 488, 471, 424, 492, 545, 530, 500, 593, 560, 522, 521, 715, 870, 737, 682, 801, 1083, 1085, 1575, 2453, 2550, 3059, 3167, 2805, 2771, 2660, 2149, 1950, 2081, 2517, 2989, 4574, 5026, 5962, 4770, 3650, 3750, 4396, 2822, 2313, 2394, 2856, 2261, 1869, 1695, 1744, 1970, 2450, 1858, 2038, 1542, 997, 646, 627, 625, 549, 703, 845, 1276, 2169, 1396, 1059, 931, 880, 314, 210, 211, 196, 214, 230, 205, 229, 210, 250, 252, 237, 229, 196, 223, 197, 230, 229, 226, 221, 211, 220, 209, 230, 200, 206, 230, 207, 195, 217, 238, 200,
    204, 218, 239, 221, 252, 216, 208, 242, 203, 202, 209, 264, 251, 238, 729, 1037, 796, 685, 610, 517, 485, 501, 500, 497, 473, 409, 409, 445, 466, 477, 443, 490, 477, 491, 565, 727, 753, 757, 974, 1039, 1244, 1838, 2493, 3311, 3252, 2683, 2753, 2402, 2123, 1982, 1958, 2272, 2878, 2940, 3473, 4551, 4888, 4839, 4787, 3268, 4275, 3976, 2579, 2183, 2619, 2699, 1990, 1714, 1668, 1618, 1834, 2067, 1589, 1809, 1421, 844, 606, 506, 548, 643, 695, 834, 1372, 2084, 1289, 1170, 964, 528, 289, 228, 224, 213, 249, 207, 199, 223, 192, 219, 214, 203, 234, 223, 234, 241, 230, 207, 223, 241, 244, 217, 234, 220, 203, 228, 229, 227, 224, 224, 201,
    217, 214, 217, 220, 247, 212, 205, 241, 235, 218, 214, 297, 287, 251, 423, 1004, 870, 756, 711, 581, 490, 451, 479, 514, 484, 541, 522, 422, 456, 493, 430, 461, 412, 460, 507, 504, 599, 760, 974, 986, 1105, 1584, 3054, 3985, 3232, 3362, 1984, 1427, 1502, 1709, 1972, 1976, 1942, 1878, 2560, 3049, 3880, 4216, 3515, 4412, 3064, 3521, 4554, 3062, 2387, 2699, 2861, 1859, 1566, 1483, 1316, 1252, 1618, 1601, 1239, 1755, 941, 582, 559, 597, 676, 729, 848, 1104, 2020, 1702, 1201, 1012, 726, 310, 234, 247, 223, 213, 223, 204, 223, 221, 209, 201, 210, 208, 202, 224, 203, 191, 239, 240, 232, 201, 213, 211, 223, 224, 240, 229, 230, 197, 246,
    229, 226, 210, 209, 210, 246, 213, 211, 246, 194, 260, 274, 242, 284, 940, 871, 737, 670, 598, 534, 514, 515, 479, 479, 547, 544, 521, 486, 555, 514, 494, 468, 552, 585, 547, 587, 661, 1034, 1130, 1010, 1151, 2784, 4809, 3514, 2959, 1925, 2142, 2600, 2583, 2605, 2367, 2500, 2796, 2104, 1517, 1933, 2578, 2609, 3404, 3134, 2639, 3031, 4637, 3268, 2263, 2697, 2436, 1567, 1372, 1245, 1054, 1035, 1209, 1742, 1198, 1421, 1526, 802, 686, 623, 657, 727, 819, 944, 1743, 1988, 1349, 1017, 780, 288, 229, 201, 251, 235, 222, 200, 247, 235, 217, 223, 217, 215, 225, 210, 203, 213, 209, 217, 221, 224, 212, 190, 237, 231, 202, 224, 205, 223, 234,
    229, 215, 234, 232, 224, 213, 220, 228, 225, 214, 254, 230, 232, 491, 1004, 839, 693, 622, 615, 560, 532, 552, 555, 546, 532, 580, 549, 549, 569, 585, 592, 544, 593, 727, 637, 707, 866, 1179, 1329, 1048, 1125, 3094, 4956, 4631, 4141, 2946, 1990, 1628, 1626, 1735, 1626, 1632, 1847, 2471, 1526, 1122, 1707, 2615, 3261, 2737, 2672, 2120, 3447, 4503, 2815, 2595, 2755, 1729, 1325, 1195, 1119, 1177, 1132, 1249, 1849, 1154, 1467, 1697, 920, 746, 673, 609, 686, 759, 926, 1755, 2218, 1300, 974, 666, 257, 230, 216, 217, 249, 216, 211, 221, 221, 233, 236, 221, 212, 193, 221, 217, 235, 208, 224, 217, 202, 222, 207, 231, 218, 238, 213, 216, 195,
    205, 225, 220, 235, 249, 192, 197, 255, 233, 189, 292, 258, 303, 978, 881, 807, 702, 646, 607, 664, 560, 628, 585, 615, 625, 655, 681, 679, 709, 708, 630, 602, 588, 643, 646, 853, 1203, 1397, 1216, 1000, 1657, 4989, 6273, 3374, 1905, 1548, 1392, 1201, 1079, 885, 802, 855, 1025, 1845, 2307, 1003, 1590, 2845, 3643, 2330, 2950, 1724, 2525, 4314, 2923, 2252, 2553, 1800, 1420, 1282, 1196, 1200, 1245, 1302, 1873, 1739, 1228, 1938, 1400, 784, 611, 605, 594, 632, 761, 1116, 2242, 1690, 961, 764, 347, 202, 218, 218, 215, 236, 227, 203, 233, 204, 205, 205, 235, 222, 209, 199, 204, 219, 203, 232, 241, 244, 212, 210, 219, 200, 234, 209, 218,
    213, 221, 236, 212, 189, 219, 221, 223, 222, 212, 251, 263, 417, 1038, 879, 855, 716, 645, 665, 715, 673, 724, 646, 681, 697, 745, 816, 787, 800, 826, 790, 764, 724, 730, 764, 833, 1188, 1416, 1302, 1253, 3056, 4154, 3588, 1802, 913, 763, 823, 897, 740, 526, 557, 560, 509, 892, 2070, 1849, 1378, 1991, 3485, 2827, 2719, 1616, 1864, 3178, 3663, 2294, 2284, 2190, 1602, 1433, 1394, 1348, 1321, 1293, 1435, 1784, 1543, 1257, 1880, 1182, 698, 637, 614, 579, 648, 738, 1231, 2202, 1340, 879, 586, 259, 214, 225, 211, 204, 209, 217, 208, 201, 204, 231, 236, 193, 194, 229, 209, 217, 218, 214, 205, 221, 204, 206, 241, 213, 233, 214, 195,
    216, 177, 216, 226, 231, 198, 237, 210, 203, 232, 252, 437, 1066, 984, 874, 819, 796, 775, 704, 720, 684, 678, 675, 716, 780, 882, 1037, 1166, 1061, 956, 834, 852, 796, 714, 813, 964, 1271, 1342, 1308, 3308, 3089, 2795, 2717, 940, 649, 673, 710, 622, 545, 696, 1356, 1595, 1067, 893, 1902, 2049, 1837, 1793, 2282, 3222, 1904, 1288, 1419, 2752, 3880, 2383, 2177, 1988, 1736, 1604, 1570, 1655, 1401, 1297, 1394, 1480, 1790, 1206, 1528, 1585, 749, 699, 599, 568, 558, 627, 852, 1793, 1497, 831, 689, 338, 210, 230, 234, 199, 224, 225, 223, 228, 209, 235, 201, 243, 192, 231, 222, 210, 217, 223, 240, 228, 233, 237, 204, 221, 221, 227, 209,
    228, 224, 229, 204, 228, 236, 219, 212, 226, 264, 283, 838, 1252, 1050, 963, 952, 1030, 1064, 982, 715, 703, 660, 699, 750, 881, 1301, 1709, 1585, 1462, 1267, 1143, 1148, 1115, 942, 919, 983, 1109, 1075, 1597, 3990, 1878, 2751, 2907, 1155, 954, 1038, 965, 1129, 1086, 999, 1267, 1347, 1869, 1553, 1568, 2532, 1893, 1371, 1804, 2999, 2191, 1424, 1269, 2102, 4319, 2880, 2163, 2065, 1897, 1639, 1674, 1543, 1420, 1352, 1311, 1252, 1520, 1517, 1166, 1903, 1266, 825, 674, 570, 494, 501, 641, 944, 1860, 1148, 755, 579, 280, 208, 226, 217, 226, 236, 192, 221, 216, 232, 201, 234, 208, 208, 232, 237, 187, 205, 237, 252, 218, 235, 226, 195, 215, 208, 211,
    236, 230, 225, 222, 204, 227, 196, 223, 215, 236, 322, 1380, 1748, 1498, 1251, 1366, 2209, 2589, 2143, 1253, 706, 705, 683, 869, 1266, 1945, 2237, 1941, 1666, 1512, 1319, 1259, 1144, 1095, 1120, 1098, 955, 903, 1813, 3516, 1637, 2592, 3963, 2050, 1636, 1524, 1335, 1115, 1023, 989, 1121, 1202, 1394, 1827, 1389, 2502, 1957, 1924, 2067, 1716, 2558, 2011, 1675, 1669, 3108, 4503, 2474, 2130, 2018, 1812, 1644, 1497, 1502, 1277, 1311, 1298, 1267, 1506, 1601, 1416, 1955, 1277, 995, 795, 657, 535, 556, 641, 1063, 1805, 905, 716, 414, 263, 216, 217, 223, 228, 222, 216, 236, 221, 203, 229, 206, 198, 226, 207, 218, 226, 234, 216, 195, 227, 225, 220, 219, 204, 209,
    221, 255, 218, 226, 236, 210, 235, 209, 196, 237, 352, 1288, 1373, 928, 633, 559, 934, 1985, 1672, 1543, 1224, 798, 824, 1079, 1878, 2720, 2780, 2169, 1917, 2156, 2103, 1980, 1558, 1402, 1253, 1168, 1089, 963, 1975, 3143, 1720, 2017, 4870, 3508, 1916, 1379, 1301, 1142, 1084, 918, 958, 1111, 1256, 1492, 1393, 2157, 3115, 2908, 1222, 703, 1779, 2203, 1991, 1868, 2574, 4668, 3746, 2452, 2246, 1942, 1829, 1510, 1438, 1356, 1372, 1427, 1215, 1284, 1547, 1657, 1981, 2400, 1766, 1442, 1195, 779, 634, 651, 754, 1554, 1478, 730, 658, 315, 252, 219, 195, 204, 205, 197, 223, 213, 229, 197, 190, 194, 240, 202, 255, 230, 224, 229, 230, 221, 236, 206, 202, 211, 207,
    215, 208, 226, 216, 222, 229, 208, 230, 213, 224, 250, 433, 338, 259, 267, 291, 649, 2525, 1419, 1185, 1225, 1146, 913, 1449, 2915, 3547, 3409, 3730, 3637, 2329, 1649, 1855, 1935, 2088, 2306, 2458, 2358, 1960, 2881, 3031, 2678, 2718, 3862, 4795, 2467, 1421, 1199, 1244, 1327, 1074, 1155, 1199, 1458, 1907, 1903, 2740, 3721, 1584, 786, 612, 1192, 1997, 1786, 1746, 2269, 4140, 4214, 3105, 2854, 2515, 2120, 1865, 1588, 1582, 1526, 1571, 1593, 1524, 1612, 1828, 2235, 2468, 2593, 2594, 2302, 1515, 787, 705, 785, 1209, 1546, 801, 735, 482, 223, 251, 204, 245, 219, 243, 226, 213, 211, 222, 231, 220, 199, 213, 226, 216, 210, 220, 210, 215, 231, 203, 233, 214, 241,
    207, 188, 211, 222, 224, 218, 210, 194, 211, 202, 225, 289, 236, 253, 218, 233, 1139, 2871, 1595, 1128, 1018, 1294, 1484, 2135, 4496, 6025, 4774, 4392, 3098, 2456, 2345, 2255, 2168, 2290, 2450, 2474, 2790, 2917, 3549, 4803, 5838, 4569, 3927, 3821, 2823, 2121, 1902, 1742, 1806, 1685, 1707, 1845, 2340, 3117, 2686, 2078, 2837, 1057, 619, 420, 638, 2019, 1747, 1544, 1750, 3106, 4248, 3303, 3194, 3154, 2825, 2277, 2066, 1952, 1811, 1987, 1999, 1677, 1696, 1848, 1853, 1960, 2114, 2483, 2943, 2705, 1764, 1061, 908, 1082, 1537, 1163, 649, 679, 358, 235, 244, 233, 239, 206, 208, 215, 215, 196, 213, 232, 208, 223, 233, 216, 212, 228, 210, 195, 223, 232, 225, 205, 228,
    221, 229, 246, 219, 225, 229, 203, 203, 197, 201, 203, 209, 277, 234, 239, 248, 975, 2242, 2729, 2188, 1595, 1572, 2509, 3981, 4778, 4213, 3530, 2412, 2033, 2055, 1924, 1862, 1807, 1894, 2212, 2416, 2525, 2441, 2294, 3710, 6523, 7018, 6481, 5525, 3551, 2489, 2142, 1942, 2121, 2063, 1852, 1877, 2157, 2226, 2020, 1777, 2370, 902, 515, 465, 525, 1289, 2873, 1882, 1438, 1855, 3844, 4041, 3723, 3204, 3397, 2863, 2422, 2284, 2372, 2245, 2150, 1907, 1941, 1509, 1490, 1555, 1669, 1871, 2375, 2437, 2373, 2186, 1345, 1075, 1247, 1580, 1088, 704, 665, 409, 242, 227, 227, 205, 193, 223, 214, 231, 205, 192, 226, 218, 198, 226, 226, 241, 190, 220, 246, 185, 221, 212, 217,
    224, 219, 187, 215, 202, 238, 199, 214, 265, 219, 209, 230, 253, 277, 275, 267, 407, 767, 627, 503, 1054, 2559, 3336, 2960, 2828, 2437, 1849, 1582, 1497, 1462, 1769, 2961, 4571, 5120, 4315, 3377, 3079, 2835, 3185, 4327, 7108, 6402, 5888, 5130, 4557, 4256, 3686, 2941, 2840, 2442, 1849, 1896, 2178, 2397, 2654, 2620, 1337, 857, 820, 987, 1305, 1739, 2370, 3422, 2339, 2383, 3467, 5720, 5340, 3559, 3305, 3545, 2859, 2549, 2417, 2226, 2137, 1936, 1686, 1462, 1540, 1467, 1270, 1561, 1804, 1934, 1983, 1983, 1813, 1404, 1356, 1696, 1572, 858, 631, 640, 329, 224, 225, 190, 228, 195, 193, 223, 193, 219, 217, 242, 214, 225, 232, 206, 212, 226, 180, 194, 229, 214, 192,
    211, 230, 235, 238, 228, 213, 198, 241, 229, 208, 208, 233, 227, 220, 236, 238, 247, 314, 545, 1817, 2891, 2454, 1997, 1751, 1519, 1296, 1145, 1437, 2387, 4185, 4736, 3841, 2757, 2362, 2144, 1857, 1699, 1598, 1643, 3083, 5853, 5569, 5554, 5012, 3951, 3473, 3471, 3618, 3433, 3261, 3307, 3543, 4070, 4977, 3335, 2798, 2950, 2959, 2723, 2575, 2667, 2843, 3204, 3848, 4277, 3498, 3563, 4559, 4808, 3625, 3329, 3649, 2887, 2397, 2230, 2103, 1917, 1727, 1526, 1431, 1424, 1271, 1284, 1280, 1467, 1658, 1652, 1569, 1639, 1396, 1274, 1610, 1687, 984, 670, 685, 405, 247, 181, 196, 232, 214, 240, 208, 185, 223, 222, 214, 238, 201, 232, 222, 196, 208, 209, 198, 244, 226, 204,
    231, 247, 212, 227, 230, 229, 187, 227, 229, 231, 224, 242, 209, 256, 214, 240, 291, 383, 1502, 2816, 2231, 1766, 1497, 1174, 1143, 1258, 1711, 3424, 4380, 3914, 3003, 2309, 1937, 1806, 1709, 1588, 1473, 1398, 1403, 1651, 3705, 4939, 4803, 3907, 3888, 3225, 2552, 2715, 2735, 2649, 2633, 2808, 3316, 3492, 1945, 1520, 1509, 1734, 1723, 1671, 1651, 1760, 1848, 2042, 2312, 2998, 3127, 3017, 4019, 3997, 3755, 3867, 4107, 2958, 2247, 2105, 1962, 1732, 1543, 1435, 1379, 1233, 1222, 1211, 1282, 1467, 1520, 1537, 1595, 1233, 1124, 1225, 1519, 1247, 798, 688, 761, 324, 213, 210, 206, 177, 225, 216, 199, 213, 218, 221, 219, 199, 232, 206, 223, 239, 207, 232, 212, 205, 213,
    227, 223, 229, 221, 219, 216, 218, 209, 230, 200, 232, 211, 213, 206, 238, 219, 365, 1456, 2888, 2261, 1764, 1337, 1094, 1137, 1430, 2320, 3658, 3622, 2751, 2425, 2116, 2003, 1754, 1587, 1674, 1567, 1470, 1402, 1314, 1467, 3151, 5305, 5248, 3957, 3316, 2852, 2380, 2334, 2415, 2556, 2781, 2848, 3458, 2393, 1281, 1153, 1244, 1566, 1869, 2113, 2000, 1612, 1447, 1476, 1581, 1904, 2802, 3343, 3672, 3876, 3899, 4206, 4848, 3861, 2578, 2010, 1799, 1653, 1509, 1321, 1367, 1347, 1343, 1237, 1201, 1176, 1210, 1516, 1847, 1398, 1018, 1034, 1349, 1343, 888, 719, 728, 549, 255, 194, 218, 210, 209, 229, 217, 200, 216, 254, 221, 222, 220, 211, 246, 210, 230, 214, 221, 228, 213,
    211, 214, 222, 224, 239, 241, 211, 201, 209, 215, 212, 218, 218, 231, 222, 330, 1429, 2884, 2193, 1499, 1142, 1096, 1274, 1510, 2766, 3224, 3109, 2477, 2066, 1951, 1866, 1685, 1558, 1607, 1646, 1698, 1559, 1533, 1543, 1926, 3963, 4471, 4848, 5008, 4188, 2957, 2665, 2784, 2628, 2588, 2576, 3064, 3635, 2423, 2219, 2348, 2382, 2454, 2813, 3086, 3104, 3080, 3014, 2628, 2069, 1952, 2825, 3985, 3752, 2837, 3172, 4240, 4175, 2977, 2517, 2180, 1721, 1600, 1305, 1237, 1192, 1199, 1315, 1271, 1098, 1100, 1100, 1297, 1680, 1680, 1194, 939, 1106, 1125, 843, 716, 739, 762, 308, 226, 209, 209, 220, 234, 209, 210, 191, 229, 201, 233, 206, 217, 220, 215, 250, 236, 221, 207, 215,
    214, 232, 209, 201, 222, 176, 251, 189, 212, 232, 189, 230, 211, 256, 295, 1342, 2825, 2070, 1471, 1116, 1183, 1373, 1681, 2622, 3181, 2615, 2202, 2022, 1828, 1826, 1928, 1811, 1588, 1662, 1901, 1905, 1657, 1994, 1987, 2912, 4157, 5007, 5041, 5083, 4928, 3501, 2562, 2562, 2856, 3012, 3461, 4081, 3846, 3479, 3159, 3055, 2710, 2766, 3174, 3358, 3718, 3474, 3506, 3378, 3244, 3122, 3553, 4331, 3867, 2677, 2937, 2955, 2978, 2009, 1713, 2073, 1700, 1396, 1197, 1053, 1088, 1042, 1045, 1213, 1111, 1028, 1029, 1125, 1429, 1700, 1369, 945, 1011, 1018, 755, 704, 637, 736, 445, 234, 224, 187, 218, 226, 209, 225, 210, 207, 196, 231, 211, 210, 205, 206, 219, 211, 197, 220, 239,
    208, 238, 200, 226, 220, 220, 225, 204, 224, 227, 236, 228, 222, 253, 1039, 2862, 2203, 1397, 1054, 1124, 1318, 1630, 2583, 2865, 2391, 2194, 1904, 1871, 1863, 1916, 1912, 1824, 1783, 1891, 1976, 2013, 2061, 2183, 2059, 4039, 6282, 7167, 7812, 7000, 5615, 5040, 3924, 3944, 4756, 4789, 4641, 4337, 3284, 2817, 2622, 2653, 2392, 2552, 2750, 2854, 3157, 3456, 3459, 3447, 3576, 4200, 4210, 3156, 3122, 3303, 2698, 1801, 2057, 2094, 1547, 1433, 1808, 1646, 1225, 1051, 992, 894, 951, 1053, 998, 1027, 961, 1077, 1229, 1587, 1665, 1046, 958, 929, 723, 680, 634, 687, 627, 263, 233, 191, 190, 209, 194, 212, 224, 203, 242, 220, 194, 220, 230, 212, 222, 214, 240, 206, 214,
    215, 209, 229, 217, 213, 212, 195, 223, 222, 213, 219, 240, 230, 920, 2820, 2048, 1358, 1015, 1064, 1346, 1657, 2500, 2784, 2334, 2127, 2197, 2016, 1820, 2013, 2034, 1872, 1799, 1875, 2099, 2081, 2154, 2341, 2268, 2737, 5447, 7007, 8974, 10475, 9249, 7819, 7125, 5101, 4361, 4174, 4414, 4385, 3568, 2856, 2733, 2792, 2629, 2471, 2574, 2615, 2744, 3238, 3637, 3802, 4674, 5449, 4875, 3840, 3793, 3896, 2865, 1699, 1685, 1813, 1916, 1609, 1416, 1520, 1665, 1292, 940, 826, 731, 763, 763, 844, 926, 955, 1040, 1313, 1526, 1532, 1253, 1034, 854, 689, 623, 591, 583, 644, 278, 220, 194, 201, 230, 232, 247, 214, 247, 189, 227, 220, 209, 225, 210, 212, 216, 219, 189, 199,
    233, 243, 224, 189, 220, 211, 219, 226, 214, 254, 247, 226, 390, 2179, 2608, 1604, 1024, 1003, 1250, 1570, 2038, 3064, 2520, 2192, 2261, 2132, 1832, 1682, 1765, 2064, 1840, 1766, 2112, 2353, 2358, 2299, 2308, 2081, 2769, 5329, 8081, 10706, 11995, 9758, 7566, 6361, 5872, 4401, 4197, 4470, 4642, 3468, 3276, 2969, 2618, 2446, 2393, 2504, 2458, 2528, 3143, 3885, 5863, 5775, 4395, 4154, 4666, 4512, 2764, 1632, 1483, 1476, 1716, 1628, 1663, 1570, 1294, 1284, 1467, 1065, 692, 654, 653, 653, 680, 809, 922, 1036, 1171, 1573, 1629, 1476, 1124, 803, 614, 525, 584, 570, 558, 491, 248, 230, 209, 190, 197, 207, 237, 222, 207, 221, 243, 222, 216, 209, 208, 206, 207, 201, 238,
    201, 230, 215, 222, 232, 251, 221, 227, 209, 224, 239, 262, 1209, 2899, 1982, 1221, 952, 1084, 1450, 1732, 2552, 2701, 2606, 2465, 2231, 1926, 1771, 1709, 1749, 2002, 1920, 1845, 2149, 2367, 2519, 2173, 2175, 1945, 2650, 4952, 8567, 9612, 9232, 8567, 8355, 7820, 6448, 4325, 4201, 4523, 4379, 3517, 3066, 3069, 3017, 2863, 2926, 2738, 2671, 2904, 3849, 5086, 5004, 3837, 4095, 4537, 3463, 2147, 1602, 1450, 1375, 1366, 1477, 1472, 1430, 1677, 1425, 1122, 1293, 1504, 983, 937, 786, 690, 700, 805, 793, 932, 1005, 1157, 1582, 1689, 1354, 893, 646, 598, 615, 583, 488, 550, 382, 192, 207, 223, 202, 216, 237, 218, 210, 197, 195, 223, 228, 205, 232, 197, 221, 216, 203,
    235, 200, 227, 223, 230, 224, 231, 200, 223, 249, 208, 478, 2453, 2327, 1381, 983, 966, 1294, 1637, 2230, 2623, 2863, 2773, 2261, 1863, 1985, 1948, 1855, 1745, 2178, 2042, 1976, 2227, 2525, 2294, 2167, 1911, 1965, 2136, 3687, 7755, 8570, 8605, 8276, 8086, 7491, 6602, 4352, 4185, 4837, 4350, 3365, 3278, 3206, 3175, 3269, 3384, 3480, 4052, 4959, 4103, 3385, 3128, 3552, 3005, 1923, 1567, 1423, 1448, 1398, 1388, 1461, 1513, 1568, 1529, 1511, 1556, 1495, 1223, 1265, 1513, 1275, 1094, 964, 959, 848, 772, 712, 890, 1031, 1192, 1870, 1616, 1019, 686, 620, 619, 557, 470, 534, 593, 292, 234, 221, 244, 254, 203, 231, 189, 203, 232, 226, 214, 212, 219, 199, 207, 212, 207,
    217, 234, 230, 226, 224, 198, 234, 230, 228, 213, 263, 1272, 2917, 1935, 1226, 961, 1025, 1352, 1780, 2410, 2481, 2678, 2541, 2289, 2016, 2006, 2282, 2024, 1766, 2022, 1969, 2179, 2228, 2197, 2113, 2166, 1964, 1816, 1775, 2696, 5832, 8019, 7775, 7182, 7164, 8276, 7058, 4853, 4256, 4437, 3581, 3239, 3222, 3466, 3827, 4530, 5237, 5035, 4478, 3788, 3322, 3224, 2792, 1991, 1641, 1534, 1447, 1409, 1352, 1383, 1617, 1960, 1571, 1404, 1361, 1352, 1319, 1376, 1440, 1273, 1338, 1444, 1154, 1169, 1113, 1056, 975, 954, 927, 1169, 1287, 2087, 1989, 1105, 753, 650, 616, 509, 497, 527, 626, 427, 248, 218, 215, 211, 204, 245, 186, 198, 211, 219, 222, 231, 194, 201, 184, 202, 209,
    214, 205, 209, 215, 218, 233, 228, 205, 224, 225, 432, 2515, 2403, 1534, 1070, 1080, 1222, 1447, 2053, 2410, 2422, 2773, 2457, 2265, 2323, 2116, 2188, 1855, 1668, 1839, 2125, 2063, 2146, 2130, 1988, 1983, 1966, 1876, 1676, 2164, 3808, 7118, 7067, 6124, 6986, 8709, 7209, 6116, 5498, 5180, 4331, 4604, 5402, 6022, 5619, 4639, 4171, 3835, 3528, 2893, 1953, 1729, 1675, 1732, 1486, 1505, 1416, 1472, 1359, 1396, 1428, 1490, 1491, 1491, 1347, 1416, 1229, 1308, 1345, 1227, 1121, 1146, 1172, 1125, 1277, 1190, 1243, 1207, 1183, 1335, 1509, 1857, 2565, 1792, 932, 752, 643, 530, 505, 509, 569, 637, 333, 204, 198, 234, 218, 212, 197, 217, 208, 221, 198, 234, 210, 242, 205, 209, 207,
    206, 245, 227, 231, 220, 213, 188, 228, 225, 284, 1346, 2971, 1908, 1196, 1092, 1187, 1338, 1680, 2365, 2352, 2644, 2665, 2481, 2428, 1982, 1964, 1918, 1781, 1689, 1814, 2164, 2048, 2105, 2163, 2208, 2025, 1856, 1908, 1790, 1554, 2881, 5544, 8515, 8861, 8717, 8855, 8270, 8172, 8366, 9140, 7522, 5985, 5397, 4993, 4533, 3817, 2688, 1822, 1430, 1294, 1216, 1250, 1406, 1729, 1827, 1484, 1337, 1389, 1451, 1284, 1397, 1521, 1444, 1413, 1452, 1418, 1238, 1273, 1307, 1171, 1235, 1123, 1044, 999, 970, 1072, 1221, 1246, 1260, 1271, 1736, 1945, 2726, 2614, 1462, 824, 651, 538, 554, 516, 530, 732, 506, 223, 267, 196, 218, 225, 197, 222, 232, 222, 210, 212, 207, 218, 215, 218, 206,
    216, 190, 223, 213, 221, 190, 210, 237, 235, 821, 2985, 2268, 1351, 1062, 1180, 1367, 1646, 1968, 2554, 2678, 3053, 2815, 2488, 2050, 1915, 1861, 1888, 1689, 1699, 1840, 2228, 2173, 2317, 2319, 2121, 2159, 2045, 1837, 1632, 1705, 2294, 4278, 7660, 10936, 10220, 9090, 9282, 8211, 7292, 6240, 3900, 2891, 2397, 2112, 1887, 1625, 1453, 1261, 1212, 1122, 1086, 1178, 1506, 1490, 1569, 1379, 1349, 1346, 1317, 1233, 1354, 1522, 1454, 1587, 1635, 1411, 1464, 1338, 1252, 1210, 1148, 1007, 846, 920, 909, 968, 1121, 1076, 1044, 1455, 1865, 1952, 2777, 2257, 1401, 664, 553, 534, 534, 508, 557, 674, 292, 201, 217, 188, 228, 197, 218, 218, 199, 240, 232, 231, 196, 198, 220, 233, 224,
    212, 201, 218, 194, 225, 239, 222, 227, 225, 983, 3085, 2177, 1292, 1091, 1236, 1477, 1594, 1995, 2765, 2772, 3034, 2820, 2376, 2084, 2004, 1870, 1982, 1921, 1726, 1759, 1974, 2147, 2191, 2240, 2143, 2111, 1932, 1859, 1856, 1657, 1922, 2477, 2860, 3021, 3477, 3573, 3672, 3672, 3690, 4498, 2533, 1713, 1600, 1359, 1356, 1432, 1302, 1110, 1090, 1033, 989, 1146, 1389, 1381, 1489, 1555, 1403, 1400, 1229, 1165, 1158, 1498, 1539, 1458, 1621, 1375, 1523, 1475, 1265, 1269, 1158, 1085, 892, 866, 882, 862, 906, 908, 1006, 1450, 1824, 1758, 2145, 2117, 1369, 829, 582, 501, 540, 532, 552, 445, 262, 200, 251, 210, 211, 184, 211, 191, 210, 198, 229, 229, 209, 220, 241, 231, 213,
    234, 223, 190, 195, 233, 204, 224, 221, 804, 2985, 2262, 1421, 1090, 1191, 1549, 1776, 1959, 2713, 2706, 2844, 2648, 2239, 2173, 2104, 2069, 1827, 1635, 1686, 1627, 1655, 2055, 2037, 2009, 2218, 1938, 1979, 1891, 1670, 1512, 2152, 2821, 2804, 2568, 2434, 2202, 2466, 2692, 3059, 4047, 2339, 1541, 1518, 1282, 1140, 1247, 1225, 1156, 1038, 1005, 950, 1163, 1246, 1382, 1389, 1406, 1424, 1274, 1170, 1198, 1403, 1426, 1377, 1423, 1387, 1408, 1542, 1287, 1187, 1058, 1118, 1165, 956, 862, 885, 899, 955, 1072, 1238, 1437, 1618, 1629, 1666, 1512, 1144, 785, 592, 534, 541, 480, 530, 383, 228, 230, 202, 219, 204, 231, 218, 188, 216, 205, 222, 222, 217, 177, 216, 226, 197, 207,
    195, 209, 220, 202, 217, 222, 241, 240, 482, 2780, 2431, 1643, 1207, 1186, 1577, 1768, 1807, 2428, 2754, 2766, 2715, 2321, 2181, 1970, 2042, 1916, 1595, 1669, 1591, 1551, 1405, 1618, 1875, 1852, 2007, 1949, 1903, 1891, 1944, 1992, 2800, 3155, 3010, 2675, 2640, 2296, 2265, 2532, 2840, 3910, 2440, 1669, 1350, 1218, 1220, 1107, 1173, 1143, 1090, 1037, 972, 1231, 1339, 1218, 1424, 1579, 1375, 1260, 1240, 1181, 1254, 1417, 1465, 1354, 1468, 1356, 1434, 1427, 1417, 1132, 1049, 1168, 1261, 1077, 859, 983, 1068, 1351, 1241, 1281, 1310, 1325, 1415, 1400, 1324, 1123, 820, 729, 590, 518, 520, 532, 417, 310, 232, 193, 207, 198, 199, 218, 202, 195, 216, 205, 218, 195, 236, 193, 194,
    198, 203, 210, 222, 214, 238, 230, 341, 2103, 2645, 1660, 1264, 1195, 1356, 1587, 1826, 2091, 2861, 2962, 2824, 2310, 2234, 2014, 1915, 1730, 1669, 1590, 1614, 1567, 1635, 1491, 1437, 1485, 1624, 1640, 1771, 1823, 1552, 1646, 2569, 4118, 3228, 2924, 2638, 2525, 2385, 2374, 2865, 3498, 4410, 1952, 1534, 1299, 1312, 1296, 1208, 1092, 1099, 1056, 1139, 1194, 1378, 1236, 1232, 1367, 1280, 1212, 1189, 1306, 1290, 1275, 1336, 1445, 1424, 1505, 1120, 1160, 1288, 1266, 1139, 994, 1048, 1230, 1110, 1025, 1102, 1221, 1446, 1289, 1165, 1142, 1182, 1271, 1306, 1237, 1041, 868, 688, 598, 511, 436, 459, 487, 600, 292, 228, 214, 232, 230, 205, 230, 209, 236, 200, 210, 213, 213, 217, 194,
    215, 203, 202, 224, 192, 204, 233, 681, 2931, 2127, 1552, 1207, 1351, 1464, 1726, 1869, 2291, 3003, 3057, 2435, 2060, 2011, 1966, 1851, 1606, 1434, 1569, 1587, 1465, 1534, 1413, 1386, 1374, 1310, 1326, 1484, 1444, 1395, 1577, 3086, 4235, 3241, 2840, 2843, 2813, 2441, 2370, 2962, 3919, 4866, 2290, 1701, 1641, 1510, 1315, 1205, 1122, 1138, 1256, 1205, 1228, 1273, 1270, 1402, 1299, 1236, 1257, 1264, 1228, 1238, 1209, 1397, 1355, 1377, 1310, 1220, 1238, 1185, 1155, 1201, 1095, 1041, 1108, 1172, 1140, 1144, 1175, 1327, 1249, 1208, 1286, 1237, 1162, 1270, 1154, 990, 925, 841, 678, 598, 473, 459, 506, 620, 588, 264, 219, 212, 214, 213, 216, 221, 208, 192, 204, 236, 230, 202, 196,
    204, 236, 223, 227, 238, 229, 318, 2155, 2840, 1770, 1506, 1318, 1388, 1598, 1813, 1903, 2909, 2857, 2624, 2127, 2082, 2165, 1975, 1855, 1576, 1507, 1523, 1591, 1486, 1438, 1372, 1295, 1396, 1336, 1326, 1318, 1346, 1506, 1583, 4305, 4270, 3353, 3027, 2927, 2903, 2903, 2833, 3069, 3702, 5644, 3330, 2188, 1764, 1503, 1558, 1342, 1207, 1275, 1213, 1289, 1346, 1208, 1156, 1210, 1295, 1307, 1291, 1385, 1233, 1192, 1189, 1420, 1463, 1519, 1428, 1149, 1148, 1104, 1060, 1123, 1157, 1091, 1056, 1147, 1178, 1181, 1265, 1395, 1393, 1315, 1228, 1164, 1204, 1201, 982, 963, 1039, 958, 811, 629, 498, 454, 513, 601, 788, 399, 216, 249, 222, 209, 210, 202, 215, 217, 214, 188, 230, 189, 231,
    212, 180, 213, 239, 232, 228, 323, 2172, 2799, 1825, 1385, 1273, 1301, 1721, 1738, 1908, 2856, 2753, 2508, 2104, 2114, 2106, 2140, 1911, 1692, 1590, 1579, 1540, 1499, 1432, 1473, 1342, 1419, 1382, 1474, 1496, 1444, 1612, 1890, 4520, 4345, 3488, 3359, 3471, 3501, 3527, 3114, 3334, 3862, 4791, 5405, 2592, 1809, 1680, 1878, 1757, 1513, 1187, 1198, 1247, 1406, 1233, 1246, 1344, 1310, 1206, 1298, 1443, 1330, 1270, 1278, 1431, 1459, 1358, 1420, 1119, 1127, 940, 1010, 936, 1073, 1099, 1006, 1148, 1156, 1109, 1271, 1340, 1547, 1436, 1423, 1330, 1291, 1246, 1034, 927, 919, 1081, 834, 661, 496, 522, 494, 576, 648, 703, 296, 213, 219, 188, 222, 189, 217, 220, 220, 211, 229, 245, 217,
    190, 237, 229, 232, 222, 231, 525, 2773, 2478, 1631, 1307, 1261, 1470, 1666, 1561, 2219, 2881, 2501, 2572, 2172, 2151, 2058, 2114, 1941, 1708, 1521, 1574, 1577, 1419, 1509, 1486, 1527, 1655, 1894, 1814, 1668, 2073, 1964, 1550, 3222, 3869, 3214, 2965, 2799, 3208, 3214, 3119, 3197, 3800, 4353, 4867, 3127, 2006, 1836, 1810, 1578, 1564, 1539, 1429, 1414, 1332, 1171, 1239, 1232, 1296, 1303, 1362, 1570, 1568, 1496, 1380, 1399, 1399, 1344, 1379, 1161, 1068, 1046, 943, 880, 879, 946, 1062, 1126, 1194, 1175, 1077, 1226, 1289, 1395, 1426, 1454, 1418, 1214, 1212, 1222, 1077, 916, 689, 691, 588, 517, 535, 558, 658, 631, 474, 252, 215, 227, 238, 237, 215, 247, 218, 231, 235, 202, 200,
    214, 229, 238, 230, 232, 298, 2318, 2921, 1775, 1287, 1122, 1411, 1517, 1504, 2138, 2763, 2477, 2633, 2334, 2086, 2020, 2084, 1905, 1659, 1513, 1465, 1564, 1627, 1666, 1833, 2335, 2435, 1912, 1946, 2148, 1883, 1655, 1566, 2084, 3995, 2867, 2576, 2435, 2404, 2587, 3297, 3697, 3542, 3826, 4447, 2662, 2079, 1774, 1653, 1520, 1497, 1468, 1549, 1637, 1632, 1326, 1319, 1206, 1097, 1337, 1514, 1506, 1634, 1443, 1433, 1368, 1473, 1360, 1328, 1285, 1057, 1023, 987, 923, 939, 849, 952, 950, 1092, 1122, 1129, 1225, 1216, 1240, 1253, 1501, 1512, 1358, 1317, 1234, 1155, 1049, 926, 716, 670, 556, 481, 515, 568, 574, 654, 468, 245, 201, 189, 228, 201, 197, 222, 216, 189, 203, 203, 218,
    226, 207, 228, 236, 259, 498, 2716, 2520, 1619, 1174, 1196, 1467, 1391, 1599, 2450, 2605, 2540, 2466, 2383, 2195, 2034, 1897, 1892, 1589, 1474, 1851, 1936, 1886, 2110, 2682, 2349, 2288, 2187, 2021, 2025, 1940, 1605, 1532, 2368, 4300, 3305, 2584, 2400, 2027, 2242, 3716, 3671, 3204, 3288, 3584, 2291, 1894, 1798, 1598, 1488, 1435, 1456, 1499, 1612, 1773, 1637, 1452, 1333, 1240, 1254, 1223, 1451, 1507, 1397, 1305, 1243, 1344, 1413, 1364, 1178, 961, 968, 1058, 849, 832, 826, 858, 874, 926, 970, 1080, 1146, 1139, 1153, 1237, 1205, 1117, 1093, 1034, 1119, 1124, 1040, 977, 699, 596, 618, 497, 557, 492, 560, 573, 610, 286, 234, 208, 245, 223, 225, 194, 203, 211, 227, 214, 222,
    185, 194, 231, 227, 237, 325, 1842, 2807, 1890, 1252, 1180, 1358, 1302, 1566, 2116, 2657, 2470, 2543, 2285, 2164, 2134, 2032, 1933, 1885, 1957, 2335, 2469, 2464, 2635, 2451, 2500, 2224, 2223, 2405, 2114, 2060, 2094, 1784, 1988, 3322, 3639, 2889, 2847, 3248, 2160, 2777, 2987, 3060, 3374, 3083, 2170, 1835, 1715, 1613, 1566, 1551, 1422, 1450, 1598, 1800, 1691, 1791, 1625, 1353, 1311, 1261, 1417, 1524, 1395, 1306, 1308, 1388, 1463, 1358, 1326, 1080, 996, 929, 1016, 1000, 949, 900, 882, 924, 832, 963, 1033, 1041, 999, 1155, 1089, 934, 1013, 887, 917, 1051, 1069, 1014, 920, 641, 553, 588, 541, 525, 506, 531, 612, 499, 239, 200, 197, 213, 185, 178, 209, 216, 189, 213, 233,
    211, 205, 211, 206, 220, 490, 2458, 2599, 1767, 1238, 1245, 1306, 1238, 1550, 2146, 2559, 2693, 2426, 2148, 2134, 2000, 2285, 2131, 2095, 2438, 2758, 2331, 2363, 2605, 2759, 2457, 2232, 2418, 2586, 2662, 2450, 2487, 2357, 2352, 3383, 3216, 2889, 2755, 2564, 1930, 2506, 2940, 2986, 3291, 3566, 2229, 1635, 1610, 1529, 1577, 1649, 1549, 1437, 1488, 1681, 1553, 1731, 1826, 1662, 1446, 1330, 1373, 1449, 1361, 1272, 1279, 1331, 1368, 1408, 1402, 1258, 1103, 963, 941, 1040, 1173, 996, 922, 866, 901, 908, 939, 939, 1060, 1071, 922, 743, 820, 895, 855, 886, 948, 982, 907, 767, 530, 513, 575, 541, 527, 561, 586, 705, 302, 221, 227, 225, 213, 225, 188, 194, 216, 223, 210,
    214, 209, 217, 197, 257, 858, 2976, 2312, 1573, 1228, 1287, 1268, 1395, 1666, 2429, 2676, 2419, 2370, 2052, 2028, 2064, 2175, 1998, 2074, 2579, 2165, 2528, 2714, 2869, 2320, 2255, 2569, 2585, 2502, 2769, 2510, 2809, 2522, 2304, 3437, 2869, 2702, 2955, 2443, 1810, 2419, 3229, 3287, 3305, 3710, 2218, 1568, 1612, 1446, 1450, 1390, 1520, 1486, 1519, 1490, 1600, 1671, 1773, 1731, 1475, 1486, 1441, 1401, 1350, 1299, 1247, 1242, 1271, 1445, 1262, 1216, 1046, 815, 871, 859, 854, 932, 919, 952, 949, 920, 866, 912, 832, 725, 744, 787, 820, 790, 752, 847, 866, 930, 851, 771, 705, 512, 582, 562, 538, 548, 621, 707, 309, 221, 204, 209, 195, 199, 222, 196, 206, 220, 203,
    223, 228, 209, 237, 331, 1885, 2880, 1874, 1263, 1201, 1218, 1312, 1601, 2046, 2756, 2484, 2373, 2067, 1915, 1839, 2180, 1914, 2140, 2669, 2450, 2344, 2578, 2764, 2348, 2169, 2276, 2303, 2516, 2771, 2934, 2996, 2907, 2850, 2580, 3641, 3264, 3210, 3278, 2662, 2100, 2297, 3030, 3065, 3263, 3622, 2071, 1845, 1541, 1404, 1449, 1423, 1508, 1519, 1563, 1604, 1650, 1700, 1615, 1586, 1581, 1667, 1618, 1351, 1268, 1211, 1199, 1207, 1267, 1340, 1224, 1105, 912, 856, 738, 694, 686, 726, 808, 736, 656, 735, 654, 669, 570, 646, 707, 790, 751, 829, 798, 751, 775, 810, 873, 774, 649, 510, 503, 542, 514, 521, 651, 738, 415, 192, 206, 207, 213, 212, 206, 223, 213, 200, 211,
    226, 245, 213, 252, 291, 1745, 2944, 1984, 1344, 1200, 1192, 1317, 1496, 1977, 2742, 2489, 2259, 1909, 1821, 1776, 2175, 2136, 2256, 2767, 2459, 2456, 2495, 2272, 2181, 2351, 2352, 2364, 2761, 2876, 2724, 2614, 2516, 2718, 2314, 3324, 2739, 2735, 3061, 2591, 1930, 1705, 2319, 2879, 2894, 3447, 2798, 1753, 1648, 1393, 1353, 1390, 1428, 1450, 1493, 1554, 1552, 1674, 1597, 1541, 1516, 1579, 1646, 1605, 1400, 1295, 1138, 1148, 1291, 1257, 1276, 1141, 977, 874, 777, 736, 649, 698, 640, 742, 595, 578, 574, 709, 664, 668, 654, 655, 687, 676, 715, 739, 725, 747, 819, 721, 680, 574, 544, 542, 488, 509, 575, 656, 732, 321, 242, 220, 188, 201, 253, 206, 228, 205, 214,
    188, 221, 213, 225, 403, 2197, 2826, 1799, 1278, 1234, 1115, 1350, 1601, 2249, 2616, 2415, 2152, 1767, 1599, 1933, 2468, 2171, 2274, 2950, 2790, 2474, 2294, 2237, 2253, 2355, 2370, 2740, 2795, 2467, 2434, 2523, 2431, 2490, 2032, 3200, 2653, 2432, 2349, 2161, 1689, 1614, 2091, 2688, 2594, 3259, 2841, 1658, 1492, 1436, 1355, 1183, 1302, 1334, 1395, 1507, 1535, 1674, 1612, 1572, 1579, 1600, 1634, 1580, 1505, 1422, 1254, 1219, 1244, 1337, 1235, 1187, 879, 803, 800, 719, 733, 629, 657, 712, 701, 622, 604, 605, 527, 587, 661, 622, 594, 606, 708, 693, 683, 687, 675, 698, 612, 632, 479, 557, 558, 528, 610, 675, 784, 304, 209, 196, 183, 227, 191, 206, 208, 229, 212,
    243, 203, 236, 261, 1513, 2968, 2073, 1458, 1237, 1184, 1373, 1663, 2008, 2523, 2350, 2251, 1800, 1617, 1736, 2916, 2816, 1988, 2760, 3127, 2333, 2248, 2281, 2298, 2393, 2531, 2781, 2685, 2480, 2588, 2518, 2526, 2677, 2248, 3214, 2997, 2657, 2531, 2700, 1882, 1531, 1593, 2342, 2498, 2740, 3602, 2234, 1557, 1387, 1343, 1175, 1167, 1210, 1300, 1329, 1420, 1430, 1549, 1504, 1571, 1740, 1897, 1767, 1626, 1484, 1279, 1275, 1276, 1300, 1306, 1164, 1011, 797, 767, 923, 790, 750, 750, 616, 591, 536, 607, 553, 486, 520, 579, 538, 563, 583, 593, 591, 727, 604, 644, 637, 562, 571, 524, 505, 569, 569, 560, 654, 750, 663, 282, 180, 203, 224, 211, 192, 221, 194, 206, 218,
    191, 222, 251, 403, 2165, 2746, 1762, 1295, 1170, 1088, 1401, 1826, 2216, 2320, 2338, 2060, 1935, 1776, 1971, 3369, 2278, 2057, 2480, 2160, 2202, 2170, 2168, 2500, 2496, 2665, 2818, 2414, 2364, 2230, 2315, 2588, 2536, 2457, 3243, 2789, 2194, 2935, 2695, 1607, 1338, 1351, 2227, 2486, 2599, 3328, 2435, 1495, 1269, 1324, 1068, 1112, 1109, 1141, 1282, 1420, 1369, 1385, 1440, 1625, 1632, 1661, 1628, 1551, 1473, 1354, 1344, 1318, 1399, 1367, 1215, 957, 739, 783, 883, 760, 671, 556, 602, 584, 556, 596, 587, 459, 452, 490, 594, 533, 542, 574, 567, 545, 539, 539, 590, 551, 608, 527, 524, 541, 548, 595, 647, 777, 675, 276, 205, 203, 202, 213, 213, 175, 221, 217, 225,
    211, 203, 210, 253, 983, 2921, 2191, 1431, 1249, 1058, 1292, 1667, 2057, 2262, 2356, 2209, 1983, 1826, 1969, 2282, 2177, 1896, 2118, 1816, 1964, 2288, 2194, 2419, 2495, 2829, 3195, 2761, 2129, 1902, 2098, 2287, 2132, 2581, 2901, 3032, 2407, 2948, 3594, 2258, 1499, 1853, 1769, 2432, 2623, 2700, 3312, 2378, 1588, 1232, 1036, 1153, 1173, 1036, 951, 1217, 1287, 1215, 1361, 1398, 1488, 1535, 1468, 1589, 1530, 1361, 1299, 1293, 1340, 1311, 1364, 1121, 887, 882, 898, 913, 677, 641, 637, 693, 572, 541, 570, 556, 528, 516, 524, 557, 611, 562, 610, 555, 501, 473, 472, 601, 576, 617, 593, 565, 461, 528, 547, 649, 764, 683, 247, 192, 206, 212, 224, 217, 232, 218, 200,
    225, 204, 209, 500, 2416, 2571, 1700, 1293, 1132, 1108, 1479, 1904, 2058, 2284, 2306, 2128, 1824, 1977, 2217, 1955, 1856, 1913, 1763, 1732, 1856, 2082, 2467, 2185, 2382, 2449, 2684, 2060, 1846, 1761, 1962, 2065, 2724, 2538, 2863, 2489, 3310, 3491, 2760, 1813, 1790, 1821, 2557, 2767, 3026, 3349, 3583, 2082, 1538, 1119, 1150, 1298, 1059, 1107, 1104, 1227, 1295, 1293, 1322, 1390, 1402, 1317, 1545, 1517, 1411, 1275, 1432, 1288, 1333, 1357, 1274, 1024, 931, 936, 823, 769, 657, 619, 618, 551, 587, 515, 580, 539, 516, 553, 555, 526, 538, 596, 552, 540, 558, 474, 541, 537, 514, 616, 584, 481, 472, 517, 532, 665, 761, 395, 220, 203, 224, 214, 209, 199, 220, 200, 197,
    189, 215, 245, 259, 1495, 2990, 2081, 1411, 1105, 1072, 1241, 1775, 2045, 2222, 2239, 2182, 1972, 1942, 2004, 1961, 2005, 2199, 1857, 1711, 1619, 1810, 2141, 2065, 2027, 2436, 2245, 2115, 1896, 1944, 1954, 1888, 2588, 2299, 3383, 3251, 3167, 3224, 3647, 2305, 1896, 1705, 1935, 2867, 3177, 3233, 3792, 3620, 2111, 1464, 1307, 1199, 1341, 1327, 1066, 1124, 1215, 1286, 1256, 1339, 1384, 1392, 1273, 1424, 1497, 1276, 1253, 1379, 1367, 1293, 1333, 1077, 914, 912, 902, 690, 696, 667, 575, 615, 758, 590, 504, 556, 571, 584, 513, 526, 480, 481, 571, 500, 566, 628, 554, 521, 553, 533, 605, 584, 487, 412, 494, 527, 519, 556, 283, 213, 203, 218, 196, 208, 211, 216, 226,
    208, 229, 241, 630, 2598, 2420, 1639, 1200, 1082, 1141, 1440, 2065, 2294, 2176, 2185, 2011, 1952, 2350, 2055, 1886, 2296, 2029, 1625, 1742, 1789, 2130, 2046, 1892, 1999, 2235, 2084, 1988, 2008, 1784, 1823, 2265, 2264, 3242, 3435, 3152, 2792, 3356, 3249, 2137, 1884, 1968, 2856, 3579, 3354, 3135, 3442, 3699, 1742, 1446, 1557, 1548, 1293, 1256, 1080, 1058, 1208, 1291, 1248, 1437, 1341, 1211, 1316, 1314, 1238, 1172, 1248, 1254, 1300, 1281, 1093, 874, 965, 909, 815, 679, 686, 598, 558, 630, 624, 554, 549, 554, 560, 507, 508, 527, 495, 546, 501, 539, 531, 509, 508, 539, 557, 551, 516, 498, 438, 506, 612, 544, 546, 638, 300, 242, 223, 202, 211, 238, 207, 200, 210,
    205, 194, 229, 321, 1886, 2799, 1800, 1362, 1146, 1067, 1310, 1751, 2209, 2383, 2297, 2270, 2004, 2249, 2530, 1970, 2204, 2392, 1695, 1568, 1751, 1963, 2140, 1985, 1971, 1924, 2046, 1930, 1931, 1910, 2080, 2285, 2250, 3005, 3888, 3028, 2762, 3187, 3606, 1924, 1847, 1965, 2411, 2796, 3591, 3556, 3386, 3443, 2843, 1500, 1290, 1343, 1338, 1354, 1245, 1198, 1170, 1157, 1293, 1353, 1388, 1285, 1294, 1409, 1224, 1142, 1194, 1133, 1192, 1303, 1134, 946, 871, 959, 845, 802, 726, 616, 554, 611, 590, 514, 475, 494, 548, 551, 520, 529, 561, 481, 538, 539, 540, 490, 474, 481, 631, 649, 558, 537, 509, 489, 589, 520, 473, 775, 456, 243, 194, 215, 228, 209, 176, 216, 229,
    218, 228, 267, 1164, 2895, 2166, 1475, 1105, 1104, 1166, 1442, 1969, 2427, 2307, 2113, 2121, 2200, 2773, 2462, 2453, 2557, 1922, 1459, 1526, 1802, 2106, 2097, 1953, 1978, 1823, 2012, 1977, 1678, 2045, 2471, 2118, 2898, 4099, 3327, 3030, 2923, 4017, 2083, 1747, 2037, 2217, 2054, 3150, 3398, 2960, 3427, 2500, 1580, 1275, 1238, 1176, 1207, 1306, 1252, 1097, 1229, 1177, 1279, 1276, 1296, 1263, 1336, 1290, 1201, 1237, 1117, 1146, 1135, 1246, 1177, 1054, 1002, 916, 899, 797, 623, 541, 571, 615, 527, 552, 511, 495, 530, 489, 496, 473, 498, 495, 622, 572, 526, 481, 468, 483, 520, 497, 514, 479, 507, 542, 573, 542, 525, 754, 324, 192, 205, 213, 191, 211, 229, 208, 227,
    217, 220, 226, 420, 2081, 2667, 1847, 1289, 1037, 1119, 1351, 1647, 2265, 2523, 2263, 2341, 2113, 2740, 2474, 2175, 2504, 2024, 1432, 1544, 1550, 2024, 2118, 1896, 1854, 1753, 1946, 1938, 1737, 2141, 2376, 2305, 2633, 3717, 3764, 3003, 2782, 3547, 3076, 1778, 2060, 2019, 1902, 2146, 2981, 2920, 2739, 3453, 2109, 1173, 1143, 1175, 1103, 1250, 1239, 1275, 1035, 1081, 1035, 1225, 1385, 1278, 1322, 1366, 1270, 1231, 1114, 1088, 1134, 1189, 1209, 1204, 1100, 944, 865, 682, 675, 593, 557, 604, 536, 509, 563, 563, 467, 455, 509, 543, 538, 531, 523, 584, 548, 593, 478, 437, 489, 552, 533, 560, 498, 468, 456, 543, 540, 844, 725, 252, 215, 227, 189, 210, 210, 227, 206,
    227, 252, 270, 1387, 2974, 2163, 1495, 1129, 1054, 1095, 1387, 1988, 2342, 2430, 2315, 2095, 2541, 2555, 2189, 2160, 1946, 1391, 1461, 1526, 1684, 1898, 1893, 1757, 1870, 1852, 1964, 1833, 2295, 2227, 2583, 2298, 3619, 4382, 3578, 3004, 3184, 3673, 1998, 1955, 1942, 1943, 1944, 2579, 2853, 2600, 2719, 3047, 1342, 1314, 1063, 1231, 1166, 1187, 1262, 1088, 1098, 965, 1144, 1205, 1349, 1158, 1290, 1328, 1162, 1146, 1094, 1177, 1106, 1326, 1281, 1183, 879, 879, 685, 623, 632, 614, 587, 550, 542, 575, 556, 598, 538, 479, 519, 574, 681, 556, 508, 527, 503, 546, 481, 532, 501, 519, 541, 519, 506, 471, 464, 582, 723, 904, 364, 214, 209, 194, 213, 214, 209, 193, 203,
    201, 237, 283, 1484, 3006, 2179, 1510, 1152, 1069, 1127, 1453, 1894, 2339, 2401, 2270, 2226, 2213, 2102, 2051, 2360, 1863, 1484, 1663, 1414, 1454, 1775, 1721, 1840, 1720, 1815, 1997, 2098, 2031, 2183, 2305, 2345, 3436, 4266, 3537, 3141, 3365, 3790, 1855, 1594, 1540, 1805, 1717, 2070, 2760, 2613, 2787, 3316, 1743, 1411, 1209, 1129, 1245, 1219, 1203, 1215, 1220, 917, 955, 1259, 1257, 1209, 1226, 1334, 1217, 1174, 1169, 1178, 1119, 1399, 1502, 1047, 892, 881, 668, 640, 635, 599, 551, 622, 590, 580, 504, 575, 439, 469, 458, 526, 549, 501, 519, 515, 570, 494, 478, 510, 459, 584, 575, 525, 482, 509, 517, 613, 699, 923, 362, 207, 227, 227, 208, 197, 201, 192, 229,
    216, 214, 256, 1307, 2842, 2179, 1549, 1243, 1121, 1175, 1492, 1922, 2435, 2393, 2258, 2266, 2350, 2288, 2004, 2291, 1993, 1358, 1390, 1445, 1324, 1646, 1680, 1808, 1969, 2048, 2382, 2281, 2089, 2262, 2164, 1858, 2445, 4331, 3550, 3069, 3567, 4115, 1925, 1569, 1673, 1622, 1445, 1662, 2717, 2815, 2941, 3518, 2436, 1482, 1257, 1162, 1199, 1215, 1138, 1229, 1245, 1027, 991, 1151, 1276, 1194, 1316, 1452, 1231, 1140, 1223, 1175, 1252, 1399, 1490, 1082, 894, 810, 676, 659, 581, 605, 591, 538, 560, 537, 519, 492, 481, 521, 460, 495, 444, 499, 534, 525, 550, 505, 494, 532, 491, 552, 670, 600, 609, 496, 548, 576, 681, 925, 551, 241, 207, 232, 228, 210, 209, 217, 195,
    228, 210, 233, 582, 2105, 2583, 1732, 1438, 1218, 1034, 1314, 1647, 2278, 2386, 2177, 2259, 2278, 2372, 2185, 2251, 2238, 1696, 1226, 1208, 1298, 1568, 1596, 1722, 2048, 2216, 2368, 2405, 2163, 2115, 2205, 1919, 2092, 3465, 3833, 3571, 3623, 3918, 2049, 1533, 1529, 1406, 1265, 1435, 2138, 2999, 2953, 2948, 3425, 1997, 1600, 1271, 1140, 1219, 1166, 1230, 1319, 1349, 1370, 1180, 1303, 1356, 1294, 1519, 1357, 1235, 1188, 1161, 1249, 1339, 1662, 1208, 810, 811, 719, 632, 579, 641, 593, 532, 540, 532, 545, 540, 459, 594, 465, 486, 438, 510, 489, 513, 641, 549, 480, 539, 475, 498, 551, 549, 590, 515, 475, 531, 632, 790, 895, 335, 194, 208, 204, 243, 234, 226, 214,
    217, 237, 248, 1147, 2646, 2252, 1664, 1384, 1215, 1217, 1456, 1955, 2411, 2189, 2222, 2315, 2269, 2390, 2121, 2324, 1926, 1547, 1353, 1150, 1471, 1757, 1698, 2134, 2216, 2096, 2462, 2326, 2187, 2213, 1931, 2246, 2606, 3810, 3543, 3495, 3645, 3150, 1706, 1632, 1440, 1252, 1304, 1686, 2605, 2987, 2769, 2850, 3279, 2067, 1457, 1237, 1088, 1204, 1303, 1320, 1344, 1487, 1367, 1389, 1474, 1407, 1382, 1304, 1336, 1190, 1174, 1179, 1275, 1556, 1446, 985, 818, 680, 615, 582, 580, 601, 544, 556, 528, 536, 514, 511, 511, 467, 519, 531, 474, 427, 494, 477, 522, 465, 508, 489, 500, 463, 486, 524, 572, 556, 573, 563, 678, 839, 737, 254, 230, 162, 206, 192, 214, 205, 241,
    221, 217, 321, 1727, 2623, 2106, 1572, 1351, 1218, 1313, 1575, 2113, 2182, 2152, 2243, 2151, 2387, 2159, 2340, 2074, 1759, 1560, 1384, 1084, 1355, 1719, 1790, 2063, 2176, 2249, 2371, 2280, 2021, 1987, 2008, 2439, 2690, 3886, 3230, 3000, 4050, 2353, 1586, 1481, 1066, 1192, 1512, 1679, 3048, 2788, 2709, 2760, 3082, 2243, 1479, 1272, 1208, 1102, 1171, 1303, 1264, 1376, 1406, 1513, 1420, 1341, 1182, 1181, 1179, 1172, 1203, 1198, 1430, 1568, 1222, 918, 848, 747, 632, 611, 570, 551, 579, 570, 564, 618, 612, 584, 517, 547, 521, 485, 422, 512, 417, 469, 421, 441, 535, 601, 479, 494, 528, 513, 624, 553, 591, 637, 727, 950, 485, 220, 218, 210, 218, 184, 196, 188, 198,
    190, 206, 281, 1477, 2806, 2237, 1699, 1444, 1221, 1351, 1500, 2028, 2226, 2107, 2272, 2140, 2258, 2155, 2205, 2093, 1697, 1474, 1341, 1149, 1194, 1556, 1801, 1880, 2164, 2359, 2392, 2187, 1984, 1815, 2098, 2175, 2205, 3743, 3330, 3210, 3784, 2300, 1579, 1345, 1137, 1207, 1468, 1581, 2009, 2179, 2604, 2691, 2794, 2260, 1319, 1168, 1083, 1076, 1097, 1277, 1416, 1402, 1466, 1485, 1434, 1119, 1055, 1104, 1083, 1169, 1249, 1299, 1401, 1479, 1160, 867, 869, 771, 698, 668, 559, 613, 579, 511, 601, 611, 629, 579, 555, 491, 578, 501, 425, 444, 477, 526, 477, 471, 474, 526, 469, 503, 529, 539, 575, 588, 608, 652, 766, 992, 667, 211, 236, 205, 195, 195, 201, 222, 194,
    229, 198, 270, 1334, 2710, 2398, 1776, 1366, 1384, 1450, 1498, 1994, 2214, 2066, 2188, 2147, 1987, 2127, 2251, 2004, 1678, 1512, 1370, 1179, 1012, 1346, 1737, 1690, 2174, 2239, 2361, 2276, 1984, 1896, 2289, 2031, 2326, 4081, 3667, 3435, 3902, 2998, 1600, 1512, 1227, 1284, 1425, 1551, 1906, 1660, 2814, 2847, 2655, 2997, 1508, 1174, 1120, 960, 1152, 1211, 1292, 1411, 1528, 1368, 1323, 1116, 1055, 1103, 1137, 1139, 1192, 1280, 1367, 1539, 1178, 879, 784, 749, 678, 661, 655, 692, 562, 502, 535, 557, 571, 585, 580, 506, 463, 426, 439, 524, 600, 506, 497, 481, 470, 503, 514, 521, 514, 530, 503, 656, 586, 616, 653, 837, 1000, 329, 215, 251, 184, 191, 227, 214, 209,
    201, 181, 244, 521, 2114, 2744, 2086, 1618, 1365, 1281, 1446, 1646, 2264, 2175, 2142, 2153, 2016, 2104, 2213, 2077, 1725, 1610, 1462, 1398, 1041, 1171, 1351, 1666, 1926, 2295, 2143, 2250, 2081, 2119, 2230, 2210, 2124, 3662, 4363, 3616, 3480, 3986, 1926, 1422, 1108, 1015, 1112, 1505, 1938, 1552, 1940, 2827, 2708, 3026, 2663, 1485, 1166, 1231, 1227, 1234, 1249, 1287, 1409, 1436, 1320, 1172, 1023, 1046, 1133, 1143, 1117, 1281, 1298, 1471, 1402, 1033, 813, 805, 683, 634, 627, 623, 583, 551, 554, 559, 562, 524, 508, 485, 451, 439, 457, 618, 822, 543, 527, 498, 499, 489, 464, 529, 511, 556, 540, 491, 582, 618, 601, 666, 1012, 555, 225, 178, 227, 207, 202, 234, 207,
    224, 235, 268, 1315, 2586, 2192, 1748, 1449, 1370, 1330, 1480, 1859, 2415, 2107, 2257, 2198, 1857, 2141, 1999, 1871, 1665, 1550, 1458, 1345, 972, 1192, 1494, 1630, 1897, 2096, 2101, 2196, 2225, 2223, 2091, 2103, 2858, 4712, 3982, 3230, 4061, 2964, 1520, 1148, 1020, 1107, 1674, 1694, 1397, 1526, 2441, 3035, 2804, 3265, 2119, 1272, 1227, 1226, 1347, 1296, 1282, 1276, 1436, 1308, 1145, 1043, 1010, 1242, 1290, 1171, 1214, 1378, 1320, 1500, 1213, 925, 808, 697, 670, 579, 566, 575, 477, 569, 598, 561, 495, 514, 445, 379, 458, 431, 444, 507, 521, 471, 500, 504, 448, 489, 445, 493, 552, 545, 516, 530, 560, 578, 639, 790, 1053, 360, 218, 221, 187, 205, 203, 198, 201,
    252, 226, 279, 1501, 2721, 2226, 1718, 1558, 1332, 1346, 1432, 1814, 2178, 2196, 2096, 2008, 1804, 1894, 1952, 1863, 1690, 1478, 1455, 1413, 1077, 1138, 1355, 1614, 1854, 2146, 2151, 2406, 2218, 1930, 1843, 2155, 2841, 3947, 3062, 3092, 4007, 2947, 1604, 1298, 1052, 1400, 1798, 1540, 1569, 1611, 2267, 3227, 3010, 3393, 2663, 1471, 1293, 1311, 1290, 1394, 1349, 1320, 1372, 1340, 1075, 891, 1056, 1186, 1208, 1245, 1211, 1282, 1386, 1397, 1111, 742, 760, 668, 675, 705, 740, 633, 562, 531, 524, 483, 548, 466, 500, 453, 401, 425, 435, 485, 495, 449, 493, 479, 470, 497, 496, 506, 512, 534, 455, 507, 493, 529, 547, 716, 968, 355, 217, 207, 191, 194, 210, 211, 211,
    183, 204, 224, 1293, 2699, 2263, 1721, 1489, 1349, 1403, 1532, 1702, 1979, 2025, 1970, 2042, 1849, 1935, 2047, 1838, 1628, 1471, 1530, 1550, 1378, 1185, 1376, 1593, 1713, 2032, 2260, 2402, 2007, 1730, 1814, 1781, 2194, 2988, 3164, 2945, 3492, 3787, 2199, 1593, 1373, 1611, 1822, 1503, 1557, 1570, 1785, 3096, 3121, 3295, 3461, 1820, 1472, 1487, 1431, 1319, 1294, 1394, 1290, 1167, 1104, 1015, 1293, 1318, 1251, 1292, 1235, 1245, 1370, 1539, 1092, 748, 665, 721, 716, 818, 966, 967, 935, 837, 785, 613, 552, 509, 493, 489, 502, 470, 472, 511, 600, 560, 485, 467, 430, 486, 440, 478, 443, 434, 418, 461, 561, 506, 515, 687, 1004, 450, 207, 198, 201, 228, 206, 247, 223,
    219, 212, 252, 924, 2686, 2496, 1866, 1541, 1391, 1386, 1521, 1679, 2080, 1960, 1895, 1971, 1799, 1971, 1917, 1804, 1638, 1365, 1475, 1446, 1442, 1407, 1502, 1557, 1709, 2100, 2313, 2218, 1918, 1715, 1492, 1630, 1995, 2640, 3475, 3083, 3630, 3191, 2110, 1608, 1476, 1590, 1692, 1593, 1580, 1525, 1617, 2814, 3239, 3271, 3268, 2013, 1379, 1583, 1278, 1245, 1282, 1338, 1276, 1205, 1098, 1125, 1296, 1352, 1179, 1225, 1153, 1090, 1362, 1495, 1117, 787, 627, 769, 741, 1055, 1044, 1080, 1092, 1007, 945, 853, 664, 542, 461, 579, 584, 495, 472, 420, 456, 524, 584, 502, 463, 460, 452, 492, 465, 448, 476, 399, 532, 494, 464, 671, 993, 473, 220, 205, 220, 220, 190, 237, 198,
    198, 225, 240, 624, 2549, 2681, 1887, 1672, 1466, 1371, 1473, 1618, 2082, 1867, 1917, 1878, 1861, 1843, 2062, 1749, 1506, 1382, 1406, 1456, 1544, 1447, 1498, 1623, 1728, 2208, 2432, 2147, 1719, 1672, 1648, 1788, 2119, 2134, 3244, 3050, 3350, 3292, 2030, 1741, 1856, 1509, 1567, 1614, 1399, 1549, 1641, 2087, 3578, 3233, 2713, 3151, 1488, 1548, 1062, 1146, 1148, 1231, 1150, 1251, 1100, 1166, 1290, 1288, 1285, 1218, 1165, 1271, 1254, 1437, 1202, 897, 813, 830, 816, 991, 1100, 1130, 1107, 1101, 956, 999, 947, 722, 569, 567, 765, 671, 500, 420, 419, 435, 477, 515, 482, 452, 515, 512, 430, 392, 431, 428, 486, 464, 469, 650, 1006, 762, 236, 220, 193, 198, 213, 222, 209,
    205, 212, 240, 608, 2515, 2591, 1970, 1690, 1661, 1549, 1534, 1690, 2067, 1889, 1913, 1865, 1878, 2037, 1891, 1587, 1422, 1355, 1348, 1319, 1331, 1479, 1458, 1522, 1816, 2106, 2204, 2086, 1889, 1609, 1819, 1947, 1951, 1814, 3316, 3168, 3330, 3242, 1839, 1810, 1703, 1275, 1481, 1371, 1227, 1430, 1800, 2334, 3768, 2971, 2716, 3104, 1706, 1258, 1012, 934, 1051, 1017, 954, 1186, 1323, 1261, 1254, 1214, 1270, 1183, 1257, 1282, 1363, 1395, 1151, 1026, 858, 930, 1038, 1164, 1127, 1222, 1252, 1193, 1017, 1044, 985, 851, 686, 622, 724, 583, 468, 409, 395, 421, 383, 471, 454, 490, 543, 478, 422, 385, 399, 415, 441, 508, 477, 644, 975, 767, 214, 234, 225, 201, 234, 210, 209,
    210, 236, 239, 685, 2670, 2352, 1973, 1808, 1765, 1545, 1654, 1797, 2067, 1807, 1852, 1909, 1904, 2022, 1913, 1534, 1380, 1331, 1312, 1315, 1287, 1359, 1464, 1560, 1789, 2008, 1776, 1754, 1648, 1648, 1938, 1986, 1665, 1836, 3339, 3150, 3370, 3116, 1766, 1735, 1399, 1333, 1409, 1260, 1372, 1445, 1922, 1982, 2200, 2127, 2388, 2539, 1505, 1047, 1066, 1034, 1077, 1123, 1140, 1210, 1334, 1284, 1308, 1211, 1259, 1223, 1229, 1255, 1390, 1377, 1110, 1141, 986, 1076, 1133, 1248, 1312, 1117, 1154, 1165, 1087, 1049, 1051, 970, 691, 515, 463, 436, 383, 415, 441, 424, 424, 417, 441, 432, 452, 419, 410, 402, 398, 453, 480, 519, 565, 751, 1016, 491, 210, 184, 221, 189, 191, 213, 202,
    193, 213, 244, 308, 1613, 2869, 2140, 1909, 1782, 1746, 1721, 1851, 2102, 2061, 1846, 1980, 1993, 2271, 2087, 1634, 1300, 1249, 1361, 1313, 1293, 1338, 1352, 1370, 1591, 1794, 1781, 1792, 1918, 1847, 2089, 2110, 1756, 1657, 2931, 3280, 2970, 3446, 1932, 1674, 1378, 1338, 1508, 1470, 1570, 1737, 1772, 1644, 1877, 2147, 1865, 1988, 1477, 1160, 1094, 1120, 1109, 1249, 1336, 1414, 1200, 1329, 1310, 1245, 1214, 1232, 1198, 1252, 1318, 1430, 1077, 1094, 1200, 1171, 1277, 1256, 1245, 1162, 1113, 1018, 937, 1030, 1039, 934, 921, 622, 410, 405, 374, 366, 371, 395, 428, 412, 411, 429, 431, 444, 456, 420, 370, 384, 414, 484, 529, 703, 903, 851, 246, 190, 208, 207, 222, 214, 210,
    221, 204, 236, 310, 1736, 2684, 2068, 1844, 1864, 1684, 1741, 1906, 2132, 1968, 1941, 1950, 2265, 2200, 1840, 1363, 1339, 1279, 1314, 1272, 1293, 1302, 1326, 1378, 1633, 1652, 1704, 1927, 1781, 1899, 2067, 1813, 1599, 1745, 3043, 3390, 3024, 3572, 2297, 1746, 1428, 1590, 1509, 1515, 1505, 1699, 1626, 1765, 2016, 1905, 1634, 1170, 1257, 1408, 1224, 1115, 1146, 1291, 1367, 1317, 1402, 1235, 1378, 1290, 1312, 1321, 1187, 1295, 1358, 1337, 1023, 1099, 1258, 1272, 1340, 1370, 1346, 1280, 1112, 1101, 975, 1011, 1100, 965, 756, 541, 422, 398, 412, 369, 348, 419, 468, 462, 475, 509, 441, 426, 405, 428, 369, 382, 433, 467, 490, 659, 908, 787, 227, 205, 193, 207, 221, 215, 182,
    222, 230, 233, 310, 1705, 2707, 2166, 1899, 1902, 1834, 1696, 1868, 2081, 2040, 2080, 2073, 2236, 2141, 1698, 1366, 1193, 1145, 1121, 1246, 1283, 1263, 1315, 1401, 1614, 1686, 1835, 1907, 1725, 1794, 1891, 1740, 1642, 2073, 3476, 3477, 3097, 3766, 2412, 1817, 1518, 1582, 1587, 1471, 1677, 1596, 1636, 1904, 1820, 1809, 1375, 1157, 1113, 1422, 1452, 1245, 1177, 1388, 1290, 1351, 1438, 1237, 1265, 1188, 1350, 1306, 1258, 1256, 1307, 1239, 986, 1186, 1408, 1416, 1493, 1504, 1459, 1264, 1125, 1158, 1119, 1082, 891, 850, 697, 571, 408, 376, 414, 399, 434, 541, 412, 437, 476, 485, 449, 403, 428, 383, 396, 403, 375, 486, 552, 683, 1005, 639, 236, 187, 214, 216, 191, 217, 213,
    235, 219, 193, 251, 1166, 2758, 2314, 2010, 1905, 1863, 1776, 1779, 2031, 2120, 2212, 2187, 2033, 1907, 1736, 1449, 1217, 1212, 1157, 1240, 1322, 1218, 1330, 1323, 1420, 1627, 1760, 2004, 1908, 1893, 1794, 2076, 1952, 1807, 2307, 2958, 2939, 3582, 2726, 1854, 1612, 1564, 1601, 1464, 1705, 1490, 1598, 1943, 1597, 1724, 1325, 1215, 1120, 1272, 1288, 1465, 1345, 1390, 1259, 1432, 1467, 1459, 1133, 1083, 1268, 1260, 1277, 1171, 1321, 1231, 1016, 1073, 1308, 1443, 1425, 1458, 1288, 1235, 1120, 1150, 1223, 1068, 950, 851, 731, 591, 464, 414, 355, 364, 374, 449, 401, 430, 415, 449, 437, 403, 444, 445, 374, 389, 404, 439, 567, 691, 975, 749, 252, 225, 221, 252, 191, 185, 195,
    240, 199, 235, 245, 989, 2807, 2295, 1938, 1773, 1942, 1826, 1888, 2065, 2282, 2337, 2139, 1974, 1822, 1583, 1484, 1257, 1183, 1109, 1242, 1336, 1359, 1326, 1386, 1328, 1503, 1851, 2079, 1994, 1654, 1784, 1910, 2036, 2036, 2204, 2637, 2663, 3059, 1925, 1685, 1420, 1338, 1292, 1534, 1709, 1530, 1705, 1584, 1634, 1628, 1467, 1444, 1318, 1330, 1279, 1326, 1398, 1401, 1311, 1448, 1537, 1527, 1150, 1081, 1203, 1245, 1128, 1181, 1367, 1164, 1073, 1133, 1308, 1453, 1403, 1381, 1298, 1302, 1204, 1125, 1137, 971, 902, 791, 558, 513, 362, 373, 344, 415, 390, 400, 407, 373, 440, 463, 444, 405, 408, 399, 433, 448, 422, 476, 601, 789, 1136, 502, 226, 212, 210, 200, 189, 194, 221,
    203, 205, 234, 234, 543, 2472, 2483, 1963, 1824, 1861, 1835, 1816, 2127, 2458, 2321, 2192, 1882, 1661, 1497, 1383, 1382, 1222, 1278, 1277, 1309, 1279, 1288, 1341, 1444, 1581, 1699, 1964, 1702, 1602, 1822, 2018, 2240, 2383, 2003, 2354, 1763, 2306, 1826, 1464, 1326, 1417, 1604, 1751, 1966, 1524, 1522, 1362, 1765, 1548, 1613, 1474, 1365, 1253, 1228, 1157, 1315, 1525, 1413, 1438, 1531, 1517, 1276, 1123, 1221, 1144, 1280, 1198, 1390, 1152, 1115, 1123, 1255, 1362, 1386, 1318, 1231, 1279, 1222, 1051, 1007, 881, 778, 600, 603, 599, 399, 386, 383, 418, 376, 493, 427, 387, 431, 486, 450, 457, 471, 425, 424, 446, 489, 505, 665, 825, 1260, 618, 235, 207, 226, 191, 218, 201, 211,
    184, 222, 229, 216, 406, 2266, 2663, 1997, 1849, 1894, 1872, 1755, 1999, 2383, 2373, 1989, 1890, 1609, 1483, 1413, 1387, 1337, 1256, 1394, 1275, 1316, 1314, 1395, 1618, 1678, 1857, 1939, 1812, 1630, 1766, 2178, 2701, 2333, 2134, 1994, 1553, 2017, 1813, 1542, 1485, 1816, 1845, 1881, 1368, 1389, 1335, 1279, 1523, 1541, 1516, 1460, 1254, 1232, 1227, 1212, 1246, 1348, 1500, 1353, 1324, 1395, 1288, 1303, 1244, 1210, 1209, 1206, 1445, 1127, 1049, 1043, 1156, 1285, 1105, 1202, 1150, 1133, 1065, 966, 787, 682, 609, 590, 600, 527, 422, 349, 500, 428, 426, 418, 354, 433, 488, 473, 507, 500, 470, 403, 428, 443, 475, 514, 585, 886, 1148, 529, 263, 208, 191, 203, 193, 228, 189,
    208, 233, 233, 220, 330, 1857, 2669, 2131, 1896, 1901, 1978, 1718, 1881, 2350, 2227, 1946, 1723, 1573, 1462, 1453, 1315, 1425, 1305, 1284, 1210, 1143, 1281, 1367, 1767, 1687, 1899, 1928, 1891, 1920, 2018, 2283, 2387, 2065, 2155, 1703, 1647, 1884, 1955, 1724, 1788, 2039, 1723, 1141, 1056, 1212, 1124, 1140, 1450, 1692, 1713, 1513, 1310, 1114, 1201, 1224, 1266, 1375, 1435, 1392, 1383, 1435, 1378, 1270, 1372, 1447, 1230, 1268, 1297, 1158, 1023, 964, 1070, 1119, 1110, 1036, 953, 873, 897, 884, 671, 626, 638, 512, 505, 452, 434, 394, 389, 397, 354, 421, 403, 385, 491, 509, 590, 485, 471, 455, 445, 450, 506, 498, 621, 785, 1160, 562, 201, 225, 231, 208, 209, 217, 230,
    202, 200, 208, 239, 287, 1752, 2742, 2053, 1902, 1890, 2057, 1995, 2121, 2186, 2091, 1904, 1820, 1638, 1479, 1433, 1509, 1378, 1467, 1110, 1088, 1143, 1247, 1320, 1446, 1645, 1693, 1612, 1627, 1907, 2099, 2295, 2199, 2211, 1970, 1659, 1957, 1835, 1962, 1863, 1972, 1750, 1112, 938, 1074, 1097, 1037, 1169, 1316, 1531, 1553, 1405, 1215, 1149, 1041, 1139, 1225, 1371, 1413, 1541, 1579, 1534, 1505, 1293, 1382, 1398, 1307, 1292, 1185, 1075, 917, 930, 950, 1048, 1071, 918, 867, 814, 860, 670, 663, 683, 618, 551, 400, 419, 422, 396, 416, 445, 367, 377, 369, 399, 445, 516, 537, 493, 460, 473, 455, 473, 425, 526, 596, 871, 1285, 418, 215, 220, 222, 218, 204, 223, 192,
    238, 228, 208, 200, 246, 956, 2931, 2363, 1874, 1742, 2110, 2257, 2155, 2012, 2050, 1914, 1849, 1707, 1523, 1548, 1372, 1447, 1357, 1293, 1061, 1100, 1212, 1337, 1473, 1752, 1668, 1566, 1539, 1655, 2006, 2315, 2097, 2293, 1995, 1961, 1985, 1746, 2038, 2092, 1902, 1189, 1057, 1035, 1083, 974, 1018, 1121, 1264, 1433, 1502, 1508, 1336, 1112, 969, 994, 1206, 1225, 1314, 1384, 1544, 1580, 1453, 1430, 1439, 1381, 1306, 1322, 1148, 1056, 891, 811, 889, 1087, 960, 804, 839, 773, 772, 636, 596, 517, 494, 480, 443, 412, 393, 386, 450, 594, 441, 450, 423, 413, 477, 491, 514, 511, 436, 468, 454, 462, 415, 473, 615, 795, 1191, 566, 244, 211, 204, 245, 209, 218, 191,
    239, 198, 201, 216, 247, 735, 2961, 2473, 1936, 1991, 2168, 2318, 2209, 1983, 2018, 1999, 1737, 1508, 1523, 1644, 1496, 1420, 1319, 1247, 1062, 1145, 1203, 1378, 1786, 1824, 1455, 1454, 1622, 1730, 1854, 2138, 2259, 2208, 1839, 1918, 1935, 1683, 1921, 1964, 1406, 998, 928, 961, 1207, 1046, 1014, 1241, 1286, 1465, 1512, 1376, 1291, 1028, 888, 957, 1119, 1126, 1287, 1442, 1623, 1601, 1453, 1408, 1378, 1288, 1222, 1251, 1182, 950, 861, 651, 819, 891, 797, 760, 748, 621, 573, 522, 482, 450, 488, 424, 426, 433, 415, 429, 451, 566, 449, 414, 455, 484, 555, 579, 529, 503, 414, 479, 457, 487, 478, 560, 592, 804, 1163, 414, 220, 231, 208, 209, 203, 218, 200,
    202, 196, 190, 199, 235, 558, 2644, 2509, 1965, 2024, 2131, 2308, 2165, 2120, 2055, 1962, 1763, 1576, 1538, 1609, 1475, 1318, 1347, 1222, 1328, 1354, 1367, 1287, 1603, 1631, 1475, 1435, 1677, 1871, 1986, 2316, 2359, 2002, 2044, 1852, 1868, 1735, 1764, 1714, 1288, 1010, 908, 1078, 1223, 1111, 1080, 1220, 1276, 1423, 1613, 1361, 1355, 998, 853, 1034, 969, 1029, 1298, 1511, 1637, 1592, 1536, 1551, 1297, 1291, 1168, 1114, 1116, 1057, 801, 778, 754, 712, 726, 631, 547, 631, 568, 492, 495, 501, 467, 482, 500, 507, 451, 427, 473, 544, 602, 432, 471, 512, 482, 555, 469, 475, 482, 468, 428, 487, 447, 447, 557, 914, 1227, 385, 221, 191, 205, 229, 204, 222, 194,
    214, 207, 212, 213, 191, 307, 1746, 2981, 2185, 1916, 2031, 2324, 2127, 1988, 1906, 1875, 1875, 1662, 1465, 1609, 1467, 1367, 1402, 1445, 1455, 1579, 1373, 1416, 1486, 1343, 1457, 1336, 1681, 1798, 1890, 2297, 2139, 1792, 1840, 1890, 1903, 1658, 1627, 1521, 1265, 1137, 994, 1128, 1081, 1032, 996, 1162, 1248, 1335, 1463, 1399, 1489, 1210, 979, 961, 905, 966, 1180, 1451, 1564, 1504, 1629, 1586, 1477, 1354, 1160, 1162, 992, 1048, 838, 782, 745, 799, 715, 648, 546, 538, 482, 480, 469, 534, 537, 526, 447, 483, 452, 399, 609, 598, 583, 510, 454, 444, 475, 565, 555, 479, 419, 420, 448, 448, 448, 483, 616, 837, 1233, 411, 211, 205, 221, 218, 206, 213, 202,
    236, 224, 233, 228, 197, 272, 1378, 3138, 2363, 1973, 2113, 2274, 2082, 1927, 2017, 1923, 1772, 1673, 1516, 1504, 1490, 1422, 1458, 1527, 1601, 1624, 1543, 1424, 1464, 1527, 1336, 1516, 1676, 1723, 1836, 2150, 1966, 1595, 1569, 1901, 1694, 1629, 1457, 1472, 1206, 976, 986, 1064, 1008, 868, 1009, 1155, 1187, 1393, 1519, 1452, 1466, 1277, 1161, 1051, 1044, 1080, 1364, 1586, 1640, 1491, 1641, 1612, 1399, 1240, 1146, 1098, 961, 1011, 833, 748, 636, 762, 711, 620, 610, 527, 525, 522, 504, 564, 757, 504, 425, 478, 436, 432, 513, 457, 450, 429, 461, 402, 496, 518, 509, 409, 462, 448, 446, 485, 468, 493, 589, 882, 1119, 364, 214, 196, 194, 208, 209, 205, 225,
    213, 200, 217, 204, 229, 242, 883, 3024, 2298, 1959, 2093, 2281, 2077, 1882, 1958, 1908, 1712, 1718, 1637, 1510, 1460, 1328, 1430, 1650, 1654, 1500, 1333, 1465, 1577, 1479, 1481, 1696, 1641, 1687, 1847, 2018, 1530, 1403, 1461, 1588, 1546, 1449, 1380, 1405, 1143, 1057, 1105, 1061, 802, 894, 1016, 1057, 1168, 1281, 1438, 1419, 1280, 1038, 1084, 1167, 1148, 1246, 1406, 1532, 1619, 1460, 1477, 1552, 1301, 1242, 1117, 1070, 949, 1036, 790, 741, 709, 815, 676, 615, 571, 615, 476, 470, 499, 515, 486, 491, 434, 477, 467, 470, 422, 462, 453, 546, 479, 419, 449, 494, 452, 482, 455, 451, 430, 474, 469, 504, 722, 985, 1048, 315, 216, 203, 211, 198, 221, 203, 211,
    199, 190, 209, 238, 203, 235, 688, 2792, 2517, 1965, 1950, 2198, 2097, 1898, 2004, 1808, 1701, 1630, 1599, 1436, 1370, 1289, 1275, 1769, 1700, 1464, 1308, 1554, 1427, 1573, 1654, 1749, 1589, 1609, 1814, 1641, 1437, 1363, 1430, 1409, 1423, 1455, 1231, 1368, 1148, 1157, 1069, 920, 699, 723, 923, 1192, 1097, 1337, 1471, 1302, 1264, 971, 862, 1167, 1203, 1180, 1390, 1531, 1463, 1403, 1361, 1545, 1318, 1164, 1201, 962, 971, 957, 789, 684, 691, 834, 725, 596, 618, 507, 542, 449, 543, 645, 609, 480, 438, 463, 545, 548, 507, 469, 547, 631, 511, 452, 493, 605, 477, 462, 452, 442, 412, 439, 460, 543, 707, 1018, 939, 305, 231, 205, 222, 191, 204, 179, 222,
    184, 210, 209, 208, 212, 229, 496, 2507, 2709, 2032, 1897, 2177, 2044, 1921, 1875, 1832, 1754, 1641, 1564, 1422, 1413, 1252, 1402, 1815, 1582, 1480, 1512, 1528, 1507, 1598, 1672, 1583, 1493, 1485, 1642, 1497, 1445, 1321, 1351, 1339, 1301, 1164, 1160, 1184, 1041, 1042, 837, 840, 838, 761, 1081, 1284, 1294, 1455, 1531, 1455, 1298, 986, 908, 1050, 1169, 1199, 1348, 1411, 1400, 1366, 1451, 1504, 1282, 1200, 1172, 996, 1036, 950, 846, 751, 719, 875, 590, 566, 577, 530, 441, 513, 566, 1051, 678, 524, 446, 559, 599, 473, 486, 519, 481, 548, 405, 446, 498, 534, 466, 419, 400, 402, 431, 446, 468, 553, 760, 1154, 791, 265, 227, 188, 212, 191, 209, 201, 204,
    218, 199, 185, 210, 214, 195, 270, 1374, 2918, 2267, 1933, 2145, 2015, 1908, 1884, 1820, 1572, 1573, 1590, 1468, 1432, 1337, 1403, 1895, 1618, 1589, 1597, 1715, 1613, 1770, 1615, 1457, 1485, 1556, 1572, 1346, 1347, 1280, 1230, 1194, 1207, 1031, 985, 1057, 1097, 819, 828, 829, 868, 843, 997, 1197, 1393, 1321, 1353, 1318, 1255, 1059, 920, 993, 1123, 1207, 1291, 1229, 1312, 1274, 1391, 1569, 1355, 1125, 1220, 1012, 990, 981, 882, 767, 746, 838, 726, 632, 520, 597, 557, 493, 464, 564, 487, 448, 510, 492, 474, 552, 409, 404, 430, 490, 415, 446, 620, 562, 440, 440, 422, 453, 424, 416, 462, 573, 748, 1098, 906, 269, 199, 217, 216, 190, 214, 216, 235,
    194, 226, 213, 207, 213, 233, 273, 1155, 2946, 2427, 2039, 2188, 2126, 1865, 1737, 1685, 1554, 1547, 1476, 1464, 1438, 1389, 1475, 1671, 1645, 1732, 1783, 1676, 2004, 1688, 1666, 1496, 1523, 1502, 1377, 1297, 1273, 1283, 1159, 1144, 941, 935, 833, 907, 824, 755, 715, 810, 877, 965, 1086, 1225, 1356, 1427, 1302, 1304, 1270, 1210, 920, 1027, 1090, 1126, 1247, 1301, 1245, 1321, 1319, 1402, 1266, 1211, 1025, 904, 997, 1025, 764, 851, 834, 764, 670, 585, 547, 541, 480, 484, 544, 482, 486, 469, 528, 505, 526, 520, 446, 480, 537, 444, 495, 571, 559, 460, 457, 401, 399, 452, 439, 445, 469, 603, 856, 1254, 609, 256, 208, 190, 223, 188, 211, 224, 182,
    219, 187, 213, 180, 206, 258, 225, 518, 2515, 2796, 1990, 2155, 2253, 1828, 1752, 1720, 1751, 1506, 1419, 1437, 1356, 1398, 1371, 1597, 1452, 1599, 1729, 1814, 1752, 1704, 1577, 1510, 1569, 1410, 1255, 1225, 1263, 1232, 1151, 1152, 1043, 897, 841, 884, 861, 907, 860, 1005, 927, 982, 1145, 1230, 1324, 1225, 1294, 1197, 1309, 1209, 954, 1005, 1096, 1067, 1140, 1276, 1324, 1418, 1392, 1463, 1262, 1199, 1078, 904, 1036, 971, 848, 788, 804, 768, 684, 598, 526, 560, 540, 564, 520, 511, 536, 449, 521, 477, 508, 526, 441, 709, 568, 530, 651, 641, 483, 513, 406, 448, 417, 459, 441, 413, 478, 594, 805, 1152, 485, 208, 237, 216, 212, 223, 198, 232, 212,
    216, 229, 177, 200, 195, 215, 237, 312, 1603, 2932, 2263, 2086, 2323, 1998, 1633, 1613, 1723, 1588, 1358, 1295, 1351, 1423, 1271, 1411, 1480, 1542, 1711, 1886, 1741, 1523, 1508, 1498, 1542, 1434, 1320, 1301, 1239, 1208, 1099, 1028, 937, 879, 857, 931, 1048, 1040, 1147, 1132, 1140, 1076, 1387, 1452, 1398, 1204, 1227, 1205, 1110, 987, 933, 957, 1161, 984, 1245, 1254, 1304, 1322, 1388, 1306, 1257, 1218, 978, 953, 1041, 983, 763, 783, 802, 777, 643, 497, 493, 522, 550, 600, 489, 509, 457, 488, 518, 498, 452, 433, 484, 525, 483, 575, 613, 564, 502, 390, 446, 412, 410, 448, 469, 411, 487, 622, 851, 1085, 348, 211, 221, 213, 205, 193, 212, 208, 217,
    226, 226, 214, 202, 173, 198, 204, 237, 753, 2643, 2526, 2089, 2295, 2006, 1658, 1610, 1618, 1538, 1485, 1364, 1305, 1371, 1163, 1337, 1472, 1484, 1709, 1849, 1670, 1477, 1386, 1433, 1416, 1468, 1449, 1441, 1396, 1270, 1058, 1051, 929, 948, 882, 976, 1002, 1106, 1212, 1234, 1307, 1301, 1400, 1338, 1227, 1106, 1170, 1043, 1052, 961, 890, 918, 969, 1043, 1220, 1310, 1238, 1326, 1219, 1341, 1281, 1220, 935, 933, 972, 962, 812, 786, 841, 834, 661, 534, 593, 607, 593, 569, 475, 530, 463, 469, 507, 472, 492, 473, 473, 457, 464, 631, 593, 575, 452, 469, 438, 401, 404, 432, 395, 391, 492, 576, 788, 1008, 334, 251, 215, 223, 212, 196, 207, 218, 197,
    212, 204, 219, 191, 208, 193, 230, 217, 442, 2109, 2907, 2155, 2408, 2036, 1703, 1600, 1606, 1574, 1502, 1437, 1365, 1220, 989, 1245, 1425, 1377, 1741, 1818, 1614, 1367, 1459, 1434, 1342, 1460, 1465, 1364, 1408, 1251, 1227, 1191, 1099, 980, 912, 1077, 1115, 1180, 1189, 1232, 1333, 1539, 1386, 1367, 1321, 1038, 1113, 1015, 1080, 911, 842, 869, 1052, 1094, 1208, 1347, 1209, 1201, 1262, 1265, 1226, 1194, 891, 902, 951, 908, 722, 692, 776, 809, 667, 660, 705, 599, 538, 554, 524, 523, 524, 492, 486, 459, 529, 503, 499, 410, 475, 536, 521, 537, 465, 387, 383, 436, 460, 429, 421, 418, 417, 614, 915, 919, 239, 212, 201, 218, 206, 204, 225, 200, 212,
    213, 199, 212, 194, 193, 212, 191, 198, 266, 1403, 2895, 2567, 2316, 2321, 1811, 1601, 1638, 1694, 1562, 1431, 1341, 1273, 1249, 1362, 1414, 1487, 1766, 1861, 1553, 1500, 1595, 1484, 1340, 1349, 1380, 1360, 1373, 1303, 1222, 1115, 1064, 1037, 950, 963, 1118, 1112, 1120, 1162, 1373, 1392, 1361, 1369, 1165, 1072, 1088, 1093, 1026, 909, 856, 858, 976, 1078, 1145, 1261, 1244, 1236, 1325, 1436, 1380, 1145, 979, 834, 956, 876, 776, 813, 758, 699, 662, 650, 686, 583, 569, 506, 492, 497, 555, 440, 479, 501, 502, 540, 424, 492, 512, 545, 531, 568, 471, 434, 397, 447, 407, 462, 448, 472, 513, 679, 1015, 697, 211, 212, 218, 219, 175, 226, 188, 210, 211,
    223, 226, 231, 230, 226, 220, 209, 205, 222, 693, 2270, 2790, 2517, 2274, 1840, 1519, 1634, 1579, 1497, 1404, 1317, 1200, 1194, 1249, 1444, 1458, 1645, 1673, 1368, 1496, 1532, 1447, 1389, 1209, 1283, 1332, 1435, 1483, 1227, 1182, 1188, 1064, 968, 987, 1090, 1130, 1183, 1247, 1421, 1371, 1166, 1047, 1056, 931, 886, 964, 1051, 974, 880, 882, 1001, 967, 1122, 1159, 1301, 1249, 1267, 1334, 1370, 1112, 961, 874, 908, 920, 823, 761, 770, 767, 749, 601, 569, 574, 498, 563, 462, 512, 522, 442, 481, 469, 428, 409, 512, 464, 450, 487, 442, 469, 457, 415, 384, 422, 439, 466, 446, 423, 546, 642, 995, 663, 239, 209, 227, 217, 215, 207, 199, 221, 196,
    216, 199, 204, 224, 207, 217, 181, 201, 210, 392, 1822, 2904, 2628, 2281, 1813, 1587, 1567, 1546, 1552, 1416, 1307, 1302, 1302, 1305, 1391, 1327, 1544, 1399, 1383, 1355, 1404, 1421, 1358, 1278, 1292, 1329, 1458, 1236, 1224, 1061, 1118, 1151, 1222, 1378, 1347, 1266, 1255, 1424, 1323, 1088, 996, 911, 913, 910, 831, 981, 1077, 1002, 910, 869, 1078, 1100, 1067, 1172, 1231, 1283, 1328, 1365, 1249, 1147, 902, 916, 1034, 942, 877, 769, 745, 794, 708, 584, 533, 515, 507, 475, 501, 495, 466, 502, 454, 479, 455, 506, 471, 474, 512, 582, 622, 564, 450, 423, 410, 418, 432, 511, 485, 498, 570, 748, 1016, 387, 227, 174, 214, 198, 239, 213, 205, 178, 205,
    198, 198, 220, 203, 196, 205, 202, 223, 203, 308, 1217, 2571, 2865, 2647, 1919, 1609, 1503, 1667, 1489, 1565, 1426, 1280, 1304, 1290, 1372, 1411, 1402, 1345, 1303, 1385, 1321, 1486, 1348, 1343, 1287, 1332, 1310, 1252, 1193, 1133, 1180, 1171, 1202, 1396, 1332, 1274, 1258, 1217, 991, 939, 861, 904, 755, 820, 875, 920, 976, 932, 890, 907, 1038, 1117, 1158, 1167, 1233, 1331, 1340, 1341, 1274, 1170, 964, 933, 1062, 1000, 800, 755, 793, 782, 740, 561, 557, 521, 484, 476, 484, 471, 579, 595, 477, 472, 474, 418, 508, 493, 492, 530, 540, 445, 424, 444, 431, 478, 405, 521, 555, 559, 661, 864, 955, 306, 198, 209, 204, 184, 222, 191, 201, 201, 204,
    211, 234, 178, 198, 212, 201, 225, 202, 237, 237, 492, 1916, 2798, 2868, 2264, 1671, 1532, 1655, 1605, 1414, 1488, 1336, 1303, 1271, 1278, 1368, 1322, 1395, 1339, 1278, 1322, 1230, 1188, 1436, 1356, 1341, 1315, 1266, 1138, 1164, 1180, 1129, 1082, 1144, 1225, 1092, 1118, 1067, 990, 919, 889, 814, 765, 844, 795, 867, 829, 816, 867, 843, 1002, 1062, 1031, 1130, 1172, 1193, 1313, 1282, 1356, 1179, 935, 909, 955, 1003, 832, 745, 763, 763, 701, 632, 538, 553, 572, 514, 485, 456, 514, 524, 474, 452, 499, 452, 496, 491, 506, 557, 457, 430, 424, 389, 466, 464, 408, 491, 519, 584, 689, 940, 915, 259, 216, 183, 192, 212, 226, 200, 186, 224, 196,
    203, 210, 203, 176, 218, 214, 248, 255, 258, 297, 387, 1308, 2228, 3077, 2608, 1870, 1495, 1624, 1605, 1492, 1529, 1497, 1412, 1071, 1244, 1321, 1346, 1386, 1240, 1244, 1190, 1150, 1219, 1350, 1334, 1344, 1245, 1295, 1253, 1176, 1166, 1146, 1102, 1073, 1195, 1101, 1150, 1125, 926, 924, 929, 803, 817, 796, 806, 833, 832, 859, 845, 920, 950, 1121, 1085, 1200, 1237, 1366, 1208, 1186, 1346, 1282, 980, 913, 925, 967, 877, 824, 714, 781, 672, 585, 557, 550, 495, 489, 522, 479, 389, 468, 447, 496, 489, 530, 505, 510, 513, 594, 439, 381, 448, 405, 413, 435, 472, 479, 518, 611, 725, 927, 865, 287, 205, 200, 207, 188, 211, 223, 231, 216, 211,
    200, 209, 216, 219, 255, 384, 711, 1236, 1968, 2087, 1856, 1871, 2937, 4204, 3945, 2336, 1740, 1685, 1632, 1570, 1511, 1483, 1458, 1177, 1189, 1240, 1435, 1408, 1294, 1202, 1225, 1296, 1338, 1304, 1285, 1252, 1237, 1198, 1150, 1125, 1207, 1086, 1115, 1204, 1145, 1034, 1139, 1101, 1029, 958, 881, 764, 809, 823, 797, 844, 874, 873, 889, 911, 1010, 1002, 1031, 1194, 1328, 1297, 1285, 1309, 1356, 1138, 924, 941, 983, 878, 757, 764, 735, 675, 622, 601, 527, 580, 531, 551, 527, 465, 426, 494, 471, 485, 498, 540, 497, 556, 551, 475, 468, 470, 453, 445, 437, 416, 441, 467, 498, 544, 634, 904, 358, 192, 196, 189, 208, 203, 206, 194, 210, 246, 187,
    218, 204, 224, 490, 1336, 2137, 2027, 1360, 1218, 1079, 775, 607, 1308, 2634, 4279, 3956, 2924, 2865, 2857, 2317, 1903, 1687, 1579, 1343, 1034, 1264, 1347, 1403, 1273, 1300, 1159, 1230, 1290, 1339, 1224, 1209, 1237, 1165, 1159, 1210, 1180, 1222, 1232, 1152, 1210, 1080, 1107, 1220, 1292, 1062, 819, 856, 899, 831, 808, 867, 869, 777, 929, 960, 947, 1013, 1065, 1121, 1226, 1234, 1310, 1249, 1285, 1145, 905, 797, 954, 854, 811, 764, 724, 680, 718, 542, 509, 553, 541, 492, 511, 513, 495, 527, 439, 496, 485, 517, 528, 437, 486, 511, 474, 494, 463, 446, 443, 450, 426, 433, 481, 485, 551, 482, 246, 201, 208, 181, 183, 213, 185, 203, 203, 212, 209,
    207, 247, 909, 1809, 1255, 952, 798, 854, 793, 648, 542, 389, 658, 2384, 3653, 4136, 2766, 2262, 2125, 2065, 2244, 2244, 2229, 2045, 1587, 1340, 1554, 1570, 1362, 1311, 1173, 1306, 1369, 1311, 1186, 1264, 1110, 1204, 1137, 1101, 1228, 1221, 1222, 1247, 1213, 1142, 1335, 1186, 1135, 1124, 980, 927, 889, 865, 841, 863, 864, 842, 827, 960, 941, 1059, 1081, 1096, 1158, 1190, 1193, 1293, 1399, 1096, 879, 854, 987, 940, 875, 749, 697, 691, 646, 585, 514, 568, 557, 518, 481, 515, 563, 470, 528, 561, 577, 562, 564, 482, 503, 572, 497, 404, 429, 438, 376, 395, 418, 453, 563, 520, 674, 598, 260, 177, 212, 188, 227, 197, 189, 219, 198, 190, 187,
    299, 835, 1027, 822, 525, 397, 337, 288, 302, 247, 245, 295, 762, 1715, 3255, 4113, 3342, 2343, 2053, 1823, 1867, 1956, 1936, 1792, 1649, 1511, 1743, 2046, 1935, 1703, 1654, 1618, 1544, 1425, 1407, 1333, 1142, 1155, 1168, 1149, 1102, 1064, 1209, 1284, 1130, 1165, 1113, 1117, 1116, 1101, 1007, 970, 942, 966, 986, 963, 896, 841, 839, 883, 885, 1045, 1066, 1101, 1172, 1277, 1234, 1217, 1322, 1139, 907, 867, 900, 1017, 794, 713, 647, 706, 616, 533, 603, 537, 486, 520, 560, 618, 640, 697, 728, 654, 744, 702, 683, 633, 525, 568, 477, 390, 420, 410, 350, 382, 387, 397, 502, 566, 695, 677, 266, 203, 207, 223, 203, 217, 171, 217, 210, 192, 195,
    755, 522, 335, 253, 255, 214, 257, 216, 230, 229, 243, 543, 1025, 1447, 2843, 3592, 3671, 2647, 2032, 1726, 1775, 1833, 1883, 1885, 1809, 1568, 1579, 1866, 1688, 1763, 1681, 1607, 1567, 1479, 1439, 1366, 1275, 1412, 1352, 1211, 1086, 1075, 1118, 1064, 1029, 994, 1090, 1153, 1102, 1057, 1024, 928, 1012, 1027, 1054, 992, 842, 859, 850, 877, 1009, 1042, 1142, 1114, 1228, 1369, 1319, 1208, 1326, 1114, 865, 790, 928, 1053, 780, 739, 700, 737, 664, 534, 525, 552, 603, 694, 701, 786, 842, 789, 843, 863, 743, 732, 686, 650, 620, 507, 408, 448, 368, 337, 339, 393, 373, 415, 427, 500, 658, 417, 218, 201, 208, 206, 220, 220, 223, 209, 216, 166, 222,
    283, 240, 210, 204, 214, 190, 235, 200, 190, 240, 324, 1101, 1232, 1299, 1729, 2845, 3699, 3183, 2209, 1794, 1733, 1725, 1786, 1795, 1691, 1717, 1736, 1801, 1734, 1724, 1665, 1605, 1508, 1339, 1398, 1273, 1177, 1205, 1412, 1295, 1205, 1123, 1065, 1138, 1011, 960, 998, 982, 1096, 1019, 963, 1007, 1001, 1110, 1152, 1078, 929, 810, 837, 790, 915, 1059, 1157, 1119, 1253, 1320, 1435, 1315, 1307, 1148, 901, 834, 900, 961, 730, 706, 732, 787, 630, 598, 523, 620, 700, 863, 868, 903, 912, 893, 953, 878, 896, 728, 693, 613, 670, 461, 407, 385, 370, 324, 342, 326, 367, 349, 432, 460, 630, 341, 202, 209, 214, 180, 212, 213, 215, 183, 194, 199, 196,
    191, 207, 200, 198, 202, 198, 222, 222, 204, 429, 1154, 1403, 1130, 980, 1056, 2106, 2993, 3633, 2475, 1976, 1680, 1656, 1788, 1801, 1825, 1742, 1851, 1814, 1716, 1822, 1685, 1431, 1298, 1202, 1287, 1311, 1246, 1195, 1259, 1149, 1176, 1139, 1258, 1148, 1101, 1054, 1024, 978, 1068, 1005, 1144, 924, 961, 1027, 1064, 1020, 973, 888, 857, 891, 1046, 1027, 1140, 1196, 1277, 1243, 1355, 1370, 1254, 1066, 952, 842, 895, 949, 822, 696, 788, 680, 656, 548, 655, 855, 952, 955, 1014, 1074, 1048, 1047, 998, 920, 822, 770, 669, 621, 645, 534, 415, 342, 338, 367, 341, 358, 354, 360, 364, 453, 522, 239, 213, 198, 210, 209, 216, 187, 219, 215, 216, 214, 241,
    210, 195, 205, 198, 194, 188, 200, 208, 235, 411, 889, 1726, 1049, 853, 691, 993, 2327, 3338, 3507, 2441, 1958, 1752, 1706, 1707, 1739, 1787, 1779, 1780, 1714, 1650, 1519, 1359, 1230, 1217, 1245, 1202, 1184, 1221, 1186, 1179, 1077, 1084, 1165, 1132, 1012, 970, 919, 929, 1000, 1036, 1049, 964, 882, 944, 1003, 1100, 914, 963, 973, 881, 889, 1049, 1045, 1234, 1348, 1237, 1318, 1453, 1310, 1209, 881, 909, 850, 908, 697, 721, 718, 679, 630, 601, 682, 968, 1332, 1159, 1112, 1145, 1123, 1165, 1075, 983, 966, 877, 697, 600, 547, 471, 385, 328, 411, 351, 381, 349, 348, 355, 342, 453, 497, 220, 212, 196, 208, 178, 211, 206, 218, 206, 207, 208, 194,
    186, 199, 203, 197, 208, 202, 187, 210, 193, 265, 496, 1497, 1289, 843, 716, 680, 1388, 2673, 3608, 3251, 2318, 2000, 1814, 1772, 1845, 1812, 1799, 1948, 1666, 1522, 1508, 1401, 1317, 1299, 1285, 1282, 1274, 1170, 1301, 1146, 1156, 1110, 1107, 1076, 1007, 927, 899, 926, 952, 977, 981, 934, 995, 955, 970, 887, 832, 933, 987, 923, 895, 895, 1078, 1257, 1349, 1229, 1315, 1256, 1301, 1293, 964, 768, 835, 923, 795, 700, 685, 692, 688, 544, 811, 1042, 1204, 1263, 1243, 1276, 1277, 1176, 1099, 1005, 935, 825, 716, 586, 515, 472, 344, 333, 333, 354, 356, 332, 354, 354, 344, 478, 332, 229, 219, 185, 201, 146, 182, 216, 200, 206, 177, 187, 217,
    180, 184, 226, 221, 208, 230, 199, 212, 226, 215, 287, 442, 938, 1218, 864, 735, 682, 1656, 2949, 3614, 3101, 2248, 1887, 1842, 1724, 1728, 1815, 1877, 1897, 1615, 1402, 1428, 1337, 1341, 1334, 1266, 1182, 1271, 1225, 1203, 1166, 1113, 1164, 1049, 1031, 885, 780, 942, 969, 929, 941, 1022, 1034, 998, 948, 943, 971, 952, 972, 925, 804, 926, 1023, 1220, 1285, 1293, 1277, 1276, 1210, 1338, 1018, 874, 864, 924, 804, 697, 734, 640, 541, 634, 862, 1072, 1254, 1231, 1247, 1289, 1224, 1105, 1091, 1001, 914, 835, 616, 575, 510, 432, 375, 332, 313, 328, 351, 317, 338, 377, 395, 473, 331, 210, 205, 186, 181, 224, 229, 209, 194, 187, 232, 195, 205,
    199, 194, 223, 216, 225, 200, 206, 213, 216, 211, 216, 262, 375, 696, 1236, 1160, 827, 1119, 2456, 3284, 3507, 2760, 2231, 1997, 1672, 1623, 1652, 1726, 1718, 1704, 1440, 1361, 1311, 1344, 1308, 1238, 1173, 1223, 1248, 1196, 1212, 1209, 1117, 1019, 774, 664, 778, 934, 967, 964, 957, 1001, 943, 883, 876, 923, 1089, 1045, 983, 924, 910, 956, 1071, 1167, 1271, 1221, 1217, 1192, 1229, 1251, 894, 826, 861, 832, 792, 684, 759, 662, 670, 867, 1142, 1345, 1284, 1255, 1227, 1090, 1061, 1069, 1094, 956, 894, 755, 656, 482, 481, 347, 361, 321, 324, 334, 302, 310, 370, 391, 404, 464, 232, 201, 192, 206, 200, 186, 202, 197, 195, 215, 217, 207, 222,
    221, 208, 210, 193, 214, 211, 200, 223, 192, 202, 216, 214, 240, 332, 378, 372, 300, 471, 1336, 2393, 3487, 3510, 2721, 2216, 1910, 1780, 1680, 1718, 1619, 1600, 1480, 1337, 1209, 1379, 1354, 1353, 1253, 1233, 1300, 1269, 1167, 1106, 1115, 1052, 936, 766, 744, 785, 894, 942, 972, 958, 917, 1011, 894, 854, 1021, 985, 963, 956, 959, 1028, 1000, 1150, 1276, 1236, 1146, 1140, 1314, 1332, 1014, 898, 803, 906, 770, 715, 747, 723, 683, 910, 1133, 1232, 1169, 1219, 1219, 1114, 1165, 1076, 993, 849, 756, 625, 589, 495, 435, 347, 303, 347, 322, 325, 298, 349, 342, 382, 425, 433, 215, 206, 199, 227, 206, 167, 187, 202, 186, 236, 192, 187, 213,
    218, 195, 191, 204, 212, 192, 197, 191, 233, 223, 211, 199, 202, 230, 238, 210, 207, 314, 521, 1750, 2824, 3841, 3125, 2366, 1991, 1702, 1614, 1485, 1474, 1371, 1479, 1423, 1380, 1383, 1437, 1377, 1408, 1411, 1360, 1264, 1263, 1285, 1214, 1088, 1041, 979, 950, 859, 893, 1003, 978, 909, 906, 902, 825, 841, 988, 956, 1000, 1033, 1000, 920, 971, 1081, 1101, 1222, 1136, 1184, 1184, 1181, 1051, 825, 872, 937, 781, 717, 685, 646, 618, 1025, 1191, 1284, 1170, 1084, 1129, 1141, 1084, 1087, 893, 843, 653, 701, 512, 404, 333, 315, 316, 348, 340, 350, 332, 365, 347, 394, 507, 315, 201, 209, 217, 225, 205, 214, 219, 192, 200, 220, 197, 204, 191,
    213, 239, 193, 190, 204, 216, 212, 192, 199, 214, 197, 208, 182, 207, 212, 210, 220, 200, 271, 663, 1826, 2979, 3830, 2923, 2258, 1817, 1700, 1548, 1285, 1276, 1335, 1394, 1501, 1396, 1426, 1438, 1452, 1499, 1605, 1550, 1389, 1403, 1113, 1208, 1177, 1185, 1122, 1035, 1115, 1089, 985, 908, 867, 820, 870, 933, 947, 1126, 1108, 1021, 948, 970, 1009, 998, 972, 1189, 1163, 1223, 1202, 1168, 1021, 840, 843, 902, 817, 721, 722, 675, 745, 941, 1139, 1227, 1290, 1178, 1061, 1026, 954, 985, 900, 685, 575, 509, 409, 392, 383, 319, 313, 294, 331, 329, 349, 353, 376, 424, 565, 294, 222, 210, 208, 219, 215, 221, 208, 221, 186, 188, 174, 204, 208,
    202, 201, 237, 213, 200, 201, 210, 218, 208, 220, 198, 195, 210, 195, 195, 213, 209, 229, 379, 485, 1075, 2262, 3294, 3772, 2727, 2185, 1766, 1610, 1268, 1228, 1273, 1206, 1284, 1492, 1423, 1457, 1365, 1469, 1728, 1681, 1427, 1398, 1455, 1371, 1187, 1143, 1190, 1118, 1088, 1067, 1014, 957, 903, 920, 946, 894, 990, 1145, 1118, 1009, 909, 948, 1063, 1161, 1010, 1037, 1202, 1183, 1265, 1301, 1046, 902, 793, 955, 797, 682, 690, 687, 692, 924, 1025, 1071, 1156, 1098, 889, 1078, 993, 971, 795, 615, 491, 436, 370, 362, 363, 296, 289, 339, 325, 308, 342, 342, 432, 491, 559, 229, 211, 226, 195, 179, 207, 198, 183, 181, 203, 211, 186, 212, 212,
    206, 210, 203, 209, 207, 234, 204, 205, 217, 197, 219, 209, 195, 211, 181, 220, 212, 203, 262, 426, 554, 1193, 2463, 3440, 3541, 2425, 1972, 1681, 1486, 1278, 1223, 1190, 1329, 1373, 1363, 1381, 1439, 1445, 1485, 1524, 1547, 1321, 1438, 1429, 1391, 1370, 1260, 1294, 1192, 1234, 957, 986, 991, 1002, 1055, 1018, 1083, 1084, 1028, 955, 981, 909, 1084, 1180, 1119, 1156, 1161, 1225, 1222, 1197, 1062, 836, 795, 891, 884, 732, 724, 729, 693, 715, 934, 970, 1040, 1090, 964, 983, 918, 926, 719, 574, 454, 449, 403, 363, 358, 352, 331, 343, 379, 364, 365, 415, 375, 552, 465, 240, 224, 181, 194, 212, 204, 189, 222, 186, 206, 192, 189, 199, 197,
    198, 240, 202, 190, 204, 194, 216, 193, 220, 217, 211, 191, 186, 211, 195, 235, 218, 210, 278, 366, 669, 783, 1588, 2789, 3865, 3000, 2192, 1787, 1548, 1382, 1249, 1305, 1246, 1270, 1321, 1324, 1406, 1477, 1568, 1442, 1463, 1422, 1311, 1414, 1378, 1391, 1439, 1313, 1237, 1234, 1171, 1012, 1028, 1049, 971, 1012, 1068, 1038, 988, 953, 877, 996, 1043, 1142, 1152, 1151, 1273, 1183, 1080, 1134, 1055, 881, 871, 968, 808, 713, 734, 722, 621, 671, 876, 952, 1110, 958, 842, 957, 943, 865, 673, 480, 414, 448, 340, 406, 390, 330, 331, 401, 372, 316, 384, 374, 465, 591, 306, 208, 213, 216, 186, 200, 207, 200, 223, 184, 180, 223, 213, 205, 196,
    186, 214, 221, 222, 202, 181, 192, 206, 194, 204, 204, 187, 183, 193, 215, 202, 209, 215, 214, 323, 612, 654, 815, 1687, 2999, 3826, 2858, 2077, 1628, 1473, 1313, 1476, 1430, 1302, 1316, 1432, 1431, 1535, 1567, 1610, 1658, 1460, 1448, 1198, 1269, 1297, 1449, 1400, 1266, 1159, 1182, 1132, 1168, 1174, 1212, 1076, 1051, 1005, 1054, 975, 998, 1055, 1010, 1105, 1058, 1219, 1183, 1169, 1082, 1099, 1060, 895, 836, 942, 782, 712, 698, 705, 591, 579, 629, 877, 969, 1014, 908, 892, 748, 665, 498, 471, 430, 428, 377, 412, 373, 368, 394, 395, 399, 404, 421, 428, 516, 588, 237, 202, 202, 202, 197, 210, 208, 184, 202, 212, 178, 216, 214, 216, 192,
    207, 224, 211, 198, 221, 212, 180, 198, 213, 200, 212, 176, 181, 211, 192, 222, 214, 197, 241, 293, 355, 736, 682, 803, 1545, 2867, 3795, 2779, 1919, 1540, 1420, 1387, 1573, 1507, 1385, 1385, 1333, 1391, 1425, 1448, 1454, 1384, 1360, 1275, 1217, 1302, 1320, 1327, 1361, 1246, 1269, 1248, 1271, 1164, 1254, 1120, 1027, 961, 1080, 1064, 990, 1002, 1078, 1198, 1164, 1206, 1187, 1205, 1110, 1171, 1001, 966, 876, 1004, 890, 732, 685, 657, 618, 627, 592, 623, 668, 785, 900, 777, 642, 527, 455, 456, 443, 424, 399, 399, 367, 353, 461, 428, 402, 403, 438, 417, 558, 710, 303, 218, 185, 211, 217, 183, 226, 203, 204, 202, 187, 181, 227, 193, 182,
    189, 202, 186, 204, 200, 191, 197, 196, 216, 215, 196, 221, 212, 196, 190, 180, 184, 207, 198, 243, 387, 607, 790, 627, 928, 2080, 3269, 3381, 2235, 1727, 1628, 1495, 1511, 1616, 1546, 1424, 1328, 1371, 1311, 1350, 1419, 1384, 1427, 1408, 1290, 1278, 1371, 1274, 1197, 1276, 1274, 1246, 1092, 1053, 1132, 1069, 966, 988, 954, 1032, 1004, 1108, 1193, 1145, 1140, 1212, 1102, 1172, 1103, 1068, 1056, 945, 824, 998, 880, 840, 686, 628, 603, 531, 580, 549, 556, 630, 666, 674, 528, 424, 457, 435, 480, 447, 402, 399, 373, 427, 398, 472, 490, 469, 472, 504, 740, 590, 251, 193, 195, 222, 176, 210, 193, 187, 224, 177, 204, 207, 200, 219, 218,
    198, 210, 233, 205, 215, 199, 208, 225, 203, 194, 217, 201, 216, 212, 199, 197, 220, 214, 242, 232, 282, 501, 928, 679, 637, 1079, 2529, 3498, 2943, 1939, 1663, 1498, 1599, 1593, 1692, 1568, 1459, 1389, 1430, 1321, 1305, 1728, 2614, 1400, 1335, 1298, 1383, 1212, 1272, 1302, 1285, 1284, 1237, 1137, 1071, 1104, 1202, 1063, 990, 1081, 1149, 1199, 1093, 1166, 1051, 1099, 1139, 1173, 1091, 1060, 1054, 895, 928, 961, 860, 738, 653, 653, 616, 655, 580, 587, 604, 557, 539, 480, 478, 467, 418, 450, 402, 472, 419, 399, 423, 455, 468, 511, 512, 479, 517, 569, 893, 319, 233, 209, 205, 195, 213, 209, 202, 197, 227, 205, 204, 209, 220, 196, 221,
    191, 201, 201, 229, 177, 219, 226, 197, 204, 186, 215, 186, 222, 211, 196, 196, 191, 211, 208, 217, 245, 383, 731, 840, 779, 692, 1081, 2446, 3473, 2943, 2101, 1781, 1652, 1653, 1636, 1700, 1669, 1502, 1503, 1313, 1292, 1423, 1424, 1390, 1259, 1303, 1362, 1268, 1329, 1275, 1275, 1301, 1256, 1218, 1214, 1098, 1134, 1107, 1077, 1035, 1159, 1101, 1166, 1056, 1087, 1037, 1163, 1117, 1033, 965, 996, 951, 920, 923, 926, 707, 655, 599, 622, 622, 584, 666, 572, 506, 522, 485, 508, 494, 527, 473, 419, 506, 409, 408, 421, 448, 472, 522, 529, 540, 518, 628, 825, 333, 208, 208, 202, 204, 216, 203, 187, 185, 198, 170, 234, 168, 223, 221, 200,
    223, 194, 209, 201, 194, 183, 190, 215, 200, 174, 203, 199, 200, 201, 190, 201, 197, 200, 184, 204, 210, 300, 439, 856, 968, 822, 752, 1300, 2585, 3396, 2863, 1997, 1732, 1722, 1673, 1712, 1628, 1632, 1491, 1461, 1408, 1465, 1557, 1396, 1381, 1213, 1246, 1387, 1382, 1294, 1210, 1228, 1257, 1286, 1129, 1189, 1121, 1064, 1047, 1107, 1037, 1123, 1189, 1091, 1092, 1122, 1080, 1068, 1034, 1016, 957, 933, 847, 965, 988, 830, 650, 648, 592, 619, 614, 546, 599, 482, 570, 508, 421, 429, 527, 516, 473, 448, 452, 421, 394, 447, 496, 554, 588, 548, 535, 715, 807, 240, 224, 211, 214, 211, 193, 178, 189, 194, 204, 212, 223, 205, 200, 201, 177,
    215, 202, 230, 206, 215, 222, 205, 201, 213, 176, 189, 207, 205, 206, 188, 205, 198, 219, 236, 195, 212, 211, 435, 565, 909, 1115, 999, 876, 1543, 2567, 3448, 2825, 1973, 1822, 1650, 1715, 1610, 1638, 1608, 1372, 1535, 1548, 1452, 1299, 1331, 1239, 1385, 1336, 1281, 1259, 1261, 1286, 1284, 1235, 1167, 1121, 1120, 1118, 1108, 1009, 1236, 1117, 1062, 1038, 1057, 1102, 1010, 1002, 966, 1027, 1034, 971, 940, 989, 1033, 790, 615, 588, 615, 598, 602, 590, 547, 614, 492, 502, 476, 541, 507, 518, 462, 464, 471, 495, 443, 534, 520, 538, 534, 554, 541, 891, 525, 236, 218, 175, 198, 219, 216, 219, 202, 203, 182, 211, 210, 207, 194, 172, 203,
    216, 190, 207, 217, 235, 194, 196, 192, 211, 203, 203, 208, 197, 187, 188, 193, 188, 216, 217, 178, 184, 210, 242, 379, 487, 896, 824, 759, 699, 1276, 2439, 3421, 2824, 1914, 1760, 1791, 1699, 1711, 1648, 1663, 1580, 1526, 1574, 1383, 1453, 1490, 1386, 1284, 1293, 1129, 1120, 1281, 1286, 1179, 1035, 1093, 1160, 1188, 1189, 1151, 1127, 1169, 1094, 1042, 1242, 1146, 946, 945, 957, 978, 1073, 973, 863, 954, 993, 799, 684, 659, 601, 662, 610, 564, 616, 604, 548, 553, 498, 485, 495, 502, 495, 481, 481, 497, 517, 595, 587, 586, 584, 619, 623, 952, 393, 189, 218, 212, 207, 186, 181, 216, 192, 188, 195, 203, 203, 193, 203, 198, 178,
    202, 234, 198, 204, 205, 189, 229, 190, 208, 187, 202, 216, 224, 200, 191, 202, 192, 201, 233, 216, 212, 187, 187, 233, 316, 486, 361, 411, 485, 758, 1517, 2504, 3308, 2743, 1967, 1809, 1734, 1656, 1732, 1736, 1663, 1569, 1576, 1700, 1735, 2176, 1491, 1346, 1263, 1260, 1150, 1282, 1246, 1107, 1207, 1122, 1073, 1245, 1260, 1229, 1378, 2080, 1285, 1208, 1221, 1013, 915, 838, 898, 960, 965, 928, 897, 954, 997, 835, 736, 698, 650, 644, 604, 692, 636, 608, 597, 549, 535, 538, 525, 498, 522, 442, 531, 525, 558, 626, 598, 601, 555, 576, 680, 911, 329, 197, 197, 198, 189, 201, 206, 199, 180, 212, 203, 192, 204, 198, 207, 189, 216,
    225, 205, 173, 210, 199, 200, 223, 210, 201, 199, 231, 203, 212, 182, 206, 218, 208, 211, 187, 202, 213, 208, 217, 213, 238, 254, 265, 231, 348, 665, 928, 1417, 2615, 3304, 2707, 1934, 1835, 1757, 1721, 1813, 1840, 1701, 1649, 1727, 2023, 1644, 1336, 1367, 1351, 1271, 1135, 1230, 1167, 1246, 1252, 1213, 1130, 1169, 1150, 1107, 1092, 1131, 1107, 1001, 1017, 1008, 829, 835, 903, 848, 946, 956, 974, 986, 959, 879, 788, 720, 712, 803, 808, 675, 681, 645, 555, 566, 547, 515, 535, 482, 498, 514, 524, 572, 598, 668, 655, 611, 638, 593, 736, 857, 308, 210, 228, 189, 194, 194, 153, 182, 194, 192, 222, 191, 177, 201, 191, 198, 202,
    190, 195, 200, 215, 209, 188, 222, 183, 201, 218, 189, 195, 178, 223, 201, 219, 198, 204, 197, 204, 213, 184, 192, 205, 197, 190, 189, 202, 256, 459, 903, 989, 1612, 2490, 3246, 2760, 1973, 1777, 1814, 1750, 1711, 1776, 1726, 1787, 2322, 1832, 1471, 1473, 1372, 1342, 1399, 1483, 1381, 1245, 1251, 1249, 1126, 1197, 1048, 1101, 1482, 1293, 1078, 968, 946, 854, 850, 855, 858, 915, 933, 911, 942, 1017, 959, 892, 811, 800, 934, 865, 822, 789, 718, 639, 605, 542, 550, 529, 538, 607, 579, 585, 649, 691, 634, 648, 642, 669, 614, 622, 978, 658, 265, 193, 231, 198, 218, 182, 183, 196, 196, 175, 206, 208, 218, 196, 215, 172, 213,
    193, 201, 190, 185, 198, 196, 197, 216, 220, 186, 213, 210, 219, 214, 199, 184, 205, 209, 202, 196, 196, 195, 205, 213, 196, 186, 208, 213, 214, 207, 310, 692, 924, 1677, 2346, 3056, 2745, 1976, 1853, 1881, 1760, 1677, 1784, 1707, 1788, 2056, 1886, 1460, 1411, 1299, 1316, 1347, 1402, 1449, 1250, 1157, 1260, 1106, 1061, 1165, 1193, 1161, 1011, 972, 848, 881, 823, 843, 824, 906, 958, 1004, 1043, 1082, 1000, 974, 863, 865, 982, 890, 845, 774, 682, 683, 638, 618, 604, 646, 614, 651, 664, 697, 711, 759, 705, 724, 737, 682, 628, 746, 1137, 519, 212, 196, 209, 196, 195, 195, 171, 206, 200, 187, 240, 197, 186, 192, 188, 196, 201,
    207, 206, 210, 240, 228, 187, 207, 202, 193, 200, 206, 205, 207, 214, 217, 200, 201, 205, 209, 185, 202, 182, 206, 209, 199, 198, 183, 179, 215, 210, 221, 272, 445, 976, 1557, 2161, 2823, 2990, 2136, 1805, 1773, 1598, 1553, 1534, 1684, 1690, 1643, 1511, 1438, 1343, 1346, 1279, 1232, 1377, 1383, 1357, 1243, 1174, 1148, 1209, 1217, 1063, 1027, 905, 940, 844, 862, 775, 797, 881, 927, 1010, 1140, 1098, 1066, 988, 1149, 1110, 1089, 989, 915, 859, 771, 704, 686, 653, 730, 686, 631, 669, 750, 701, 777, 769, 877, 785, 726, 745, 711, 777, 1187, 552, 217, 202, 216, 226, 215, 192, 204, 214, 216, 188, 180, 179, 220, 175, 196, 212, 191,
    194, 184, 223, 213, 206, 186, 223, 201, 205, 197, 208, 225, 206, 199, 190, 192, 201, 197, 197, 216, 207, 180, 173, 170, 241, 219, 199, 203, 207, 230, 196, 207, 208, 371, 902, 1360, 2015, 2695, 3121, 2259, 1813, 1716, 1644, 1536, 1591, 1580, 1541, 1580, 1522, 1448, 1411, 1272, 1284, 1292, 1327, 1307, 1167, 1224, 1181, 1156, 1084, 1034, 975, 1006, 932, 837, 873, 812, 813, 915, 1070, 1190, 1288, 1379, 1572, 1596, 1675, 1718, 1714, 1738, 1798, 1725, 1569, 1340, 1094, 828, 767, 715, 762, 756, 771, 788, 796, 915, 909, 790, 805, 789, 765, 856, 1353, 563, 220, 206, 212, 198, 206, 202, 199, 209, 194, 183, 217, 194, 192, 212, 202, 202, 194,
    199, 198, 199, 210, 178, 211, 240, 194, 185, 171, 177, 205, 184, 210, 234, 219, 193, 188, 197, 192, 180, 182, 197, 199, 192, 210, 185, 211, 238, 191, 234, 229, 217, 257, 456, 900, 1328, 2141, 2851, 3042, 2305, 1892, 1755, 1693, 1667, 1542, 1498, 1554, 1467, 1468, 1417, 1421, 1393, 1345, 1352, 1268, 1152, 1112, 1109, 1128, 1077, 1127, 1065, 1029, 997, 943, 924, 888, 956, 987, 1175, 1552, 1822, 2210, 2686, 3241, 4020, 5006, 4089, 4154, 4388, 3738, 3639, 3167, 2395, 1766, 1051, 791, 835, 884, 852, 961, 964, 962, 939, 831, 787, 821, 804, 1237, 1215, 297, 208, 201, 222, 190, 193, 192, 214, 206, 201, 202, 192, 179, 198, 206, 171, 193, 191,
    191, 201, 188, 194, 229, 209, 218, 216, 214, 213, 202, 209, 209, 212, 214, 173, 197, 196, 193, 200, 188, 188, 198, 214, 219, 188, 225, 189, 209, 188, 194, 227, 206, 228, 250, 397, 787, 775, 1456, 2405, 3045, 2940, 2044, 1857, 1778, 1673, 1546, 1518, 1507, 1447, 1420, 1432, 1346, 1334, 1300, 1334, 1204, 1189, 1130, 1211, 1101, 1100, 1054, 1092, 986, 1092, 1008, 964, 992, 1042, 1384, 1575, 2284, 2962, 3281, 3613, 3829, 3770, 3632, 3563, 3792, 3517, 3264, 3003, 2476, 2044, 1612, 1115, 899, 938, 937, 1038, 1047, 1003, 914, 958, 872, 890, 878, 1243, 1587, 418, 231, 186, 200, 203, 180, 198, 222, 195, 172, 207, 168, 200, 199, 216, 207, 203, 199,
    186, 213, 193, 196, 185, 213, 205, 173, 187, 213, 182, 214, 217, 173, 213, 182, 218, 198, 202, 180, 222, 213, 185, 190, 206, 188, 176, 207, 186, 212, 197, 191, 175, 196, 212, 366, 707, 667, 932, 1648, 2652, 3276, 2724, 2207, 1841, 1832, 1709, 1519, 1617, 1513, 1383, 1328, 1327, 1410, 1341, 1318, 1243, 1196, 1201, 1132, 1148, 1119, 1256, 1246, 1163, 1107, 1104, 1069, 1208, 1486, 1815, 2172, 2891, 2590, 2819, 2800, 2649, 2457, 2437, 2463, 2459, 2354, 2169, 1984, 1763, 1698, 1445, 971, 928, 1001, 1022, 1031, 1081, 1080, 952, 886, 942, 912, 904, 1624, 994, 224, 235, 199, 189, 214, 182, 190, 187, 204, 188, 190, 189, 222, 188, 200, 187, 196, 199,
    188, 184, 194, 200, 233, 206, 192, 194, 149, 191, 205, 194, 199, 222, 203, 202, 216, 195, 202, 184, 199, 179, 175, 201, 207, 191, 202, 213, 200, 212, 197, 193, 228, 219, 194, 220, 363, 657, 528, 560, 967, 1833, 2539, 3030, 2943, 2283, 2016, 1791, 1780, 1608, 1535, 1460, 1433, 1450, 1449, 1450, 1360, 1240, 1181, 1176, 1219, 1263, 1345, 1247, 1241, 1221, 1221, 1115, 1263, 1479, 1801, 2138, 2447, 2555, 2496, 2547, 2435, 2414, 2344, 2248, 2321, 2243, 2105, 1956, 1853, 1682, 1479, 1127, 1029, 1025, 1084, 1204, 1222, 1254, 1183, 1048, 995, 990, 897, 1204, 1628, 430, 211, 198, 180, 192, 195, 187, 211, 212, 191, 197, 241, 174, 214, 200, 211, 176, 188,
    188, 191, 217, 196, 205, 205, 242, 193, 182, 191, 202, 210, 200, 210, 228, 200, 197, 178, 189, 216, 237, 220, 228, 195, 208, 184, 191, 201, 219, 177, 183, 195, 196, 236, 226, 190, 272, 643, 591, 480, 516, 790, 1299, 2271, 3041, 3266, 2544, 2130, 1948, 1888, 1689, 1603, 1546, 1507, 1498, 1359, 1354, 1330, 1370, 1309, 1287, 1375, 1152, 1167, 1174, 1161, 1159, 1165, 1560, 1793, 2037, 2253, 2477, 2497, 2644, 2425, 2537, 2415, 2448, 2386, 2337, 2156, 2201, 1948, 1905, 1794, 1372, 1152, 1105, 1104, 1084, 1196, 1132, 1276, 1210, 1106, 1097, 1085, 960, 1377, 1275, 309, 213, 193, 180, 195, 189, 205, 202, 220, 208, 183, 224, 184, 174, 172, 207, 191, 188,
    218, 181, 235, 219, 234, 213, 184, 214, 175, 217, 189, 196, 195, 186, 202, 203, 171, 205, 206, 187, 200, 220, 233, 224, 201, 209, 179, 212, 216, 218, 194, 234, 196, 202, 207, 167, 196, 274, 660, 553, 462, 459, 474, 680, 1203, 2011, 2777, 3340, 2940, 2318, 2102, 1844, 1819, 1725, 1716, 1673, 1614, 1352, 1322, 1503, 1297, 1217, 1188, 1228, 1168, 1224, 1155, 1265, 1662, 2012, 2080, 2270, 2446, 2595, 2481, 2482, 2347, 2406, 2534, 2430, 2407, 2428, 2493, 2326, 2197, 2107, 1886, 1503, 1372, 1263, 1313, 1267, 1280, 1293, 1285, 1359, 1292, 1213, 1155, 1235, 1756, 530, 230, 206, 197, 193, 190, 169, 192, 189, 203, 207, 189, 190, 209, 195, 197, 218, 175,
    196, 194, 193, 189, 204, 216, 186, 193, 202, 177, 211, 204, 203, 213, 179, 211, 196, 199, 186, 196, 210, 204, 198, 208, 203, 214, 204, 192, 200, 190, 197, 213, 206, 195, 195, 220, 181, 332, 701, 600, 519, 430, 425, 483, 641, 911, 1299, 1736, 2693, 3328, 2734, 2424, 2260, 2208, 2096, 1930, 1675, 1455, 1499, 1441, 1260, 1155, 1114, 1138, 1088, 1222, 1455, 1657, 1804, 2027, 2278, 2518, 2417, 2686, 2503, 2480, 2635, 2836, 2893, 3063, 3024, 2821, 2519, 2483, 2414, 2199, 1871, 1605, 1550, 1489, 1542, 1357, 1325, 1355, 1371, 1320, 1350, 1370, 1101, 1823, 940, 222, 236, 193, 204, 222, 182, 196, 191, 184, 180, 226, 156, 188, 218, 207, 216, 201, 198,
    209, 206, 219, 216, 200, 212, 189, 197, 177, 208, 202, 192, 194, 189, 196, 222, 184, 174, 186, 190, 195, 197, 206, 231, 200, 199, 208, 223, 216, 219, 186, 209, 188, 181, 210, 212, 216, 237, 552, 673, 529, 422, 447, 476, 382, 431, 541, 637, 865, 1320, 2038, 2816, 3366, 3043, 2866, 2539, 2310, 1849, 1677, 1735, 1685, 1468, 1318, 1125, 1319, 1382, 1656, 1892, 1940, 2208, 2351, 2389, 2694, 2901, 3152, 3170, 3308, 3030, 2692, 2351, 1967, 1786, 1616, 1419, 1309, 1083, 674, 553, 782, 1164, 1290, 1320, 1631, 1806, 1715, 1919, 1944, 1356, 1193, 1583, 1190, 259, 197, 180, 203, 186, 200, 189, 204, 212, 187, 199, 217, 190, 181, 187, 189, 208, 218,
    208, 205, 222, 205, 204, 219, 185, 213, 220, 230, 198, 184, 182, 221, 202, 195, 207, 183, 204, 191, 225, 187, 225, 169, 189, 192, 172, 194, 215, 218, 199, 214, 184, 198, 206, 205, 197, 224, 213, 406, 689, 617, 508, 445, 404, 443, 444, 462, 409, 390, 432, 585, 823, 1072, 1399, 1774, 2138, 2152, 2045, 2278, 2313, 2217, 2283, 1591, 1638, 1598, 1829, 1982, 2097, 2102, 2427, 2363, 2488, 2433, 2293, 2105, 2070, 1911, 1852, 1699, 1636, 1506, 1412, 1346, 1242, 951, 695, 378, 259, 299, 376, 548, 871, 1219, 1234, 1432, 699, 1257, 1774, 1259, 1656, 524, 213, 215, 190, 222, 204, 192, 185, 175, 185, 196, 211, 195, 184, 172, 182, 213, 188,
    204, 189, 217, 170, 219, 222, 202, 178, 218, 195, 208, 225, 213, 209, 181, 186, 186, 175, 188, 212, 190, 224, 219, 206, 196, 212, 181, 241, 204, 210, 200, 217, 213, 206, 185, 223, 197, 225, 189, 229, 462, 837, 666, 436, 429, 539, 968, 1087, 301, 195, 231, 230, 283, 312, 349, 397, 431, 430, 456, 479, 492, 573, 495, 456, 619, 794, 939, 1112, 1295, 1296, 1435, 1689, 1745, 1848, 1753, 1723, 1829, 1811, 1727, 1625, 1591, 1569, 1433, 1340, 1155, 1027, 702, 310, 217, 209, 220, 234, 272, 321, 430, 382, 259, 360, 1612, 1557, 1652, 573, 213, 221, 182, 201, 208, 216, 193, 219, 193, 182, 226, 192, 179, 214, 202, 193, 214,
    205, 201, 178, 220, 182, 210, 206, 213, 216, 210, 183, 218, 192, 190, 203, 177, 163, 210, 202, 193, 207, 195, 197, 198, 181, 230, 203, 183, 212, 183, 220, 204, 163, 207, 180, 177, 207, 204, 180, 201, 222, 300, 440, 532, 461, 422, 900, 848, 303, 213, 210, 205, 213, 194, 211, 216, 225, 223, 206, 194, 222, 270, 285, 446, 683, 802, 929, 1049, 1194, 1216, 1339, 1532, 1634, 1810, 1801, 1769, 1849, 1792, 1729, 1654, 1609, 1553, 1371, 1354, 1238, 1062, 703, 350, 201, 213, 190, 196, 211, 213, 203, 226, 209, 248, 595, 1719, 1644, 527, 225, 189, 218, 199, 187, 181, 187, 200, 202, 187, 157, 181, 199, 201, 223, 195, 171,
    201, 200, 213, 193, 209, 182, 202, 193, 190, 206, 192, 185, 198, 210, 198, 197, 201, 190, 191, 195, 169, 203, 182, 208, 201, 210, 217, 182, 187, 191, 211, 201, 208, 205, 220, 189, 220, 183, 190, 194, 198, 237, 197, 212, 227, 281, 819, 1081, 387, 210, 202, 189, 229, 191, 172, 213, 205, 198, 220, 188, 226, 332, 591, 722, 888, 909, 1115, 1149, 1241, 1355, 1485, 1636, 1714, 1766, 1797, 1751, 1741, 1696, 1737, 1616, 1543, 1525, 1371, 1332, 1158, 976, 525, 232, 197, 201, 216, 184, 199, 205, 222, 192, 192, 227, 439, 1524, 672, 222, 207, 196, 195, 197, 192, 199, 165, 212, 174, 234, 216, 212, 197, 188, 199, 188, 226,
    219, 219, 197, 173, 197, 181, 207, 192, 196, 208, 186, 203, 212, 181, 212, 189, 193, 187, 212, 212, 195, 200, 204, 190, 220, 189, 212, 214, 198, 176, 185, 193, 214, 205, 212, 185, 217, 219, 175, 187, 229, 218, 193, 215, 216, 199, 287, 793, 788, 301, 205, 178, 194, 183, 184, 212, 180, 211, 210, 218, 383, 620, 770, 899, 1027, 1157, 1250, 1272, 1359, 1442, 1608, 1657, 1768, 1805, 1814, 1782, 1777, 1797, 1628, 1615, 1526, 1520, 1431, 1246, 1138, 938, 556, 223, 200, 202, 211, 183, 177, 199, 204, 198, 196, 184, 256, 324, 247, 203, 188, 196, 167, 192, 176, 199, 197, 189, 203, 179, 178, 195, 194, 216, 216, 207, 197,
    177, 217, 221, 201, 193, 186, 208, 187, 212, 225, 177, 190, 168, 189, 206, 202, 216, 230, 215, 192, 194, 221, 213, 181, 215, 199, 227, 212, 197, 200, 196, 197, 212, 202, 184, 193, 200, 209, 196, 221, 200, 225, 168, 230, 207, 211, 195, 379, 809, 459, 223, 226, 219, 188, 202, 171, 188, 228, 245, 453, 708, 846, 936, 1085, 1167, 1280, 1295, 1616, 1564, 1515, 1820, 1738, 1810, 1827, 1798, 1756, 1802, 1725, 1660, 1614, 1519, 1516, 1347, 1325, 1070, 831, 471, 209, 206, 199, 208, 217, 215, 200, 220, 182, 174, 195, 195, 209, 194, 198, 181, 189, 183, 198, 199, 182, 185, 192, 185, 186, 204, 181, 188, 202, 210, 187, 200,
    212, 196, 193, 193, 208, 189, 184, 212, 210, 191, 209, 190, 204, 208, 222, 202, 190, 211, 227, 187, 213, 209, 207, 216, 193, 197, 201, 200, 196, 203, 204, 189, 195, 210, 194, 182, 217, 190, 178, 210, 207, 195, 218, 208, 222, 205, 194, 207, 379, 715, 395, 231, 207, 205, 190, 192, 181, 242, 431, 709, 916, 1022, 1070, 1185, 1264, 1364, 1451, 1466, 1419, 1539, 1651, 1766, 1856, 1844, 1816, 1905, 1839, 1707, 1711, 1679, 1636, 1452, 1372, 1274, 1097, 867, 520, 252, 198, 222, 197, 185, 214, 209, 206, 208, 184, 236, 196, 211, 202, 182, 198, 209, 203, 218, 221, 206, 201, 187, 220, 202, 195, 205, 217, 199, 186, 219, 202,
    167, 186, 190, 196, 211, 203, 185, 188, 207, 207, 224, 213, 191, 222, 208, 174, 231, 202, 214, 210, 201, 197, 190, 191, 182, 197, 198, 224, 203, 197, 187, 201, 203, 198, 189, 194, 193, 194, 214, 188, 210, 198, 195, 177, 180, 180, 209, 196, 259, 338, 578, 432, 246, 203, 214, 196, 189, 374, 747, 898, 1077, 1259, 1263, 1318, 1406, 1438, 1461, 1511, 1575, 1666, 1681, 1787, 1850, 1751, 1794, 1789, 1834, 1719, 1656, 1721, 1600, 1488, 1380, 1325, 1060, 855, 537, 251, 200, 200, 197, 180, 209, 183, 226, 175, 205, 190, 197, 197, 194, 190, 208, 177, 208, 183, 186, 206, 216, 210, 195, 197, 214, 223, 186, 231, 200, 220, 210),
    dtype=np.float32).reshape(175, 119)


# main ########################################################################

if __name__ == "__main__":
    import sys
    import traceback

    if 'gl' in sys.argv or 'opengl' in sys.argv:
        backend = 'opengl'
    elif 'osmesa' in sys.argv or 'mesa' in sys.argv:
        backend = 'osmesa'
    else:
        backend = 'mpl'
    logger.info('BACKEND: %s', backend)

    app = qt.QApplication([])

    # Exception handler
    def handler(type_, value, trace):
        logger.error(
            "%s %s %s" % (type_, value, ''.join(traceback.format_tb(trace))))
    sys.excepthook = handler
    window = TestWindow(parent=None, backend=backend)

    sys.exit(app.exec_())
