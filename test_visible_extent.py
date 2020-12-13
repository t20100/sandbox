from typing import Optional, Tuple

from silx.utils.proxy import docstring
from silx.gui import qt
from silx.gui.plot import items, PlotWindow

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import silx_monkey_patch

# TODO for live update of the HDF5 file:
# - make a h5py LevelOfDetailImageData that closes the file each time + no file locking
# - update at regular interval

# TODO pythonic slice accessor?, asynchronous
class LevelOfDetailImageData:
    """Multi-resolution image data accessor

     Provides access to a pyramid of images:
     Level of detail 0 gives access to the full resolution image.
     Level of detail 1 to data binned 2x2, and so on

    :param List[numpy.ndarray] data: Pyramid of image data.
    """

    def __init__(self, data):
        self.__lods = data

    def getMaxLevel(self) -> Optional[int]:
        """Returns the maximum available level of detail.

        :rtype: Union[int,None]
        """
        return len(self.__lods) - 1 if self.__lods else None

    def __checkLevel(self, level: int) -> None:
        """Check if provided level of detail is valid

        :param int level: Level of detail
        :raises ValueError: if requested level of detail is not available
        """
        maxLevel = self.getMaxLevel()
        if maxLevel is None or not 0 <= level <= maxLevel:
            raise ValueError("Requested level of detail is not available")

    def getData(self, level: int = 0, copy: bool = True):
        """Returns data array for selected level of detail

        :param int level: Level of detail
        :param bool copy: True to copy, False to get internal representation.
        :rtype: Union[numpy.ndarray,h5py.Dataset]
        :raises ValueError: if requested level of detail is not available
        """
        self.__checkLevel(level)
        data = self.__lods[level]
        return numpy.array(data, copy=True) if copy else data

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
        :return: Data at given level of detail for given slicing and
           corresponding level 0 slicing.
        :raises ValueError: if requested level of detail is not available
        """
        self.__checkLevel(level)
        lodrows, rows = self.__convertLevel0Slice(rows, level)
        lodcols, cols = self.__convertLevel0Slice(cols, level)
        data = self.__lods[level]
        return numpy.array(data[lodrows, lodcols], copy=copy), (rows, cols)


class Image(items.ImageData):

    sigVisibleSlicesChanged = qt.Signal()
    """Signal emitted when the visible slices of the array has changed."""

    def __init__(self):
        self.__loddata = LevelOfDetailImageData(
            [numpy.array((0, 0), dtype=numpy.float32)]
        )
        self.__previousLevelOfDetail = -1
        self.__previousVisibleSlices = slice(0), slice(0)
        self.__chunkShape = 1, 1
        super().__init__()
        self._sigVisibleBoundsChanged.connect(self.__visibleBoundsChanged)
        self._setVisibleBoundsTracking(True)

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

    def _getLevelOfDetail(self) -> int:
        """Returns current level of detail (0 for full resolution)"""
        plot = self.getPlot()
        if plot is None:
            return 0

        sx, sy = self.getScale()
        width, height = plot.getPixelSizeInData()
        elemPerPixel = max(width / sx, height / sy)
        level = int(numpy.ceil(numpy.log2(elemPerPixel))) if elemPerPixel > 1.0 else 0
        return numpy.clip(level, 0, self.__loddata.getMaxLevel())

    def getData(self, copy=True):
        """Returns the image data

        :param bool copy: True (Default) to get a copy,
                          False to use internal representation (do not modify!)
        :rtype: Union[numpy.ndarray,h5py.Dataset]
        """
        return self.__loddata.getData(copy=copy)

    def setData(self, data):
        """Set the level of detail image data

        :param List[numpy.ndarray] data:
        """
        self.__loddata = LevelOfDetailImageData(data)
        self._visibleBoundsChanged()
        self._updated(items.ItemChangedType.DATA)

    @docstring(items.ImageData)
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
        level = numpy.clip(level, 0, self.__loddata.getMaxLevel())
        dataToUse, (rowSlice, colSlice) = self.__loddata.getDataForLevel(
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
            colormap=colormap if dataToUse.ndim == 2 else None,
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
    from silx.gui.plot.AlphaSlider import ActiveImageAlphaSlider
    import numpy
    import h5py
    import sys

    filename = sys.argv[1]
    bg_filename = sys.argv[2] if len(sys.argv) == 3 else None

    qt.QApplication.setAttribute(qt.Qt.AA_ShareOpenGLContexts, True)
    qt.QApplication.setAttribute(qt.Qt.AA_EnableHighDpiScaling, True)

    app = qt.QApplication([])
    plot = PlotWindow(backend="gl")
    #w.getYAxis().setInverted(True)
    #w.setAxesDisplayed(False)
    plot.setKeepDataAspectRatio(True)
    item = Image()
    colormap = plot.getDefaultColormap()
    colormap.setVRange(-0.1, 0.3)
    item.setColormap(colormap)

    f = h5py.File(filename, mode="r")
    lods = [f['level%d' % i] for i in range(8) if ('level%d' % i) in f.keys()]
    item.setData(lods)

    item.setChunkShape((256, 256))
    plot.addItem(item)

    if bg_filename is not None:
        bgfile = h5py.File(bg_filename, mode="r")
        lods = [bgfile['level%d' % i] for i in range(8) if ('level%d' % i) in bgfile.keys()]
        bgitem = Image()
        bgitem.setName("Background")
        bgitem.setZValue(-1)
        bgitem.setData(lods)
        bgitem.setChunkShape((256, 256))
        plot.addItem(bgitem)

    plot.setActiveImage(item.getName())
    plot.resetZoom()

    alphaSlider = ActiveImageAlphaSlider(plot=plot)
    alphaSlider.show()

    window = qt.QMainWindow()
    window.setCentralWidget(plot)
    alphaDock = qt.QDockWidget()
    alphaDock.setWidget(alphaSlider)
    window.addDockWidget(qt.Qt.LeftDockWidgetArea, alphaDock)
    window.show()
    app.exec_()
