# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2017 European Synchrotron Radiation Facility
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
"""
Widget displaying the synthesis of many curves taken with the same X values
"""

from __future__ import division

__authors__ = ["T. VINCENT"]
__license__ = "MIT"
__date__ = "15/05/2017"


import logging

import numpy

from silx.gui import qt
from silx.gui.plot import Plot1D

_logger = logging.getLogger(__name__)

if hasattr(numpy, 'nanmean'):
    nanmean = numpy.nanmean
else:  # Debian 7 support
    def nanmean(data, axis=None):
        """Compute mean of none NaN elements

        :param numpy.ndarray data: The array to process
        :param axis: None or the axis index along which to compute the means.
        """
        notNaNMask = numpy.logical_not(numpy.isnan(data))
        return numpy.nansum(data, axis) / numpy.sum(notNaNMask, axis, dtype='int')


# TODO split control widgets from curves plot
# TODO make curves handling not being a widget and make it interact with a plot
# TODO optimisation of min/mean/max computation
# TODO optimisation of plotting: no update curves when not in live mode
# TODO optimisation of plotting: no update of background when not 'visible' change
# TODO add std? in background
# TODO error bars of current curves
# TODO set number of curves displayed
# TODO matplotlib bad rendering of filled curves regarding edges
# TODO OO API with setters

