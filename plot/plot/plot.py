# -*- coding: utf-8 -*-
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
# ###########################################################################*/
"""Classes describing a plot."""

__authors__ = ["T. Vincent"]
__copyright__ = "ESRF"
__license__ = "MIT"
__date__ = "08/02/2016"


from collections import namedtuple
import logging
import weakref

from . import items, utils


logger = logging.getLogger(__name__)


class Axis(items.Base):
    """Describe a single axis."""

    SCALES = "linear", "log"
    """Supported scales"""

    def __init__(self, label="", scale="linear", limits=(0.0, 1.0), autoscale=False):
        """Init.

        :param str label: Label of the axis
        :param str scale: Scale of the axis in 'linear', 'log'
        :param limits: Start and end values of the axis
        :type limits: 2-tuple of float
        :param bool autoscale: Whether to rescale or not the axis on zoom reset
        """
        super(Axis, self).__init__()
        self._parents = []
        self.label = label
        self.scale = scale
        self.limits = limits
        self.autoscale = autoscale

    @property
    def parents(self):
        """Tuple of Axes using this axis."""
        return tuple(ref() for ref in self._parents)

    def _addParent(self, parent):
        """Add a parent to this Axis, to be used by Axes only.

        It will be removed from the list when the Axes instance is deleted.
        """
        # Not using self._parents.remove directly to have helpful traceback
        self._parents.append(weakref.ref(parent, self._removeParent))

    def _removeParent(self, ref):
        """Callback removing dead parents."""
        self._parents.remove(ref)

    @property
    def autoscale(self):
        """True to reset the axis bounds when reseting the zoom.

        It does not send any event.
        """
        return self._autoscale

    @autoscale.setter
    def autoscale(self, value):
        self._autoscale = bool(value)

    label = items.notifyProperty("_label", str, """Label of the axis.""")

    @property
    def scale(self):
        """Scale of the axis in 'linear', 'log'."""
        return self._scale

    @scale.setter
    def scale(self, value):
        assert value in self.SCALES
        if not hasattr(self, "_scale") or self._scale != value:
            self._scale = value
            self._notifySet("scale", value)

    @property
    def limits(self):
        """Start and end data values of the axis (2-tuple of float)."""
        return self._limits

    @limits.setter
    def limits(self, value):
        assert len(value) == 2
        value = float(value[0]), float(value[1])
        assert value[0] != value[1]
        if not hasattr(self, "_limits") or self._limits != value:
            self._limits = value
            self._notifySet("limits", value)

    @property
    def inverted(self):
        """True if the axis limits are inverted."""
        return self.limits[0] > self.limits[1]

    @property
    def visible(self):
        """An axis is visible if at least one Axes using it is visible."""
        for parent in self.parents:
            if parent.visible:
                return True
        return False


class Axes(items.Base):
    """Describe a pair of X and Y axes and its data content."""

    def __init__(
        self,
        xaxis=None,
        yaxis=None,
        aspectRatio=False,
        visible=True,
        xlabel="",
        xscale="linear",
        xlimits=(0.0, 1.0),
        xautoscale=False,
        ylabel="",
        yscale="linear",
        ylimits=(0.0, 1.0),
        yautoscale=False,
    ):
        """Init.

        :param Axis xaxis: The X axis to use (for shared axis).
        :param Axis yaxis: The Y axis to use (for shared axis).
        """
        super(Axes, self).__init__()
        self._items = []
        self.visible = visible
        self.aspectRatio = aspectRatio

        self._x = (
            xaxis
            if xaxis is not None
            else Axis(label=xlabel, scale=xscale, limits=xlimits, autoscale=xautoscale)
        )
        self._x._addParent(self)
        self._x.addListener(self._axisChanged)

        self._y = (
            yaxis
            if yaxis is not None
            else Axis(label=ylabel, scale=yscale, limits=ylimits, autoscale=yautoscale)
        )
        self._y._addParent(self)
        self._y.addListener(self._axisChanged)

    def _axisChanged(self, source, event, **kwargs):
        if self.visible:
            self.notify(source=source, event=event, **kwargs)  # Broadcast

    visible = items.notifyProperty(
        "_visible",
        bool,
        doc="""Whether the axes are visible or not.

        For shared Axis, the shared axis is hidden only if all Axes are hidden.
        """,
    )

    # Axes

    # TODO: how to handle both axes shared and keep ratio?
    aspectRatio = items.notifyProperty(
        "_aspectRatio",
        bool,
        doc="""True to keep aspect ratio between axes, False otherwise.""",
    )

    # X axis

    @property
    def x(self):
        """The X axis."""
        return self._x

    xlabel = utils.proxyProperty("x", "label")
    xlimits = utils.proxyProperty("x", "limits")
    xscale = utils.proxyProperty("x", "scale")
    xautoscale = utils.proxyProperty("x", "autoscale")
    xinverted = utils.proxyProperty("x", "inverted", setter=False)

    # Y axis

    @property
    def y(self):
        """The y axis."""
        return self._y

    ylabel = utils.proxyProperty("y", "label")
    ylimits = utils.proxyProperty("y", "limits")
    yscale = utils.proxyProperty("y", "scale")
    yautoscale = utils.proxyProperty("y", "autoscale")
    yinverted = utils.proxyProperty("y", "inverted", setter=False)

    # Plot content

    # TODO
    # difference between data and overlay...
    # data bounds

    def addItem(self, item):
        """Add a PlotItem to the plot"""
        item._setParent(self)
        item.addListener(self._itemNeedRedisplay, event="needRedisplay")
        item.addListener(self._itemChanged, event="set")

        self._items.append(item)
        self.notify(event="addItem", item=item)
        if self.visible:
            self.notify(event="needRedisplay")
        return item

    def removeItem(self, item=None):
        """Remove a PlotItem from the plot"""
        if item is None:  # Remove all
            for item in self._items[:]:
                self.removeItem(item)
        else:
            try:
                self._items.remove(item)
            except ValueError:
                logger.warning("Trying to remove an item that is not in the plot")
            else:
                item.removeListener(self._itemNeedRedisplay, event="needRedisplay")
                item.removeListener(self._itemChanged, event="set")
                self.notify(event="removeItem", item=item)
                if self.visible:
                    self.notify(event="needRedisplay")

    def addCurve(self, *args, **kwargs):
        curve = items.Curve(*args, **kwargs)
        self.addItem(curve)
        return curve

    def addImage(self, *args, **kwargs):
        image = items.Image(*args, **kwargs)
        self.addItem(image)
        return image

    def _itemNeedRedisplay(self, source, event, **kwargs):
        """Callback registered on item's needRedisplay event"""
        if self.visible:
            self.notify(source=source, event=event, **kwargs)  # Broadcast

    def _itemChanged(self, source, event, **kwargs):
        """Callback registered on item's set event"""
        self.notify(source=source, event=event, **kwargs)  # Broadcast


