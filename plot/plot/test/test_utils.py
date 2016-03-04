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
"""Test for utils module."""

__authors__ = ["T. Vincent"]
__copyright__ = "ESRF"
__license__ = "MIT"
__date__ = "08/02/2016"


import unittest

from .. import utils


class TestProxyProperty(unittest.TestCase):
    """Test for proxyProperty function"""

    def testProxyProperty(self):
        """Test proxyProperty over attribute and property"""

        class Leaf(object):
            """The class that is wrapped"""
            def __init__(self):
                self._prop = 'value prop'
                self.instanceAttribute = 'value attribute'

            @property
            def prop(self):
                return self._prop

            @prop.setter
            def prop(self, value):
                self._prop = value

        class Composite(object):
            """The wrapping class"""
            def __init__(self):
                self.leaf = Leaf()

            testAttribute = utils.proxyProperty('leaf', 'instanceAttribute')
            testPropertyRO = utils.proxyProperty('leaf', 'prop', setter=False)
            testProperty = utils.proxyProperty('leaf', 'prop', setter=True)

        test = Composite()

        # Wrapped attribute
        self.assertEqual(test.testAttribute, 'value attribute')

        # Property wrapped as read-only
        self.assertEqual(test.testPropertyRO, 'value prop')
        with self.assertRaises(AttributeError):
            test.testPropertyRO = None

        # Wrapped property
        self.assertEqual(test.testProperty, 'value prop')
        test.testProperty = 'new value'
        self.assertEqual(test.testProperty, 'new value')


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestProxyProperty))
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
