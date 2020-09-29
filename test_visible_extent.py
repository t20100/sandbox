from silx.gui import qt
from silx.gui.plot import items, PlotWindow

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import silx_monkey_patch


class TestItem(items.ImageData):

    sigVisibleExtentChanged = qt.Signal()

    def _setPlot(self, plot):
        super()._setPlot(plot)

        xaxis = plot.getXAxis()
        xaxis.sigLimitsChanged.connect(self._limitsChanged)
        xaxis.sigScaleChanged.connect(self._scaleChanged)

        yaxis = plot.getYAxis(
            self.getYAxis() if isinstance(self, items.YAxisMixIn) else 'left')
        yaxis.sigLimitsChanged.connect(self._limitsChanged)
        yaxis.sigScaleChanged.connect(self._scaleChanged)

        self.__previousVisibleExtent = self.getVisibleExtent()
        self.sigVisibleExtentChanged.emit()

    def _limitsChanged(self, begin, end):
        extent = item.getVisibleExtent()
        if extent != self.__previousVisibleExtent:
            self.__previousVisibleExtent = extent
            self.sigVisibleExtentChanged.emit()

    def _scaleChanged(self, scale):
        pass  # TODO ?

    def _update(self, backend):
        super()._update(backend)
        width, height = item.getPlot().getPixelSizeInData()
        print('Pixel size', width, height)
        sx, sy = item.getScale()
        print('Array size', width / sx, height / sy)


if __name__ == "__main__":
    from silx.gui import qt
    import numpy

    qt.QApplication.setAttribute(qt.Qt.AA_ShareOpenGLContexts, True)
    qt.QApplication.setAttribute(qt.Qt.AA_EnableHighDpiScaling, True)

    app = qt.QApplication([])
    w = PlotWindow(backend='gl')
    item = TestItem()

    def cb():
        print('Extent', item.getVisibleExtent())
        print('Slices', item.getVisibleSlices())
    item.sigVisibleExtentChanged.connect(cb)

    item.setData(numpy.arange(100, dtype='float16').reshape(10, 10))
    w.addItem(item)
    w.show()
    app.exec_()
