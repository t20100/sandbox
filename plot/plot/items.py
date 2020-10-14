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
"""Base classes for items of the plot."""

__authors__ = ["T. Vincent"]
__copyright__ = "ESRF"
__license__ = "MIT"
__date__ = "05/02/2016"


import logging
import weakref

import numpy

from . import event

logger = logging.getLogger(__name__)


# Plot event system base ######################################################


class Base(event.Notifier):
    """Base class for classes of plot components.

    Enable usage of :func:`notifyProperty`."""

    def _notifySet(self, attr, value, **kwargs):
        """Send notifications upon property changes.

        Intended to be used by :func:`notifyProperty` and derived classes
        notifying properties.

        :param str attr: The attribute name that was set
        :param value: The new value
        """
        self.notify(event="set", attr=attr, value=value, **kwargs)
        if attr == "visible" or getattr(self, "visible", True):
            self.notify(event="needRedisplay")


def notifyProperty(name, type_=None, doc=None):
    """Property calling :method:`_notifySet` upon changes.

    Intended to be used by :class:`PlotItem' and derived classes.

    :param str name: The name of the attribute to wrap.
    :param type type_: Type of the attribute.
    :return: A property
    """

    def getter(self):
        return getattr(self, name)

    if type_ is not None:

        def setter(self, value):
            value = type_(value)
            if not hasattr(self, name) or value != getattr(self, name):
                setattr(self, name, value)
                self._notifySet(name.lstrip("_"), value)

    else:

        def setter(self, value):
            if not hasattr(self, name) or value != getattr(self, name):
                setattr(self, name, value)
                self._notifySet(name.lstrip("_"), value)

    return property(getter, setter, doc=doc)


# Items #######################################################################


class PlotItem(Base):
    """Base class for items that can be rendered in a plot"""

    def __init__(self, z=0, selectable=False, draggable=False, visible=True):
        """Init.

        :param int z: The rendering layer to which the item belongs.
        :param bool selectable: Whether this item is selectable or not.
        :param bool draggable: Whether this item is draggable or not.
        :param bool visible: Whether this item is visible or not.
        """
        self._parentRef = None
        super(PlotItem, self).__init__()
        self.z = z
        self.selectable = selectable
        self.draggable = draggable
        self.visible = visible
        self.origin = 0.0, 0.0
        self.scale = 1.0, 1.0

    @property
    def parent(self):
        """The PlotContent this item is attached to or None."""
        return self._parentRef()

    def _setParent(self, parent=None):
        """Set the parent of this item, to be used by PlotContent only.

        It will be reset when the PlotContent is deleted.
        """
        if parent is None:  # Reset
            self._parentRef = None
        elif self._parentRef is not None:
            logger.warning(
                "This PlotItem already belongs to a Plot, cannot set parent."
            )
        else:
            self._parentRef = weakref.ref(parent, self._resetParent)

    def _resetParent(self, ref):
        self._parentRef = None

    z = notifyProperty(
        "_z", int, """The rendering layer to which the item belongs to."""
    )

    selectable = notifyProperty(
        "_selectable", bool, """Bool, True if the item is selectable."""
    )

    draggable = notifyProperty(
        "_draggable", bool, """Bool, True if the item is draggable."""
    )

    visible = notifyProperty("_visible", bool, """Bool, True if the item is visible.""")

    @property
    def origin(self):
        """(ox, oy) origin of the data in the plot."""
        return self._origin

    @origin.setter
    def origin(self, value):
        assert len(value) == 2
        value = (float(value[0]), float(value[1]))
        if not hasattr(self, "_origin") or value != self._origin:
            self._origin = value
            self._notifySet("origin", value)

    @property
    def scale(self):
        """(sx, sy) scale of the data in the plot."""
        return self._scale

    @scale.setter
    def scale(self, value):
        assert len(value) == 2
        value = (float(value[0]), float(value[1]))
        if not hasattr(self, "_scale") or value != self._scale:
            self._scale = value
            self._notifySet("scale", value)

    @property
    def bounds(self):
        """The Plot item bounding box (aligned with the axes)"""
        return None  # TODO