class Plot(items.Base):
    """Description of a single plot.

    It has a title, a bottom X axis, a left and a right Y axes.
    """

    def __init__(self, title="", grid="none"):
        """Init.

        :param str title: The main title of the plot.
        :param str grid: The kind of grid in 'none', 'major', 'both'.
        """
        super(Plot, self).__init__()
        self.title = title
        self.grid = grid

        left = Axes()
        right = Axes(xaxis=left.x)  # Twin X
        self._axes = namedtuple("_Axes", ("left", "right"))(left, right)
        left.addListener(self._axesListener)
        right.addListener(self._axesListener)  # TODO issue with twin axis

    title = items.notifyProperty("_title", str, doc="""The main title of the plot.""")

    GRIDS = "none", "major", "both"
    """Supported grid types"""

    @property
    def grid(self):
        """The type of grid to display in 'none', 'major', 'both'."""
        return self._grid

    @grid.setter
    def grid(self, value):
        assert value in self.GRIDS
        if not hasattr(self, "_grid") or self._grid != value:
            self._grid = value
            self._notifySet("grid", value)

    @property
    def axes(self):
        """The Axes of this plot"""
        return self._axes

    @property
    def defaultAxes(self):
        """Left and bottom axes"""
        return self._axes[0]

    def _axesListener(self, source, event, **kwargs):
        self.notify(source=source, event=event, **kwargs)  # Broadcast

    # Proxies to default axes

    visible = utils.proxyProperty("defaultAxes", "visible")
    aspectRatio = utils.proxyProperty("defaultAxes", "aspectRatio")

    xlabel = utils.proxyProperty("defaultAxes", "xlabel")
    xlimits = utils.proxyProperty("defaultAxes", "xlimits")
    xscale = utils.proxyProperty("defaultAxes", "xscale")
    xautoscale = utils.proxyProperty("defaultAxes", "xautoscale")
    xinverted = utils.proxyProperty("defaultAxes", "xinverted", setter=False)

    ylabel = utils.proxyProperty("defaultAxes", "ylabel")
    ylimits = utils.proxyProperty("defaultAxes", "ylimits")
    yscale = utils.proxyProperty("defaultAxes", "yscale")
    yautoscale = utils.proxyProperty("defaultAxes", "yautoscale")
    yinverted = utils.proxyProperty("defaultAxes", "yinverted", setter=False)

    def addItem(self, *args, **kwargs):
        return self.defaultAxes.addItem(*args, **kwargs)

    def removeItem(self, *args, **kwargs):
        self.defaultAxes.removeItem(*args, **kwargs)

    def addCurve(self, *args, **kwargs):
        return self.defaultAxes.addCurve(*args, **kwargs)

    def addImage(self, *args, **kwargs):
        return self.defaultAxes.addImage(*args, **kwargs)
