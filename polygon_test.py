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
from silx.image.shapes import polygon_fill_mask


logging.basicConfig()
_logger = logging.getLogger(__name__)


class TestPolygon(PlotWindow):
    SIZE = 4096  # 1024

    def __init__(self, *args, **kwargs):
        super(TestPolygon, self).__init__(*args, **kwargs)
        self.image = numpy.arange(self.SIZE ** 2, dtype=numpy.float32).reshape(
            self.SIZE, self.SIZE
        )
        colormap = {
            "name": "temperature",
            "normalization": "linear",
            "autoscale": True,
            "vmin": 0.0,
            "vmax": 1.0,
        }
        self.addImage(self.image, legend="image", colormap=colormap)

        self._mask_colormap = {
            "name": None,
            "normalization": "linear",
            "autoscale": False,
            "vmin": 0.0,
            "vmax": 1.0,
            "colors": numpy.array(
                ((0.0, 0.0, 0.0, 0.0), (0.5, 0.5, 0.5, 0.5)), dtype=numpy.float32
            ),
        }

        self.sigPlotSignal.connect(self._handleDraw)
        self.setInteractiveMode("draw", shape="polygon", color="pink")

    def _handleDraw(self, event):
        if event["event"] not in ("drawingProgress", "drawingFinished"):
            return

        points = numpy.array((event["ydata"], event["xdata"])).T

        mask = polygon_fill_mask(points, (self.SIZE, self.SIZE))
        self.addImage(
            mask,
            legend="mask",
            colormap=self._mask_colormap,
            replace=False,
            resetzoom=False,
        )


def main(argv=None):
    global app  # To avoid seg fault on quit
    app = qt.QApplication([])
    plot = TestPolygon()
    plot.show()
    return app.exec_()


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv[1:]))
