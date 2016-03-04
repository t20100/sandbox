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
"""Test for items module."""

__authors__ = ["T. Vincent"]
__copyright__ = "ESRF"
__license__ = "MIT"
__date__ = "05/02/2016"


import unittest

import numpy

from .. import items


class TestPlotItems(unittest.TestCase):
    """Stupid test to check the existence of classes"""

    def testPlotItems(self):
        """Check existence of class"""
        item = items.PlotItem()  # noqa

    def testColormap(self):
        """Check existence of class"""
        colormap = items.Colormap()  # noqa

    def testImage(self):
        """Check existence of class"""
        data = numpy.arange(100.).reshape(10, -1)
        image = items.Image(data)  # noqa

    def testCurve(self):
        """Check existence of class"""
        curve = items.Curve()  # noqa

    def testShape(self):
        """Check existence of class"""
        shape = items.Shape()  # noqa


class TestPlotItemNotifyProperty(unittest.TestCase):
    """Test _notifiyProperty method"""

    def setUp(self):
        self.notifications = []  # List of received notifications

    def tearDown(self):
        del self.notifications

    def listener(self, source, event, **kwargs):
        """Listener method used for tests"""
        self.notifications.append((source, event, kwargs))

    def testNotifyProperty(self):
        """Property without type casting with notification.

        Init property, register listener, set the same value,
        set a different value, unregister listener.
        """
        class TestItem(items.PlotItem):
            tester = items.notifyProperty('_tester', doc="""Test""")

        testItem = TestItem()
        self.assertEqual(TestItem.tester.__doc__, 'Test')

        testItem.tester = 1
        self.assertEqual(testItem.tester, 1)

        testItem.addListener(self.listener)
        testItem.tester = 1  # No modification = no notification
        testItem.tester = 2  # Notification
        testItem.removeListener(self.listener)

        self.assertEqual(len(self.notifications), 2)
        self.assertEqual(self.notifications[0],
                         (testItem, 'set', {'attr': 'tester', 'value': 2}))
        self.assertEqual(self.notifications[1],
                         (testItem, 'needRedisplay', {}))

    def testNotifyPropertyWithType(self):
        """Property with type casting with notification.

        Init property, register listener, set the same value,
        set a different value, unregister listener.
        """
        class TestItem(items.PlotItem):
            tester = items.notifyProperty(
                '_tester', str, doc="""Test""")

        testItem = TestItem()
        testItem.tester = 1
        self.assertEqual(testItem.tester, '1')

        testItem.addListener(self.listener)
        testItem.tester = 1  # No modification = no notification
        testItem.tester = 2  # Notification
        testItem.removeListener(self.listener)

        self.assertEqual(len(self.notifications), 2)
        self.assertEqual(self.notifications[0],
                         (testItem, 'set', {'attr': 'tester', 'value': '2'}))
        self.assertEqual(self.notifications[1],
                         (testItem, 'needRedisplay', {}))


def suite():
    testSuite = unittest.TestSuite()
    for testClass in (TestPlotItems, TestPlotItemNotifyProperty):
        testSuite.addTest(
            unittest.defaultTestLoader.loadTestsFromTestCase(testClass))
    return testSuite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
