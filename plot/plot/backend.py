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
"""Protocol to provide a plot backend as a delegate of a Plot instance."""

__authors__ = ["T. Vincent"]
__copyright__ = "ESRF"
__license__ = "MIT"
__date__ = "08/02/2016"


import logging
import weakref


logging.basicConfig()
logger = logging.getLogger(__name__)


class Backend(object):
    """Delegate of a Plot instance performing the drawing."""

    def __init__(self, plot):
        """Init.

        :param plot: The plot for which to perform actions.
        """
        self._plot = weakref.ref(plot)
        self._changes = []
        self._needRedisplay = False

        # TODO init from description

        plot.addListener(self._needRedisplayListener, event="needRedisplay")
        plot.addListener(self._setListener, event="set")
        plot.addListener(self._itemsListener, event="addItem")
        plot.addListener(self._itemsListener, event="removeItem")

    def triggerRedisplay(self):
        pass

    @property
    def plot(self):
        """The plot this backend is the delegate of."""
        return self._plot()

    @property
    def needRedisplay(self):
        return self._needRedisplay

    @needRedisplay.setter
    def needRedisplay(self, value):
        value = bool(value)
        if self._needRedisplay != value:
            self._needRedisplay = value
            if value:
                self.triggerRedisplay()
            else:  # Reset change log
                self._changes = []

    def _needRedisplayListener(self, source, event, **kwargs):
        self.needRedisplay = True

    def _setListener(self, source, event, attr, value, **kwargs):
        self._changes.append(
            {"event": event, "source": source, "attr": attr, "value": value}
        )

    def _itemsListener(self, source, event, item, **kwargs):
        self._changes.append({"event": event, "source": source, "item": item})

    def draw(self):
        """Perform the rendering."""
        self.needRedisplay = False

    def pick(self, x, y):
        """Perform the picking"""
        pass
