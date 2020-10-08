from typing import Tuple

from silx.gui import qt
from silx.gui.plot import items, PlotWindow

#import os
#import sys
#sys.path.insert(0, os.path.dirname(__file__))
#import silx_monkey_patch

class Image(items.ImageData):

    sigVisibleSlicesChanged = qt.Signal()
    """Signal emitted when the visible slices of the array has changed."""

    def __init__(self):
        self.__previousVisibleSlices = slice(0), slice(0)
        self.__chunkShape = 1, 1
        super().__init__()
        self._sigVisibleExtentChanged.connect(self.__visibleExtentChanged)

    def __visibleExtentChanged(self):
        """Emit sigVisibleSlicesChanged when slicing has changed."""
        slices = self.getVisibleChunkSlices()
        if slices != self.__previousVisibleSlices:
            self.__previousVisibleSlices = slices
            self.sigVisibleSlicesChanged.emit()

    def getVisibleSlices(self):
        """Returns the array slicing of the image part inside the plot area.

        This is inclusive in that partly visible array elements are included.

        :returns: (dim0 slice, dim1 slice)
        :rtype: List[slice]
        """
        extent = self.getVisibleExtent()
        if extent is None:
            return slice(0), slice(0)  # Empty slicing

        xmin, xmax, ymin, ymax = extent

        ox, oy = self.getOrigin()
        sx, sy = self.getScale()

        return (slice(int((ymin - oy) / sy), int(numpy.ceil((ymax - oy) / sy))),
                slice(int((xmin - ox) / sx), int(numpy.ceil((xmax - ox) / sx))))

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
            self.__visibleExtentChanged()

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
        return (slice(height * (ystart // height),
                      height * int(numpy.ceil(ystop / height))),
                slice(width * (xstart // width),
                      width * int(numpy.ceil((xstop / width)))))


if __name__ == "__main__":
    from silx.gui import qt
    import numpy

    qt.QApplication.setAttribute(qt.Qt.AA_ShareOpenGLContexts, True)
    qt.QApplication.setAttribute(qt.Qt.AA_EnableHighDpiScaling, True)

    app = qt.QApplication([])
    w = PlotWindow(backend='gl')
    w.setKeepDataAspectRatio(True)
    item = Image()
    item._setVisibleExtentTracking(True)

    def cb():
        print('Chunked slices', item.getVisibleChunkSlices())
        #print('Extent', item.getVisibleExtent())
        #print('Slices', item.getVisibleSlices())
        #width, height = item.getPlot().getPixelSizeInData()
        #print('Pixel size', width, height)
        #sx, sy = item.getScale()
        #print('Array size', width / sx, height / sy)
    item.sigVisibleSlicesChanged.connect(cb)
    #item._sigVisibleExtentChanged.connect(cb)

    item.setScale((1, 2))
    item.setData(numpy.arange(100).reshape(10, 10))
    item.setChunkShape((5, 5))
    #item.setData(numpy.arange(1024**2, dtype='float32').reshape(1024, 1024))
    w.addItem(item)
    w.resetZoom()
    w.show()
    app.exec_()
