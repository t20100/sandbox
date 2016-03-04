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
__date__ = "05/02/2016"


from collections import defaultdict
import inspect
import logging
import weakref


logging.basicConfig()
logger = logging.getLogger(__name__)


class Notifier(object):
    """Implements a generic notification mechanism."""

    def __init__(self, event_types=None):
        """Init.

        :param event_types: An iterable of event names or None to support
            any event (in this case you can register to an event
            that does not exist).
        """
        if event_types is None:
            self._listeners = defaultdict(list)
        else:  # Limit the supported events
            self._listeners = dict((event, []) for event in event_types)
            self._listeners[None] = []

    @staticmethod
    def _listener_info(listener):
        assert callable(listener)

        if inspect.ismethod(listener):
            # Bound method, store weakref to instance and implementation
            # Taken from Python >= 3.4 weakref.WeakMethod
            instance = listener.__self__
            impl = listener.__func__
            return weakref.ref(instance), weakref.ref(impl), type(listener)
        else:
            return weakref.ref(listener)

    def addListener(self, listener, event=None):
        """Register a listener.

        Adding an already registered listener has no effect.

        :param callable listener: The function or method to register.
        :param str event: The name of the event or None for all events.
        """
        listener_info = self._listener_info(listener)

        if listener_info not in self._listeners[event]:
            self._listeners[event].append(listener_info)
        else:
            logger.warning(
                'Ignoring addition of an already registered listener')

    def removeListener(self, listener, event=None):
        """Remove a previously registered listener.

        Removing a listener that is not registered has no effect.

        :param callable listener: The function or method to unregister.
        :param str event: The name of the event or None for all events.
        """
        if event in self._listeners:
            listener_info = self._listener_info(listener)
            listeners = self._listeners[event]

            try:
                listeners.remove(listener_info)
            except ValueError:
                logger.warning(
                    'Trying to remove a listener that is not registered')

    def notify(self, source=None, event=None, **kwargs):
        """Notify all listeners with the given parameters.

        Listeners are called directly in this method.
        Listeners are called in the order they were registered.

        :param source: The source of the event, if None, source is self.
        :param str event: The name of the event type.
        """
        if source is None:
            source = self

        self._notify(self._listeners[event], source, event, **kwargs)
        self._notify(self._listeners[None], source, event, **kwargs)

    def _notify(self, listeners, source, event, **kwargs):
        for listener_info in listeners[:]:  # Copy list to remove items
            if isinstance(listener_info, tuple):
                # Retrieve bound method info
                instance_ref, impl_ref, method_type = listener_info
                instance = instance_ref()
                if instance is None:
                    listeners.remove(listener_info)
                else:
                    impl = impl_ref()
                    method = method_type(impl, instance)
                    method(source, event, **kwargs)
            else:
                function = listener_info()
                if function is None:
                    listeners.remove(listener_info)
                else:
                    function(source, event, **kwargs)
