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
"""Interactive test script for silx/PyMca PlotWidget

Script options:

- pymca: To use PyMca PlotWidget (default is using silx)
- gl: To use OpenGL backend (only with PyMca, default is matplotlib)
"""


# import ######################################################################

import logging
import sys
import numpy as np
from uuid import uuid4

logging.basicConfig()
logger = logging.getLogger()

if 'pymca' in sys.argv:
    logger.warning('Using PyMca PlotWidget')
    from PyMca5.PyMcaGui import PyMcaQt as qt
    from PyMca5.PyMcaGui.plotting.PlotWidget import PlotWidget
else:
    logger.warning('Using silx PlotWidget')
    from silx.gui import qt
    from silx.gui.plot import PlotWidget


# TestWindow ##################################################################

class TestWindow(qt.QMainWindow):
    _COLORS = 'black', 'video inverted', 'red', 'green', 'blue', None

    def __init__(self, plot):
        self.plot = plot
        self._colorIndex = 0
        self._grid = 0
        self._activeCurve = True

        super(TestWindow, self).__init__()
        self.setCentralWidget(self.plot.getWidgetHandle())
        self._initMenuBar()

    def _initMenuBar(self):
        menuBar = qt.QMenuBar()

        # Menu VIEW
        menu = menuBar.addMenu('View')
        menu.addAction('resetZoom()', self.plot.resetZoom)

        def resetDataMargins():
            self.plot.setDataMargins()
        menu.addAction('setDataMargins()', resetDataMargins)

        def setDataMargins():
            self.plot.setDataMargins(0.1, 0.2, 0.3, 0.4)
        menu.addAction('setDataMargins(.1, .2, .3, .4)', setDataMargins)

        def resetZoom():
            self.plot.resetZoom((0.4, 0.3, 0.2, 0.1))
        menu.addAction('resetZoom(0.4, 0.3, 0.2, 0.1)', resetZoom)

        def toggleAutoScaleX():
            self.plot.setXAxisAutoScale(not self.plot.isXAxisAutoScale())
            self.statusBar().showMessage('Axis autoscale X: %s, Y: %s' %
                                         (self.plot.isXAxisAutoScale(),
                                          self.plot.isYAxisAutoScale()))
        menu.addAction('Toggle Autoscale X', toggleAutoScaleX)

        def toggleAutoScaleY():
            self.plot.setYAxisAutoScale(not self.plot.isYAxisAutoScale())
            self.statusBar().showMessage('Axis autoscale X: %s, Y: %s' %
                                         (self.plot.isXAxisAutoScale(),
                                          self.plot.isYAxisAutoScale()))
        menu.addAction('Toggle Autoscale Y', toggleAutoScaleY)

        def keepAspectRatio():
            self.plot.keepDataAspectRatio(
                not self.plot._plot.isKeepDataAspectRatio())
            # Ugly workaround Plot not forwarding isKeepDataAspectRatio
        menu.addAction('Keep aspect ratio', keepAspectRatio)

        def invertYAxis():
            self.plot.invertYAxis(not self.plot.isYAxisInverted())
            self.plot.replot()
        menu.addAction('Invert Y axis', invertYAxis)

        def changeGrid():
            self._grid = (self._grid + 1) % 4
            self.plot.showGrid(self._grid)
            self.statusBar().showMessage('Grid mode: %d' % self._grid)
        menu.addAction('Change Grid', changeGrid)

        def toggleCursor():
            cursor = self.plot.getGraphCursor()
            if cursor is None:
                self.plot.setGraphCursor(True, color='red', linewidth=1)
            else:
                self.plot.setGraphCursor(False)
            self.statusBar().showMessage('Cursor mode: %s' %
                                         str(self.plot.getGraphCursor()))
        menu.addAction('Toggle Cursor', toggleCursor)

        def toggleLogX():
            self.plot.setXAxisLogarithmic(not self.plot.isXAxisLogarithmic())
            self.plot.replot()
            self.statusBar().showMessage('Log Scale X: %s, Y: %s' %
                                         (self.plot.isXAxisLogarithmic(),
                                          self.plot.isYAxisLogarithmic()))
        menu.addAction('Toggle Log X', toggleLogX)

        def toggleLogY():
            self.plot.setYAxisLogarithmic(not self.plot.isYAxisLogarithmic())
            self.plot.replot()
            self.statusBar().showMessage('Log Scale X: %s, Y: %s' %
                                         (self.plot.isXAxisLogarithmic(),
                                          self.plot.isYAxisLogarithmic()))
        menu.addAction('Toggle Log Y', toggleLogY)

        def changeBaseVectors():
            baseVectors = self.plot._plot.getBaseVectors()
            if baseVectors == ((1., 0.), (0., 1.)):
                baseVectors = (1., 0.5), (0.3, 1.)
            else:
                baseVectors = (1., 0.), (0., 1.)
            self.plot._plot.setBaseVectors(*baseVectors)
            self.plot.replot()
        menu.addAction('Change base vectors', changeBaseVectors)

        # Menu INTERACTION
        menu = menuBar.addMenu('Interaction')

        def zoomMode():
            self._colorIndex = (self._colorIndex + 1) % len(self._COLORS)
            color = self._COLORS[self._colorIndex]
            self.statusBar().showMessage('Enable zoom, color: %s' % color)
            self.plot.setZoomModeEnabled(True, color)
        menu.addAction('Zoom Mode', zoomMode)

        def drawPolygon():
            self.plot.setDrawModeEnabled(True, 'polygon', label='mask',
                                         color='red')
        menu.addAction('Draw Polygon', drawPolygon)

        def drawRect():
            self.plot.setDrawModeEnabled(True, 'rectangle', label='mask')
        menu.addAction('Draw Rectangle', drawRect)

        def drawLine():
            self.plot.setDrawModeEnabled(True, 'line', label='LINE')
        menu.addAction('Draw Line', drawLine)

        def drawHLine():
            self.plot.setDrawModeEnabled(True, 'hline', label='HORIZONTAL')
        menu.addAction('Draw Horiz. Line', drawHLine)

        def drawVLine():
            self.plot.setDrawModeEnabled(True, 'vline', label='VERTICAL')
        menu.addAction('Draw Vert. Line', drawVLine)

        def toggleActiveCurve():
            self._activeCurve = not self._activeCurve
            self.plot.enableActiveCurveHandling(self._activeCurve)
            self.statusBar().showMessage(
                'Active curve handling: %s' % self._activeCurve)
        menu.addAction('Toggle active curve', toggleActiveCurve)

        def panMode():
            if hasattr(self.plot, 'setInteractiveMode'):  # silx
                self.plot.setInteractiveMode('pan')
            else:  # matplotlib OpenGL backend
                self.plot._plot.setInteractiveMode('pan')
        action = menu.addAction('Pan Mode', panMode)
        if (not hasattr(self.plot, 'setInteractiveMode') and
                not hasattr(self.plot._plot, 'setInteractiveMode')):
            action.setEnabled(False)

        # Menu DATA
        menu = menuBar.addMenu('Data')

        def clear():
            self.resetTimer()
            self.plot.clear()
        menu.addAction('Clear', self.plot.clear)

        def saveAsSvg():
            filename = 'testSaveGraph.svg'
            self.plot.saveGraph(filename, 'svg')
            self.statusBar().showMessage('Saved as %s' % filename)
        menu.addAction('Save as svg', saveAsSvg)

        def toggleRightAxis():
            curve = self.plot.getCurve("rightTest")
            if curve is None:
                data = np.arange(1000., dtype=np.float32)
                self.plot.addCurve(data, np.sqrt(data), legend="rightTest",
                                   replace=False, replot=True, z=5,
                                   color='black', linestyle="-",
                                   selectable=True,
                                   xlabel="Right X", ylabel="Right Y",
                                   yaxis="right")
            else:
                self.plot.removeCurve("rightTest")
        menu.addAction('Right axis data', toggleRightAxis)

        def setUInt16Data():
            dataUInt16 = np.arange(1024*1024, dtype=np.uint16)
            dataUInt16.shape = 1024, -1

            colormap2 = {'name': 'temperature', 'normalization': 'linear',
                         'autoscale': False,
                         'vmin': 1.0, 'vmax': dataUInt16.max(),
                         'colors': 256}
            self.plot.addImage(dataUInt16, legend="image 2",
                               xScale=(0, 1.0), yScale=(100., 1.0),
                               replace=False, replot=True,
                               colormap=colormap2)
        menu.addAction('DataSet uint16 1', setUInt16Data)

        def setUInt16Data2():
            dataUInt16 = np.arange(1024*1024, dtype=np.uint16) + 10000
            dataUInt16.shape = 1024, -1

            colormap2 = {'name': 'temperature', 'normalization': 'linear',
                         'autoscale': False, 'vmin': 1.0,
                         'vmax': dataUInt16.max(),
                         'colors': 256}
            self.plot.addImage(dataUInt16, legend="image 2",
                               xScale=(0, 1.0), yScale=(0., 1.0),
                               replace=False, replot=True, colormap=colormap2)
        menu.addAction('DataSet uint16 2', setUInt16Data2)

        def testEverythingAction():
            self.resetTimer()
            self.plot.clear()
            self.plot.resetZoom()
            testEverything(self.plot)
        menu.addAction('Test everything', testEverythingAction)

        def testLogAction():
            self.resetTimer()
            self.plot.clear()
            self.plot.resetZoom()
            testLog(self.plot)
        menu.addAction('Test Log', testLogAction)

        def testErrorBarsAction():
            self.resetTimer()
            self.plot.clear()
            self.plot.resetZoom()
            testErrorBars(self.plot)
        menu.addAction('Test Error Bars', testErrorBarsAction)

        def testReversedImagesAction():
            self.resetTimer()
            self.plot.clear()
            self.plot.resetZoom()
            testReversedImages(self.plot)
        menu.addAction('Test Reversed Images', testReversedImagesAction)

        def testMarkersAction():
            self.resetTimer()
            self.plot.clear()
            self.plot.resetZoom()
            testMarkers(self.plot)
        menu.addAction('Test Markers', testMarkersAction)

        def testScatterAction():
            self.resetTimer()
            self.plot.clear()
            self.plot.resetZoom()
            testScatter(self.plot)
        menu.addAction('Test Scatter', testScatterAction)

        def testStreamingAction():
            self.resetTimer()
            self.plot.clear()
            self.streaming()
            self.plot.resetZoom()
            self.useTimer(self.streaming, 100)
        menu.addAction('Test Streaming', testStreamingAction)

        self.setMenuBar(menuBar)
        self.show()

    def streaming(self):
        data = np.asarray(np.random.random(512*512), dtype=np.float32)
        data.shape = 512, 512
        # replot=False to avoid resetZoom
        self.plot.addImage(data, replace=False, replot=False)
        self.plot.replot()

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
        self.plot.keyPressEvent(event)


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
        replace=False, replot=False,
        shape="polygon", fill=True, color='blue')
    w.addItem(
        xdata=np.array((200, 200, 400, 400)),
        ydata=np.array((200, 400, 400, 200)),
        legend="test2", info=None,
        replace=False, replot=False,
        shape="polygon", fill=False, color='green')
    w.addItem(
        xdata=np.array((1300, 1600, 1900, 1300, 1900)),
        ydata=np.array((-700, -200, -700, -300, -300)),
        legend="star", info=None,
        replace=False, replot=False,
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
        replace=False, replot=False,
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

    print('add curve 2')
    w.addCurve(xData, xData ** 8, legend="curve 2", z=2,
               # color='#0000FF80',
               replace=False, replot=False, linestyle="-", symbol="o",
               xlabel="curve 2 X", ylabel="curve 2 Y",
               # selectable=True,
               yaxis="left")  # fill=True)

    print('add curve minus')
    w.addCurve(xData, (xData - 100.) ** 7, legend="curve minus", z=1,
               # color='#0000FF80',
               replace=False, replot=False, linestyle="-", symbol="o",
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


# attic #######################################################################

def attic():
    # Second plot
    w2 = PlotWidget.PlotWidget(parent=None, backend=backend)
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


# callback ####################################################################

def _plotCallback(eventDict=None):
    if eventDict['event'] != 'mouseMoved':
        pass  # print(eventDict)
    if eventDict['event'] == 'curveClicked':
        print('setActiveCurve', eventDict['label'])
        w.setActiveCurve(eventDict['label'])
    if eventDict['event'] == 'drawingFinished':
        shape = eventDict['type']
        if shape in ['polygon', 'rectangle']:
            w.addItem(
                xdata=eventDict['xdata'],
                ydata=eventDict['ydata'],
                legend=str(uuid4()), info=None,
                replace=False, replot=True,
                shape=eventDict['type'], fill=True,
                color="#000000")
        elif shape in ['hline', 'vline', 'line']:
            w.addItem(
                xdata=eventDict['xdata'],
                ydata=eventDict['ydata'],
                legend=str(uuid4()), info=None,
                replace=False, replot=True,
                shape=eventDict['type'], fill=False,
                color="#0000FF")


# main ########################################################################

if __name__ == "__main__":
    import sys
    import time

    if 'gl' in sys.argv or 'opengl' in sys.argv:
        backend = 'opengl'
    elif 'osmesa' in sys.argv or 'mesa' in sys.argv:
        backend = 'osmesa'
    else:
        backend = 'mpl'
    logger.info('BACKEND: %s', backend)

    app = qt.QApplication([])

    w = PlotWidget(parent=None, backend=backend)
    w.sigPlotSignal.connect(_plotCallback)

    testLog(w)

    window = TestWindow(w)

    w.setPanWithArrowKeys(True)

    sys.exit(app.exec_())
