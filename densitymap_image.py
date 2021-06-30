import logging
from typing import Optional, Tuple

import numpy

from silx.utils.proxy import docstring
from silx.gui import qt
from silx.gui.plot import items, PlotWindow


_logger = logging.getLogger(__name__)


class Plot(PlotWindow):

    def getPixelSizeInData(self, axis="left"):
        """Returns the size of a pixel in plot data coordinates

        :param str axis: Y axis to use in: 'left' (default), 'right'
        :return:
            Size (width, height) of a Qt pixel in data coordinates.
            Size is None if it cannot be computed
        :rtype: Union[List[float],None]
        """
        assert axis in ("left", "right")

        xaxis = self.getXAxis()
        yaxis = self.getYAxis(axis)

        if xaxis.getScale() != items.Axis.LINEAR or yaxis.getScale() != items.Axis.LINEAR:
            raise RuntimeError("Only available with linear axes")

        xmin, xmax = xaxis.getLimits()
        ymin, ymax = yaxis.getLimits()
        width, height = self.getPlotBoundsInPixels()[2:]
        if width == 0 or height == 0:
            return None
        else:
            return (xmax - xmin) / width, (ymax - ymin) / height



class ImageDensityMap(items.ImageBase, items.ColormapMixIn):
    """Item displaying an image as a density map."""

    def __init__(self):
        items.ImageBase.__init__(self, numpy.zeros((0, 0), dtype=numpy.float32))
        items.ColormapMixIn.__init__(self)
        self.__cacheLODData = {}
        self.__currentLOD = 0, 0

    def _addBackendRenderer(self, backend):
        """Update backend renderer"""
        plot = self.getPlot()
        assert plot is not None
        if not self._isPlotLinear(plot):
            # Do not render with non linear scales
            return None

        data = self.getData(copy=False)
        if data.size == 0:
            return None  # No data to display

        colormap = self.getColormap()
        if colormap.isAutoscale():
            # Avoid backend to compute autoscale: use item cache
            colormap = colormap.copy()
            colormap.setVRange(*colormap.getColormapRange(self))

        # Aggregate data according to level of details
        # TODO:
        # - pre-compute pyramid of images?
        # - allow to set aggregator
        # - make a true histogram?
        lodx, lody = self._getLevelOfDetails()

        if (lodx, lody) not in self.__cacheLODData:
            height, width = data.shape
            self.__cacheLODData[(lodx, lody)] = numpy.max(
                data[:(height//lody)*lody, :(width//lodx)*lodx].reshape(
                    height // lody, lody, width // lodx, lodx),
                axis=(1, 3))

        self.__currentLOD = lodx, lody
        aggregatedData = self.__cacheLODData[self.__currentLOD]

        sx, sy = self.getScale()
        aggregatedScale = sx * lodx, sy * lody
 
        return backend.addImage(aggregatedData,
                                origin=self.getOrigin(),
                                scale=aggregatedScale,
                                colormap=colormap,
                                alpha=self.getAlpha())

    def _getLevelOfDetails(self) -> Tuple[int,int]:
        """Return current level of details the image is displayed with."""
        plot = self.getPlot()
        if plot is None or not self._isPlotLinear(plot):
            return 1, 1  # Fallback to bas LOD

        sx, sy = self.getScale()
        xUnitPerPixel, yUnitPerPixel = plot.getPixelSizeInData()
        lodx = max(1, int(numpy.ceil(xUnitPerPixel / sx)))
        lody = max(1, int(numpy.ceil(yUnitPerPixel / sy)))
        return lodx, lody

    def getRgbaImageData(self, copy=True):
        """Get the displayed RGB(A) image

        :returns: Array of uint8 of shape (height, width, 4)
        :rtype: numpy.ndarray
        """
        return self.getColormap().applyToData(self)

    def setData(self, data, copy=True):
        """"Set the image data.

        :param numpy.ndarray data: Data array with 2 dimensions (h, w)
        :param bool copy: True (Default) to get a copy,
                          False to use internal representation (do not modify!)
        """
        data = numpy.array(data, copy=copy)
        assert data.ndim == 2
        if data.dtype.kind == 'b':
            _logger.warning(
                'Converting boolean image to int8 to plot it.')
            data = numpy.array(data, copy=False, dtype=numpy.int8)
        elif numpy.iscomplexobj(data):
            _logger.warning(
                'Converting complex image to absolute value to plot it.')
            data = numpy.absolute(data)
        self.__cacheLODData = {}  # Reset cache
        super().setData(data)

    def _updated(self, event=None, checkVisibility=True):
        # Synchronizes colormapped data if changed
        if event in (items.ItemChangedType.DATA, items.ItemChangedType.MASK):
            self._setColormappedData(
                self.getValueData(copy=False),
                copy=False)
        super()._updated(event=event, checkVisibility=checkVisibility)

    @docstring(items.ImageBase)
    def _setPlot(self, plot):
        """Refresh image when plot limits change"""
        previousPlot = self.getPlot()
        if previousPlot is not None:
            for axis in (previousPlot.getXAxis(), previousPlot.getYAxis()):
                axis.sigLimitsChanged.disconnect(self.__plotLimitsChanged)

        super()._setPlot(plot)

        if plot is not None:
            for axis in (plot.getXAxis(), plot.getYAxis()):
                axis.sigLimitsChanged.connect(self.__plotLimitsChanged)

    def __plotLimitsChanged(self):
        """Trigger update if level of details has changed"""
        if self.__currentLOD != self._getLevelOfDetails():
            self._updated()

if __name__ == "__main__":
    import sys
    from silx.gui import qt
    from silx.io import get_data
    import numpy

    if len(sys.argv) > 1:
        url = sys.argv[1]
        if ':' not in url:
            url = 'fabio:' + url
        image = get_data(url)
        height, width = image.shape
    else:  # Dummy data
        height, width = 4096, 4096
        npeaks = min(height, width)
        image = numpy.random.random((height, width))
        image[numpy.random.randint(0, height, npeaks), numpy.random.randint(0, width, npeaks)] = 10000.

    qt.QApplication.setAttribute(qt.Qt.AA_ShareOpenGLContexts, True)
    qt.QApplication.setAttribute(qt.Qt.AA_EnableHighDpiScaling, True)

    app = qt.QApplication([])
    w = Plot(backend="gl")
    #w.getYAxis().setInverted(True)
    w.setKeepDataAspectRatio(True)

    colormap = w.getDefaultColormap()
    colormap.setName('viridis')
 
    item = ImageDensityMap()
    item.setName("density map")
    item.setData(image)
    item.setColormap(colormap)
    w.addItem(item)

    item = items.ImageData()
    item.setName("image data")
    item.setData(image)
    item.setColormap(colormap)
    item.setOrigin((width, height))
    w.addItem(item)

    w.resetZoom()
    w.show()

    app.exec_()