# TODO check vbegin, vend for log norm
class Colormap(event.Notifier):
    """Description of a colormap"""

    DEFAULTS = {"cmap": "grey", "norm": "linear", "vbegin": None, "vend": None}

    def __init__(self, cmap=None, norm=None, vbegin=None, vend=None):
        """Init.

        :param cmap: Name of the colormap.
        :param str norm: The normalization to apply in 'linear', 'log'.
        :param vbegin: Value of the beginning of the colormap or
                       None for autoscale.
        :param vend: Value of the end of the colormap or
                     None for autoscale.
        """
        super(Colormap, self).__init__()

        self.cmap = cmap if cmap is not None else self.DEFAULTS["cmap"]
        self.norm = norm if norm is not None else self.DEFAULTS["norm"]
        self.vbegin = vbegin if vbegin is not None else self.DEFAULTS["vbegin"]
        self.vend = vend if vend is not None else self.DEFAULTS["vend"]

    @classmethod
    def toColormap(cls, desc):
        """Convert a Colormap, a dict or a str to a Colormap instance."""
        if isinstance(desc, Colormap):
            return desc
        elif isinstance(desc, dict):
            cmap = desc.get("cmap", cls.DEFAULT["cmap"])
            norm = desc.get("norm", cls.DEFAULT["norm"])
            vbegin = desc.get("vbegin", cls.DEFAULT["vbegin"])
            vend = desc.get("vend", cls.DEFAULT["vend"])
            return Colormap(cmap, norm, vbegin, vend)
        elif isinstance(desc, str):
            if desc in ("linear", "log"):
                return Colormap(norm=desc)
            else:
                return Colormap(cmap=desc)

    @property
    def cmap(self):
        """Name of the colormap."""
        return self._cmap

    @cmap.setter
    def cmap(self, value):
        cmap = str(value)
        if not hasattr(self, "_cmap") or self._cmap != cmap:
            self._cmap = cmap
            self.notify(event="set", attr="cmap", value=cmap)

    @property
    def vbegin(self):
        """Value of the beginning of the colormap or None for autoscale."""
        return self._vbegin

    @vbegin.setter
    def vbegin(self, value):
        if not hasattr(self, "_vbegin") or self._vbegin != value:
            self._vbegin = value
            self.notify(event="set", attr="vbegin", value=value)

    @property
    def vend(self):
        """Value of the end of the colormap or None for autoscale."""
        return self._vend

    @vend.setter
    def vend(self, value):
        if not hasattr(self, "_vend") or self._vend != value:
            self._vend = value
            self.notify(event="set", attr="vend", value=value)

    @property
    def norm(self):
        """The normalization to apply in 'linear', 'log'."""
        return self._norm

    @norm.setter
    def norm(self, value):
        assert value in ("linear", "log")
        if not hasattr(self, "_norm") or self._norm != value:
            self._norm = value
            self.notify(event="set", attr="norm", value=value)

    @property
    def lut(self):
        """The color look-up table."""
        return None  # TODO return an array

    def apply(self, value):
        """Convert a value or an array of values to uint8 RGBA.

        For arrays, the resulting array has an additional dimension to the
        input one.
        """
        return None  # TODO


class Image(PlotItem):
    """2D dataset, either 2D array of 3D array for RGB(A) images."""

    def __init__(
        self,
        data,
        copy=True,
        colormap=None,
        origin=(0.0, 0.0),
        scale=(1.0, 1.0),
        z=0,
        selectable=False,
        draggable=False,
        visible=True,
    ):
        super(Image, self).__init__(z, selectable, draggable, visible)
        self._colormap = None  # Init private attribute for setter to work
        if colormap is None:
            colormap = Colormap.DEFAULTS["cmap"]
        self.colormap = colormap
        self.origin = origin
        self.scale = scale
        self.setData(data, copy)

    def getData(self, copy=True):
        """Returns the data.

        :param bool copy: Whether to return a copy (the default) or the
            internal array (that should be considered read-only).
        """
        return numpy.array(self._data, copy=copy)

    def setData(self, data, copy=True):
        """Update the data.

        :param numpy.ndarray data: 2D array of values or
            3D array for RGB(A) images.
        :param bool copy: Whether to use a copy (the default) or the
            provided array.
        """
        data = numpy.array(data, copy=copy)

        assert len(data.shape) in (2, 3)
        if len(data.shape) == 3:
            assert data.shape[2] in (3, 4)
            assert data.dtype in (numpy.uint8,)

        self._data = data
        self._notifySet("data", self._data)

    @property
    def colormap(self):
        """Colormap to use."""
        return self._colormap

    @colormap.setter
    def colormap(self, value):
        value = Colormap.toColormap(value)
        if value != self._colormap:
            if self._colormap is not None:
                self._colormap.removeListener(self._colormapListener, event="set")

            self._colormap = value

            if self._colormap is not None:
                self._colormap.addListener(self._colormapListener, event="set")

            self._notifySet("colormap", value)

    def _colormapListener(self, source, event, **kwargs):
        """Listener of colormap to broadcast colormap changes."""
        # TODO: This is a coarse update message
        self.notifySet("colormap", self.colormap)


