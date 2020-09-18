from silx.gui import qt
from silx.gui.plot import items, PlotWindow
import sys
print(sys.path)
import silx_monkey_patch


class TestItem(items.ImageData):

    sigVisibleExtentChanged = qt.Signal()

    def _setPlot(self, plot):
        super()._setPlot(plot)
        xaxis = plot.getXAxis()
        xaxis.sigLimitsChanged.connect(self._limitsChanged)
        xaxis.sigScaleChanged.connect(self._scaleChanged)

        yaxis = plot.getYAxis() # TODO handle left axis
        yaxis.sigLimitsChanged.connect(self._limitsChanged)
        yaxis.sigScaleChanged.connect(self._scaleChanged)

    def _limitsChanged(self, begin, end):
        self.sigVisibleExtentChanged.emit()

    def _scaleChanged(self, scale):
        pass


if __name__ == "__main__":
    from silx.gui import qt
    import numpy

    qt.QApplication.setAttribute(qt.Qt.AA_ShareOpenGLContexts, True)
    qt.QApplication.setAttribute(qt.Qt.AA_EnableHighDpiScaling, True)

    app = qt.QApplication([])
    w = PlotWindow()
    item = TestItem()
    item.setData(numpy.arange(100).reshape(10, 10))
    w.addItem(item)
    w.show()
    app.exec_()