class CurvesView(qt.QWidget):
    """Widget displaying statistical indicators over many curves

    :param parent:
    :param f:
    """

    def __init__(self, parent=None, f=qt.Qt.WindowFlags()):
        super(CurvesView, self).__init__(parent, f)

        self._nbExtraCurves = 5
        self._currentCurveColor = 0., 0.8, 0., 1.
        self._index = -1
        self._x = None
        self._data = None
        self._min = None
        self._max = None
        self._sum = None
        self._count = None

        self._plot = Plot1D() #backend='gl')
        self._plot.setActiveCurveHandling(False)

        layout = qt.QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self._plot, 0, 0, 1, 2)

        self._slider = qt.QSlider(qt.Qt.Horizontal)
        layout.addWidget(self._slider, 1, 0)
        self._spinBox = qt.QSpinBox()
        layout.addWidget(self._spinBox, 1, 1)

        self._slider.valueChanged.connect(self._indexChanged)
        self._spinBox.valueChanged.connect(self._indexChanged)

        self._updateControlWidgets()

    def getPlot(self):
        """Returns the used :class:`PlotWidget` plot."""
        return self._plot

    def setXData(self, x):
        """Set the X coordinates of the curves.

        :param numpy.ndarray x: The X coordinates of the curves.
        """
        x = numpy.array(x, copy=True)
        assert x.ndim == 1
        if self._data is not None:
            assert len(x) == self._data.shape[-1]

        self._x = x

    def getXData(self):
        """Returns the X coordiantes of the curves(numpy.ndarray)"""
        return numpy.array(self._x, copy=True)

    def clear(self):
        """Reset the plot by removing all curves"""
        self._data = None
        self._min = None
        self._max = None
        self._sum = None
        self._count = None
        self.getPlot().clear()
        self.setCurrentCurveIndex(-1)
        self._updateControlWidgets()

    def _updateCurrentCurve(self):
        """Update the current curve in the plot"""
        plot = self.getPlot()
        data = self.getData(copy=False)
        currentIndex = self.getCurrentCurveIndex(absolute=True)

        for offset in range(- self._nbExtraCurves - 1,
                            self._nbExtraCurves + 1):
            index = currentIndex + offset
            if offset == 0:
                continue

            legend = 'N%+d' % offset
            plot.remove(legend=legend, kind='curve')

            if 0 <= index < len(data):
                distance = abs(offset) / (self._nbExtraCurves + 1)
                if abs(offset) == 1:  # first curve
                    linestyle = '-'
                elif distance < 0.66:
                    linestyle = '--'
                else:
                    linestyle = ':'
                if offset < 0:
                    color = numpy.array(self._currentCurveColor) * 0.5
                else:
                    color = '#FF9900'
                plot.addCurve(
                    self.getXData(), data[index], legend=legend,
                    color=color,
                    linestyle=linestyle,
                    z=100, resetzoom=False)

        # Current curve
        if currentIndex < len(data):
            currentCurve = data[currentIndex]
            plot.addCurve(
                self.getXData(), currentCurve, legend='current',
                color=self._currentCurveColor, z=101,
                linewidth=2,
                resetzoom=False)
        else:
            plot.remove(legend='current', kind='curve')

    def _indexChanged(self, index):
        """Handle spinBox or slider value changed"""
        currentIndex = self.getCurrentCurveIndex(absolute=True)
        if currentIndex != index:
            # Do not update index if it is already OK
            self.setCurrentCurveIndex(index)
        elif index == len(self.getData(copy=False)) - 1:
            # Set to last curve
            self.setCurrentCurveIndex(-1)

    def setCurrentCurveIndex(self, index=-1):
        """Perform update when current curve changed

        :param int index:
            The index of the current curve in the array
            The index can be negative to start indexing from the end
            Default: -1 = Lastest curve.
        """
        data = self.getData(copy=False)
        assert index in (-1, 0) or - len(data) <= index < len(data)
        self._index = index

        if self._index < 0:
            absoluteIndex = len(data) + self._index
        else:
            absoluteIndex = self._index

        self._spinBox.setValue(absoluteIndex)
        self._slider.setValue(absoluteIndex)

        self._updateCurrentCurve()

    def getCurrentCurveIndex(self, absolute=False):
        """Returns the current curve index

        :param bool absolute:
            False (default) to get index as Python indexing (can be negative),
            True to get current index from the beginning of the data array (>= 0).
        :return: The index
        :rtype: int
        """
        if absolute and self._index < 0:  # Negative index is from the end
            return max(0, len(self.getData(copy=False)) + self._index)
        else:
            return self._index

    def _updateControlWidgets(self):
        """Update widgets controlling """
        nbCurves = len(self.getData(copy=False))
        if self.getCurrentCurveIndex() >= 0:
            index = nbCurves - 1
        else:
            index = nbCurves + self.getCurrentCurveIndex()

        self._slider.setRange(0, index)
        self._spinBox.setRange(0, index)
        self._slider.setEnabled(nbCurves > 0)
        self._spinBox.setEnabled(nbCurves > 0)

        self.setCurrentCurveIndex(self.getCurrentCurveIndex())

    def getData(self, copy=True):
        """Return displayed curves data

         :param bool copy: True to get a copy (default),
             False to get internal representation, do not modify.
        :return: A copy of the data currently displayed
        """
        if self._data is None:
            return numpy.array(()).reshape(0, 0)  # Empty 2D array
        else:
            return numpy.array(self._data, copy=copy)

    def appendCurves(self, data):
        """Add curve(s) to the plot.

        The data is always copied.

        :param numpy.ndarray data:
            If 1D, it is a curve to append to the plot.
            If 2D, it is a set of curves to append.
        """
        plot = self.getPlot()
        data = numpy.atleast_2d(numpy.array(data, copy=False))
        assert data.ndim == 2

        wasData = self._data is not None

        if self._data is None:
            if self._x is None:
                self._x = numpy.arange(data.shape[-1])
            assert len(self._x) == data.shape[-1]
            self._data = numpy.array(data, copy=True)

        else:
            assert self._data.shape[-1] == data.shape[-1]
            self._data = numpy.append(self._data, data, axis=0)

        self._updateControlWidgets()

        # Update plot background
        z = 1
        maxs = numpy.nanmax(self._data, axis=0)
        plot.addCurve(
            self.getXData(), maxs, legend='maximum',
            color='#D0D0D0', fill=True, z=z,
            linestyle='-',
            resetzoom=False)

        z += 1
        mins = numpy.nanmin(self._data, axis=0)
        plot.addCurve(
            self.getXData(), mins, legend='minimum',
            color='#FFFFFF', fill=True, z=z,
            linestyle='-',
            resetzoom=False)

        z += 1
        means = nanmean(self._data, axis=0)
        plot.addCurve(
            self.getXData(), means, legend='mean',
            color='#FFFFFF',
            linewidth=2, linestyle='-',
            z=z,
            resetzoom=False)

        # Draw current curve
        self._updateCurrentCurve()


        if not wasData:
            self.resetZoom()

    def resetZoom(self):
        """Reset Plot zoom"""
        self.getPlot().resetZoom()


import base64, sys

