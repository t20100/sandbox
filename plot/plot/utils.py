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
"""Base class for a generic event notification/listener system."""

__authors__ = ["T. Vincent"]
__copyright__ = "ESRF"
__license__ = "MIT"
__date__ = "08/02/2016"


import logging


logger = logging.getLogger(__name__)


def proxyProperty(component, attribute, setter=True, doc=None):
    """Create a property that wraps an attribute of an attribute.

    Useful for composition.

    :param str component: The name of the component attribute.
    :param str attribute: The name of attribute of the attribute to wrap.
    :param bool setter: True to provide a setter, False for read-only property.
    :param str doc: The docstring of the property.
    :return: A property
    """

    def getter(self):
        instance = getattr(self, component)
        return getattr(instance, attribute)

    if not setter:
        return property(getter, doc=doc)

    else:

        def setter(self, value):
            instance = getattr(self, component)
            setattr(instance, attribute, value)

        return property(getter, setter, doc=doc)
