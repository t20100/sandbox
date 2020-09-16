import numpy

from silx.gui.plot import items

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
    if plot is None or bounds is None:
        return None

    xmin, xmax = numpy.clip(bounds[:2], *plot.getXAxis().getLimits())
    yaxis = plot.getYAxis(
        self.getYAxis() if isinstance(self, items.YAxisMixIn) else 'left')
    ymin, ymax = numpy.clip(bounds[2:], *yaxis.getLimits())

    if xmin == xmax or ymin == ymax:  # Outside the plot area
        return None
    else:
        return xmin, xmax, ymin, ymax


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
items.Item.getVisibleExtent = getVisibleExtent
items.ImageBase.getVisibleSlices = getVisibleSlices

