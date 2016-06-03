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
# ############################################################################*/
"""Interactive test of silx polygon filling"""


__authors__ = ["T. Vincent"]
__license__ = "MIT"
__date__ = "03/06/2016"


import logging

import numpy

from silx.gui import qt
from silx.gui.plot import PlotWindow
from silx.image.polygon import polygon_fill


logging.basicConfig()
_logger = logging.getLogger(__name__)


class TestPolygon(PlotWindow):
    SIZE = 1024

    def __init__(self, *args, **kwargs):
        super(TestPolygon, self).__init__(*args, **kwargs)
        self.mask = numpy.zeros((self.SIZE, self.SIZE), dtype=numpy.uint8)

        self.addImage(self.mask)
        self.sigPlotSignal.connect(self._handleDraw)
        self.setInteractiveMode('draw', shape='polygon', color='pink')

    def _handleDraw(self, event):
        if event['event'] not in ('drawingProgress', 'drawingFinished'):
            return

        points = numpy.array((event['ydata'], event['xdata'])).T

        self.mask = polygon_fill(points, (self.SIZE, self.SIZE))
        self.addImage(self.mask, resetzoom=False)


def main(argv=None):
    global app  # To avoid seg fault on quit
    app = qt.QApplication([])
    plot = TestPolygon()
    plot.show()
    return app.exec_()


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv[1:]))
