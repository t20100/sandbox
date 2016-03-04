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
"""Test for plot module."""

__authors__ = ["T. Vincent"]
__copyright__ = "ESRF"
__license__ = "MIT"
__date__ = "08/02/2016"


import unittest

from .. import backend, items, plot


class TestPlot(unittest.TestCase):
    def testPlot(self):
        class DummyPlot(plot.Plot):
            def __init__(self, title=''):
                super(DummyPlot, self).__init__(title=title)
                self._backend = backend.Backend(self)

        test = DummyPlot()
        print('### Create curve ###')
        curve = items.Curve(y=(1, 2, 2))
        print('### addItem ###')
        test.axes.left.addItem(curve)
        print('### change curve visible = False ###')
        curve.visible = False
        print('### change curve linewidth ###')
        curve.linewidth = 2
        print('### change plot title ###')
        test.title = 'test plot'


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestPlot))
    return test_suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
