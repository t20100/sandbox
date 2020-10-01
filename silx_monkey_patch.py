import numpy

from silx.gui.plot import PlotWidget
from silx.gui.plot import items


# silx.gui.plot.PlotWidget

# TODO support for log scale?
# by providing a position or by giving the max and/or min.
def getPixelSizeInData(self, axis='left'):
    """Returns the size of a pixel in plot data coordinates

    :param str axis: Y axis to use in: 'left' (default), 'right'
    :return:
        Size (width, height) of a Qt pixel in data coordinates.
        Size is None if it cannot be computed
    :rtype: Union[List[float],None]
    """
    assert axis in ('left', 'right')

    xaxis = self.getXAxis()
    yaxis = self.getYAxis(axis)

    if (xaxis.getScale() != items.Axis.LINEAR or
                yaxis.getScale() != items.Axis.LINEAR):
        raise RuntimeError("Only available with linear axes")

    xmin, xmax = xaxis.getLimits()
    ymin, ymax = yaxis.getLimits()
    width, height = self.getPlotBoundsInPixels()[2:]
    if width == 0 or height == 0:
        return None
    else:
        return (xmax - xmin) / width, (ymax - ymin) / height


# Monkey-patching
PlotWidget.getPixelSizeInData = getPixelSizeInData


# silx.gui.plot.items.core class Items

def getVisibleExtent(self):
    """Returns visible extent of the item bounding box in the plot area.

    :returns:
        (xmin, xmax, ymin, ymax) in data coordinates of the visible area or 
        None if item is not visible in the plot area.
    :rtype: Union[List[float],None]
    """
    plot = self.getPlot()
    bounds = self.getBounds()
    if plot is None or bounds is None or not self.isVisible():
        return None

    xmin, xmax = numpy.clip(bounds[:2], *plot.getXAxis().getLimits())
    yaxis = plot.getYAxis(
        self.getYAxis() if isinstance(self, items.YAxisMixIn) else 'left')
    ymin, ymax = numpy.clip(bounds[2:], *yaxis.getLimits())

    if xmin == xmax or ymin == ymax:  # Outside the plot area
        return None
    else:
        return xmin, xmax, ymin, ymax

# Monkey-patching
items.Item.getVisibleExtent = getVisibleExtent


# silx.gui.plot.items.image class ImageBase

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

# Monkey-patching
items.ImageBase.getVisibleSlices = getVisibleSlices