def xsDataToArray(_xsdata):
    """
    Lightweight, EDNA-Free implementation of the same function.
    Needed library: Numpy, base64 and sys
    Convert a XSDataArray into either a numpy array or a list of list

    @param _xsdata: XSDataArray instance
    @return: numpy array
    """
    shape = tuple(_xsdata.getShape())
    encData = _xsdata.getData()

    if _xsdata.getCoding() is not None:
        strCoding = _xsdata.getCoding().getValue()
        if strCoding == "base64":
            decData = base64.b64decode(encData)
        elif strCoding == "base32":
            decData = base64.b32decode(encData)
        elif strCoding == "base16":
            decData = base64.b16decode(encData)
        else:
            print(
                "Unable to recognize the encoding of the data !!! got %s, expected base64, base32 or base16, I assume it is base64 " % strCoding)
            decData = base64.b64decode(encData)
    else:
        print("No coding provided, I assume it is base64 ")
        strCoding = "base64"
        decData = base64.b64decode(encData)
    try:
        matIn = numpy.fromstring(decData, dtype=_xsdata.getDtype())
    except Exception:
        matIn = numpy.fromstring(decData, dtype=numpy.dtype(str(_xsdata.getDtype())))
    arrayOut = matIn.reshape(shape)
    # Enforce little Endianness
    if sys.byteorder == "big":
        arrayOut.byteswap(True)
    return arrayOut


if __name__ == '__main__':
    import glob

    live = True #False

    if not live:
        npz = numpy.load('curves.npz')
        q = npz['q']
        data = npz['intensities']
        npz.close()
        data[data <= 1] = 1  # HACK

    if 0:
        data, q = [], None
        for f in glob.glob('*.dat'):
            if q is None:
                q = numpy.loadtxt(f).T[0]  # Get Q
            data.append(numpy.loadtxt(f).T[1])  # Get I
        data = numpy.array(data)
        numpy.savez('curves.npz', q=q, intensities=data)
        data[data <= 1] = 1  # HACK

    import os
    os.environ['TANGO_HOST'] = 'nela:20000'

    import PyTango
    from XSDataBioSaxsv1_0 import XSDataResultBioSaxsHPLCv1_0

    class CB(object):
        def __init__(self, device, w):
            self._device = device
            self._w = w
            self._init = False

        def push_event(self, event):
            print('got something', event)
            if event.attr_value is not None:
                if event.attr_value.name.endswith("jobSuccess"):
                    print('jobSuccess')
                    # Get curve
                    jobid = event.attr_value.value  # from event
                    print('jobid', jobid)
                    x = self._device.getJobOutput(jobid)
                    xsd = XSDataResultBioSaxsHPLCv1_0.parseString(x)
                    if not self._init and xsd.dataQ is not None:
                        q = xsDataToArray(xsd.dataQ)
                        w.setXData(q)
                        self._init = True
                    if xsd.dataI is not None:
                        i = xsDataToArray(xsd.dataI)
                        i[i <= 1] = 1
                        print('i', i)
                        w.appendCurves(i)

                    # err = xsDataToArray(xsd.dataStdErr)

    app = qt.QApplication([])

    class MyCurvesView(CurvesView):
        """Makes appendCurves callable from threads"""

        sigAppendCurves = qt.Signal(object)
        sigSetXData = qt.Signal(object)

        def __init__(self, parent=None):
            super(MyCurvesView, self).__init__(parent)
            self.sigAppendCurves.connect(
                super(MyCurvesView, self).appendCurves)

        def appendCurves(self, curves):
            self.sigAppendCurves.emit(curves)

        def setXData(self, x):
            self.sigSetXData.emit(x)


    w = MyCurvesView()
    # w.setAttribute(qt.Qt.WA_DeleteOnClose)
    w.getPlot().setYAxisLogarithmic(True)
    w.show()

    if live:
        thread = False
        device = PyTango.DeviceProxy("DAU/edna/3")
        cb = CB(device, w)
        device.subscribe_event("jobSuccess", PyTango.EventType.CHANGE_EVENT, cb, [], True)
        # device.subscribe_event("jobFailure", PyTango.EventType.CHANGE_EVENT, cb, [], True)
        # device.subscribe_event("statisticsCollected", PyTango.EventType.CHANGE_EVENT, cb, [], True)
        print('init done')

    if not live:
        import threading
        import time

        w.appendCurves(data)
        w.setXData(q)

        running = True

        def addCurves():
            index = 0
            while running:
                time.sleep(1)
                w.appendCurves(data[index % len(data)])
                index += 1

        thread = threading.Thread(target=addCurves)
        thread.start()


    app.exec_()
    print('closing...')
    if thread:
        running = False
        thread.join(2)
