import unittest

from .test_event import suite as test_event_suite
from .test_items import suite as test_items_suite
from .test_plot import suite as test_plot_suite
from .test_utils import suite as test_utils_suite


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(test_event_suite())
    test_suite.addTest(test_items_suite())
    test_suite.addTest(test_plot_suite())
    test_suite.addTest(test_utils_suite())
    return test_suite
