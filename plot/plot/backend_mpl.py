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
"""Plot backend implemented over matplotlib."""

__authors__ = ["V. A. Sole", "T. Vincent"]
__copyright__ = "ESRF"
__license__ = "MIT"
__date__ = "09/02/2016"


import logging

from .backend import Backend
from . import items, plot


import matplotlib

# TODO checks for mpl backend
matplotlib.rcParams["backend"] = "Qt4Agg"

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from matplotlib.image import AxesImage
from matplotlib import cm
from matplotlib.colors import LogNorm, Normalize

from PyQt4 import QtCore, QtGui


logger = logging.getLogger(__name__)


class BackendMPL(FigureCanvas, Backend):
    """matplotlib backend"""

    _signalRedisplay = QtCore.pyqtSignal()  # PyQt binds it to instances

    def __init__(self, plot, parent=None, **kwargs):
        Backend.__init__(self, plot)

        self.fig = Figure()
        self.fig.set_facecolor("w")
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(
            self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding
        )

        self._items = {}  # Mapping: plot item -> matplotlib item

        # Set-up axes
        leftAxes = self.fig.add_axes([0.15, 0.15, 0.75, 0.75], label="left")
        rightAxes = leftAxes.twinx()
        rightAxes.set_label("right")

        # critical for picking!!!!
        rightAxes.set_zorder(0)
        rightAxes.set_autoscaley_on(True)
        leftAxes.set_zorder(1)
        # this works but the figure color is left
        leftAxes.set_axis_bgcolor("none")
        self.fig.sca(leftAxes)

        self._axes = {self.plot.axes.left: leftAxes, self.plot.axes.right: rightAxes}

        # Sync matplotlib and plot axes
        for plotAxes, mplAxes in self._axes.items():
            self._syncAxes(mplAxes, plotAxes)

        # TODO sync all the plot items to support backend switch !

        # Set-up events

        self.fig.canvas.mpl_connect("button_press_event", self.onMousePressed)
        self.fig.canvas.mpl_connect("button_release_event", self.onMouseReleased)
        self.fig.canvas.mpl_connect("motion_notify_event", self.onMouseMoved)
        self.fig.canvas.mpl_connect("scroll_event", self.onMouseWheel)

        # Connect draw to redisplay
        self._signalRedisplay.connect(self.draw, QtCore.Qt.QueuedConnection)

    @staticmethod
    def _syncAxes(mplAxes, plotAxes):
        """Sync matplotlib Axes with the plot Axes"""
        mplAxes.set_xlabel(plotAxes.xlabel)
        mplAxes.set_xlim(plotAxes.xlimits)
        mplAxes.set_xscale(plotAxes.xscale)

        mplAxes.set_ylabel(plotAxes.ylabel)
        mplAxes.set_ylim(plotAxes.ylimits)
        mplAxes.set_yscale(plotAxes.yscale)

    def triggerRedisplay(self):
        self._signalRedisplay.emit()

    def draw(self):
        # Apply all modifications before redraw
        for change in self._changes:
            if change["event"] == "addItem":
                self._addItem(change["source"], change["item"])
            elif change["event"] == "removeItem":
                self._removeItem(change)
            elif change["event"] == "set":
                self._setAttr(change["source"], change["attr"], change["value"])
            else:
                logger.warning("Unhandled event %s" % change["event"])

        Backend.draw(self)
        FigureCanvas.draw(self)

    def onMousePressed(self, event):
        pass  # TODO

    def onMouseMoved(self, event):
        pass  # TODO

    def onMouseReleased(self, event):
        pass  # TODO

    def onMouseWheel(self, event):
        pass  # TODO

    def _addItem(self, axes, item):
        mplAxes = self._axes[axes]

        if isinstance(item, items.Curve):
            x, y = item.getData(copy=False)
            line = Line2D(
                xdata=x,
                ydata=y,
                color=item.color,
                marker=item.marker,
                linewidth=item.linewidth,
                linestyle=item.linestyle,
                zorder=item.z,
            )
            # TODO error bars, scatter plot..
            # TODO set picker
            mplAxes.add_line(line)
            self._items[item] = line

        elif isinstance(item, items.Image):
            # TODO ModestImage, set picker
            data = item.getData(copy=False)

            if len(data.shape) == 3:  # RGB(A) images
                image = AxesImage(mplAxes, origin="lower", interpolation="nearest")
            else:  # Colormap
                # TODO use own colormaps
                cmap = cm.get_cmap(item.colormap.cmap)
                if item.colormap.norm == "log":
                    norm = LogNorm(item.colormap.vbegin, item.colormap.vend)
                else:
                    norm = Normalize(item.colormap.vbegin, item.colormap.vend)
                image = AxesImage(
                    mplAxes,
                    origin="lower",
                    cmap=cmap,
                    norm=norm,
                    interpolation="nearest",
                )
            image.set_data(data)
            image.set_zorder(item.z)

            height, width = data.shape[0:2]
            xmin, ymin = item.origin
            xmax = xmin + item.scale[0] * width
            ymax = xmax + item.scale[1] * height

            # set extent (left, right, bottom, top)
            if image.origin == "upper":
                image.set_extent((xmin, xmax, ymax, ymin))
            else:
                image.set_extent((xmin, xmax, ymin, ymax))

            mplAxes.add_artist(image)
            self._items[item] = image

        else:
            logger.warning("Unsupported item type %s" % str(type(item)))

    def _removeItem(self, axes, item):
        mplItem = self._items.pop(item)
        mplItem.remove()

    def _setAttr(self, obj, attr, value):
        if isinstance(obj, plot.Axis):
            plotAxes = obj.parents[0]
            if obj == plotAxes.x:
                direction = "x"
            elif obj == plotAxes.y:
                direction = "y"
            else:
                logging.warning("Incoherent axes information.")
                return

            mplAxes = self._axes[plotAxes]

            if attr == "label":
                if direction == "x":
                    mplAxes.set_xlabel(value)
                else:
                    mplAxes.set_ylabel(value)

            elif attr == "scale":
                if direction == "x":
                    mplAxes.set_xscale(value)
                else:
                    mplAxes.set_yscale(value)

            elif attr == "limits":
                if direction == "x":
                    mplAxes.set_xlim(value)
                else:
                    mplAxes.set_ylim(value)

            else:
                logger.warning("Unsupported attribute %s" % attr)

        elif isinstance(obj, plot.Axes):
            mplAxes = self._axes[obj]

            if attr == "visible":
                # For twin axes, Axes can be not visible but Axis is visible
                # So use Axis (and not Axes) visible value.
                mplAxes.get_xaxis().set_visible(obj.x.visible)
                mplAxes.get_yaxis().set_visible(obj.y.visible)

            elif attr == "aspectRatio":
                mplAxes.set_aspect("equal" if value else "auto")

            else:
                logger.warning("Unsupported attribute %s" % attr)

        elif isinstance(obj, plot.Plot):
            leftAxes = self._axes[self.plot.axes.left]

            if attr == "title":
                # Set title on left axes which should not be hidden
                leftAxes.set_title(value)

            elif attr == "grid":
                leftAxes.grid(which=value)

            else:
                logger.warning("Unsupported attribute %s" % attr)

        elif isinstance(obj, items.Curve):  # TODO
            logger.warning("Unsupported item type %s" % str(type(obj)))

        elif isinstance(obj, items.Image):  # TODO
            logger.warning("Unsupported item type %s" % str(type(obj)))

        else:
            logger.warning("Unsupported item type %s" % str(type(obj)))
