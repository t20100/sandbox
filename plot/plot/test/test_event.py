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
"""Test for event module."""

__authors__ = ["T. Vincent"]
__copyright__ = "ESRF"
__license__ = "MIT"
__date__ = "05/02/2016"


import unittest

from .. import event


class TestNotifier(unittest.TestCase):
    """Tests for Notifier class"""

    def setUp(self):
        self.notifier = event.Notifier()  # Notifier for test
        self.notifications = []  # List of received notifications

    def tearDown(self):
        del self.notifier
        del self.notifications

    def listener(self, source, event, **kwargs):
        """Listener method used for tests"""
        self.notifications.append((source, event, kwargs))

    def testListenerFunction(self):
        """Function as a listener:

        Register, send an event, unregister, send another event."""

        def callback(source, event, **kwargs):
            self.listener(source, event, **kwargs)

        self.notifier.addListener(callback)
        self.notifier.notify(event="test", value=1)
        self.notifier.removeListener(callback)
        self.notifier.notify(event="test", value=2)

        self.assertEqual(len(self.notifications), 1)
        self.assertEqual(self.notifications[0], (self.notifier, "test", {"value": 1}))

    def testListenerMethod(self):
        """Method as a listener:

        Register, send an event, unregister, send another event."""
        self.notifier.addListener(self.listener)
        self.notifier.notify(event="test", value=1)
        self.notifier.removeListener(self.listener)
        self.notifier.notify(event="test", value=2)

        self.assertEqual(len(self.notifications), 1)
        self.assertEqual(self.notifications[0], (self.notifier, "test", {"value": 1}))


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestNotifier))
    return test_suite


if __name__ == "__main__":
    unittest.main(defaultTest="suite")
