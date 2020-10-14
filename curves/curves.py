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
"""Test CurvesView with live data."""

from __future__ import division

__authors__ = ["T. VINCENT"]
__license__ = "MIT"
__date__ = "30/05/2017"


import base64, sys
import os

os.environ["TANGO_HOST"] = "nela:20000"

import PyTango
from XSDataBioSaxsv1_0 import XSDataResultBioSaxsHPLCv1_0

from CurvesView import CurvesView


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
                "Unable to recognize the encoding of the data !!!"
                "got %s, expected base64, base32 or base16,"
                "I assume it is base64 " % strCoding
            )
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


class CB(object):
    def __init__(self, device, w):
        self._device = device
        self._w = w
        self._init = False

    def push_event(self, event):
        if event.attr_value is not None:
            if event.attr_value.name.endswith("jobSuccess"):
                print("jobSuccess")
                # Get curve
                jobid = event.attr_value.value  # from event
                print("jobid", jobid)
                x = self._device.getJobOutput(jobid)
                xsd = XSDataResultBioSaxsHPLCv1_0.parseString(x)
                if not self._init and xsd.dataQ is not None:
                    q = xsDataToArray(xsd.dataQ)
                    w.setXData(q)
                    self._init = True
                if xsd.dataI is not None:
                    i = xsDataToArray(xsd.dataI)
                    i[i <= 1] = 1  # Hack
                    w.appendCurves(i)

                # err = xsDataToArray(xsd.dataStdErr)


if __name__ == "__main__":
    from silx.gui import qt

    app = qt.QApplication([])

    w = CurvesView()
    # w.setAttribute(qt.Qt.WA_DeleteOnClose)
    w.getPlot().setYAxisLogarithmic(True)
    w.show()

    device = PyTango.DeviceProxy("DAU/edna/3")
    cb = CB(device, w)
    device.subscribe_event("jobSuccess", PyTango.EventType.CHANGE_EVENT, cb, [], True)
    # device.subscribe_event("jobFailure", PyTango.EventType.CHANGE_EVENT, cb, [], True)
    # device.subscribe_event("statisticsCollected", PyTango.EventType.CHANGE_EVENT, cb, [], True)
    print("init done")

    app.exec_()
