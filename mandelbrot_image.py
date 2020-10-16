from typing import Optional, Tuple

from silx.utils.proxy import docstring
from silx.gui import qt
from silx.gui.plot import items, PlotWindow


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


def mandelbrot(
    iterations: int,
    x: Tuple[float, float],
    y: Tuple[float, float],
    shape: Tuple[int, int],
):
    """Mandelbrot set: image of number of iterations to reach threshold

    See https://en.wikipedia.org/wiki/Mandelbrot_set

    :param int iterations: Maximum number of iterations.
    :param List[float] x: (xmin, xmax) range to compute Mandelbrot
    :param List[float] y: (ymin, ymax) range to compute Mandelbrot
    :param List[int] shape: (height, width) of the output image
    """
    xmin, xmax = x
    ymin, ymax = y
    assert xmin < xmax
    assert ymin < ymax

    height, width = shape

    x = numpy.linspace(x[0], x[1], width, endpoint=True)
    y = numpy.linspace(y[0], y[1], height, endpoint=True)
    c = x.reshape(1, -1) + 1j * y.reshape(-1, 1)

    for dtype in (numpy.uint8, numpy.uint16, numpy.uint32, numpy.uint64):
        if numpy.iinfo(dtype).max > iterations:
            break
    image = numpy.zeros_like(c, dtype=dtype)

    z = c  # Correspond to first iteration
    for index in range(iterations):
        z = z**2 + c
        image[z.real**2 + z.imag**2 < 2**2] = index

    return image