# TODO: a value + colormap variant?, separate class for scatter plot?
class Curve(PlotItem):
    """A single 1D curve as a set of 2D points.

    It supports error bars, display as lines or markers.
    """

    DEFAULTS = {
        "marker": "o",
        "linestyle": "-",
        "linewidth": 1.0,
    }

    def __init__(
        self,
        x=None,
        y=None,
        xerror=None,
        yerror=None,
        color=(0.0, 0.0, 0.0),
        copy=True,
        marker=None,
        linewidth=None,
        linestyle=None,
        z=0,
        selectable=False,
        draggable=False,
        visible=True,
    ):
        super(Curve, self).__init__(z, selectable, draggable, visible)
        self.setData(x, y, copy=copy)
        self.setXerror(xerror, copy=copy)
        self.setYerror(yerror, copy=copy)

        self.color = color
        self.marker = marker if marker is not None else self.DEFAULTS["marker"]
        self.linewidth = (
            linewidth if linewidth is not None else self.DEFAULTS["linewidth"]
        )
        self.linestyle = (
            linestyle if linestyle is not None else self.DEFAULTS["linestyle"]
        )

    marker = notifyProperty("_marker", str, doc="Type of markers symbol in:")

    linewidth = notifyProperty("_linewidth", float, doc="Width of line in pixels.")

    linestyle = notifyProperty("_linestyle", str, doc="Style of line in: _, ., None.")

    @property
    def color(self):
        """Color of the curve."""
        return self._color

    @color.setter
    def color(self, value):
        # TODO support str colors + array of one color per point + RGB(A)
        assert len(value) == 3
        value = (float(value[0]), float(value[1]), float(value[2]))
        if not hasattr(self, "_color") or value != self._color:
            self._color = value
            self._notifySet("color", value)

    def getData(self, copy=True):
        """Return x and y data.

        :param bool copy: Whether to return a copy (the default) or
            the interal arrays (to be considered read-only).
        :returns: (x, y) data.
        :rtype: 2-tuple of numpy array
        """
        return numpy.array(self._x, copy=copy), numpy.array(self._y, copy=copy)

    def setData(self, x=None, y=None, copy=True):
        """Set the data.

        If a single array is provided, x coords are computed:
        set_data((1, 2, 3)) => set_data(x=(0, 1, 2), y=(1, 2, 3))

        :param numpy.array x: 1D array of x coords.
        :param numpy.array y: 1D array of y coords.
        :param bool copy: Whether to copy the data or not.
        """
        # Convert to numpy array
        if x is not None:
            x = numpy.array(x, copy=copy)
        if y is not None:
            y = numpy.array(y, copy=copy)

        # Deals with None data
        if x is None and y is None:
            x, y = numpy.array([]), numpy.array([])
        elif x is None:
            x, y = numpy.arange(len(y)), y
        elif y is None:
            x, y = numpy.arange(len(x)), x

        assert len(x.shape) == 1
        assert len(y.shape) == 1
        assert len(x) == len(y)

        self._y = y
        self._x = x
        self._notifySet("data", (x, y), x=x, y=y)

    def setXerror(self, xerror, copy=True):
        """Set errorbars along the x axis."""
        # TODO check and support multiple types
        self._xerror = numpy.array(xerror, copy=copy)
        self._notifySet("xerror", self._xerror)

    def setYerror(self, yerror, copy=True):
        """Set errorbars along the y axis."""
        # TODO check and support multiple types
        self._yerror = numpy.array(yerror, copy=copy)
        self._notifySet("yerror", self._yerror)


class Shape(PlotItem):
    """2D vector line and fill"""

    def __init__(self):
        super(Shape, self).__init__()