class MandelbrotSet(items.ImageBase, items.ColormapMixIn):
    """Item displaying a Mandelbrot set.

    Illustrates multi-resolution images
    """

    XRANGE = -2.5, 1.
    YRANGE = -1., 1.
    SHAPE = 1e50, 1e50  # 1 Googol pixels (https://en.wikipedia.org/wiki/Googol)
    ITERATIONS = 100

    sigVisibleSlicesChanged = qt.Signal()
    """Signal emitted when the visible slices of the array has changed."""

    def __init__(self):
        items.ImageBase.__init__(self, None)
        items.ColormapMixIn.__init__(self)
        self.__previousLevelOfDetail = -1
        self.__previousVisibleSlices = slice(0), slice(0)
        self.__chunkShape = 1, 1
        self._sigVisibleBoundsChanged.connect(self.__visibleBoundsChanged)
        self._setVisibleBoundsTracking(True)

    def _isPlotLinear(self, plot):
        """Return True if plot only uses linear scale for both of x and y
        axes."""
        linear = plot.getXAxis().LINEAR
        if plot.getXAxis().getScale() != linear:
            return False
        if plot.getYAxis().getScale() != linear:
            return False
        return True

    def _getBounds(self):
        if 0 in self.SHAPE:  # Empty data
            return None

        height, width = self.SHAPE
        origin = self.getOrigin()
        scale = self.getScale()
        # Taking care of scale might be < 0
        xmin, xmax = origin[0], origin[0] + width * scale[0]
        if xmin > xmax:
            xmin, xmax = xmax, xmin
        # Taking care of scale might be < 0
        ymin, ymax = origin[1], origin[1] + height * scale[1]
        if ymin > ymax:
            ymin, ymax = ymax, ymin

        plot = self.getPlot()
        if plot is not None and not self._isPlotLinear(plot):
            return None
        else:
            return xmin, xmax, ymin, ymax

    @docstring(items.ImageData)
    def _setPlot(self, plot):
        previousPlot = self.getPlot()
        if previousPlot is not None:
            for axis in (plot.getXAxis(), plot.getYAxis()):
                axis.sigLimitsChanged.disconnect(self.__plotLimitsChanged)

        self.__previousLevelOfDetail = -1
        super()._setPlot(plot)

        if plot is not None:
            for axis in (plot.getXAxis(), plot.getYAxis()):
                axis.sigLimitsChanged.connect(self.__plotLimitsChanged)

    def __plotLimitsChanged(self, *args) -> None:
        level = self._getLevelOfDetail()
        if level != self.__previousLevelOfDetail:
            self.__previousLevelOfDetail = level
            self._updated()  # Dirty the

    def _getMaxLevel(self) -> Optional[int]:
        """Returns the maximum available level of detail.

        :rtype: Union[int,None]
        """
        return max(0, numpy.log2(max(*self.SHAPE)) - numpy.log2(512))

    def _getLevelOfDetail(self) -> int:
        """Returns current level of detail (0 for full resolution)"""
        plot = self.getPlot()
        if plot is None:
            return 0

        sx, sy = self.getScale()
        width, height = plot.getPixelSizeInData()
        elemPerPixel = max(width / sx, height / sy)
        level = int(numpy.ceil(numpy.log2(elemPerPixel))) if elemPerPixel > 1.0 else 0
        return numpy.clip(level, 0, self._getMaxLevel())

    def getOrigin(self):
        return self.XRANGE[0], self.YRANGE[0]

    def getScale(self):
        height, width = self.SHAPE
        return ((self.XRANGE[1] - self.XRANGE[0]) / width,
                (self.YRANGE[1] - self.YRANGE[0]) / height)

    def __checkLevel(self, level: int) -> None:
        """Check if provided level of detail is valid

        :param int level: Level of detail
        :raises ValueError: if requested level of detail is not available
        """
        maxLevel = self._getMaxLevel()
        if maxLevel is None or not 0 <= level <= maxLevel:
            raise ValueError("Requested level of detail is not available")

    def __convertLevel0Slice(self, slice_, level) -> Tuple[slice]:
        """Convert Level of detail 0 slicing to another level.

        Conversion is done so that initial array subset is fully
        available in sub-sampled slicing.
        Converted slicing can cover a larger extent than the initial one,
        thus corresponding slicing in level 0 is also returned.

        :param slice_: Slice in level of detail 0
        :param level: The level of detail to convert slicing to
        :return: Converted slice, Corresponding level 0 slice
        :rtype: List[slice]
        :raises ValueError: if requested level of detail is not available
        """
        self.__checkLevel(level)
        if slice_.step not in (1, None):
            raise NotImplementedError("slice step must be 1 or None")

        factor = 2 ** level
        if slice_.start is None:
            start = None
        else:
            start = slice_.start // factor
        if slice_.stop is None:
            stop = None
        else:
            stop = int(numpy.ceil(slice_.stop / factor))
        return slice(start, stop), slice(
            None if start is None else start * factor,
            None if stop is None else stop * factor,
        )

    def getDataForLevel(
        self, rows: slice, cols: slice, level: int = 0, copy: bool = True
    ):
        """Returns data from the requested level and level 0 slicing.

        :param slice rows: Requested level of detail 0 slicing
        :param slice cols: Requested level of detail 0 slicing
        :param int level: Level of detail to convert slice to
        :param bool copy: True to copy, False to get internal representation
        :return: Data at given level of detail for given slicing and
           corresponding level 0 slicing.
        :raises ValueError: if requested level of detail is not available
        """
        self.__checkLevel(level)
        lodrows, rows = self.__convertLevel0Slice(rows, level)
        lodcols, cols = self.__convertLevel0Slice(cols, level)

        level0Height, level0Width = self.SHAPE
        xrange = self.XRANGE[1] - self.XRANGE[0]
        x = (self.XRANGE[0] + xrange * cols.start/level0Width,
             self.XRANGE[0] + xrange * cols.stop/level0Width)
        yrange = self.YRANGE[1] - self.YRANGE[0]
        y = (self.YRANGE[0] + yrange * rows.start/level0Height,
             self.YRANGE[0] + yrange * rows.stop/level0Height)

        shape = int(lodrows.stop - lodrows.start), int(lodcols.stop - lodcols.start)

        data = mandelbrot(
            iterations=self.ITERATIONS,
            x=x,
            y=y,
            shape=shape)

        return data, (rows, cols)

    @docstring(items.DataItem)
    def _setVisibleBoundsTracking(self, enable: bool) -> None:
        if not enable:
            raise RuntimeError(
                "This item does not support disabling visible bounds tracking"
            )
        super()._setVisibleBoundsTracking(enable)

    def _addBackendRenderer(self, backend):
        """Update backend renderer"""
        plot = self.getPlot()
        assert plot is not None
        if not self._isPlotLinear(plot):
            # Do not render with non linear scales
            return None

        colormap = self.getColormap()
        if colormap.isAutoscale():
            # Avoid backend to compute autoscale: use item cache
            colormap = colormap.copy()
            colormap.setVRange(*colormap.getColormapRange(self))

        # Compute sub image and offset
        rowSlice, colSlice = self.getVisibleChunkSlices()
        emptySlice = slice(0)
        if rowSlice == emptySlice or colSlice == emptySlice:
            return None  # No data to display

        sx, sy = self.getScale()
        width, height = self.getPlot().getPixelSizeInData()
        elemPerPixel = max(width / sx, height / sy)
        level = int(numpy.ceil(numpy.log2(elemPerPixel))) if elemPerPixel > 1.0 else 0
        level = numpy.clip(level, 0, self._getMaxLevel())
        dataToUse, (rowSlice, colSlice) = self.getDataForLevel(
            rowSlice, colSlice, level, copy=False
        )
        if dataToUse.size == 0:
            return None  # No data to display

        # Offset origin to sub image
        ox, oy = self.getOrigin()
        origin = ox + sx * colSlice.start, oy + sy * rowSlice.start

        return backend.addImage(
            dataToUse,
            origin=origin,
            scale=(sx * 2**level, sy * 2**level),
            colormap=colormap,
            alpha=self.getAlpha(),
        )

    def __visibleBoundsChanged(self):
        """Emit sigVisibleSlicesChanged when slicing has changed."""
        slices = self.getVisibleChunkSlices()
        if slices != self.__previousVisibleSlices:
            self.__previousVisibleSlices = slices
            self._updated(checkVisibility=False)
            self.sigVisibleSlicesChanged.emit()

    def getVisibleSlices(self):
        """Returns the array slicing of the image part inside the plot area.

        This is inclusive in that partly visible array elements are included.

        :returns: (dim0 slice, dim1 slice)
        :rtype: List[slice]
        """
        bounds = self.getVisibleBounds()
        if bounds is None:
            return slice(0), slice(0)  # Empty slicing

        xmin, xmax, ymin, ymax = bounds

        ox, oy = self.getOrigin()
        sx, sy = self.getScale()

        return (
            slice(int((ymin - oy) / sy), int(numpy.ceil((ymax - oy) / sy))),
            slice(int((xmin - ox) / sx), int(numpy.ceil((xmax - ox) / sx))),
        )

    def getChunkShape(self) -> Tuple[float]:
        """Returns current chunk shape (rows, columns).

        :rtype: List[float]
        """
        return self.__chunkShape

    def setChunkShape(self, shape: Tuple[float]):
        """Set the chunk shape (rows, columns).

        :param List[float] shape:
        """
        if shape != self.__chunkShape:
            self.__chunkShape = shape
            self.__visibleBoundsChanged()

    def getVisibleChunkSlices(self):
        """Returns the array slicing of the image aligned to chunks.

        This is inclusive in that partly visible array elements are included.

        :returns: (dim0 slice, dim1 slice)
        :rtype: List[slice]
        """
        yslice, xslice = self.getVisibleSlices()

        emptySlice = slice(0)
        if yslice == emptySlice or xslice == emptySlice:
            return emptySlice, emptySlice  # Nothing to display

        height, width = self.getChunkShape()
        ystart, ystop = yslice.start, yslice.stop
        xstart, xstop = xslice.start, xslice.stop
        return (
            slice(
                height * (ystart // height), height * int(numpy.ceil(ystop / height))
            ),
            slice(width * (xstart // width), width * int(numpy.ceil((xstop / width)))),
        )


if __name__ == "__main__":
    from silx.gui import qt
    import numpy

    qt.QApplication.setAttribute(qt.Qt.AA_ShareOpenGLContexts, True)
    qt.QApplication.setAttribute(qt.Qt.AA_EnableHighDpiScaling, True)

    app = qt.QApplication([])
    w = Plot(backend="gl")
    #w.getYAxis().setInverted(True)
    w.setAxesDisplayed(False)
    w.setKeepDataAspectRatio(True)
    item = MandelbrotSet()
    colormap = w.getDefaultColormap()
    colormap.setVRange(0, 50)
    colormap.setNormalization('log')
    item.setColormap(colormap)

    item.setChunkShape((256, 256))
    w.addItem(item)
    w.resetZoom()
    w.show()

    app.exec_()
