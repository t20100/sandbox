# coding: utf-8
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
# ############################################################################*/
"""Benchmark of different polygon fill implementations
"""


__authors__ = ["T. Vincent"]
__license__ = "MIT"
__date__ = "03/06/2016"


from itertools import combinations
import logging
import time

import numpy

import matplotlib.pyplot as plt


logging.basicConfig()
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)


FILL_FUNCTIONS = {}
"""Polygon filling function to benchmark"""


# silx
try:
    from silx.image.shapes import polygon_fill_mask as silx_polygon_fill
except ImportError:
    _logger.warning(
        'silx polygon fill not found, not included in benchmark')
else:
    FILL_FUNCTIONS['silx'] = silx_polygon_fill


# skimage
try:
    from skimage.draw import polygon as sk_polygon
except ImportError:
    _logger.warning(
        'scikit-image polygon fill not found, not included in benchmark')
else:
    def skimage_polygon_fill(vertices, mask_shape):
        """Polygon filling using sci-kit image"""
        vertices = numpy.asarray(vertices)
        mask = numpy.zeros(mask_shape, dtype=numpy.bool_)
        y, x = sk_polygon(vertices[:, 0], vertices[:, 1], mask_shape)
        if len(y):
            mask[y, x] = True
        return mask

    FILL_FUNCTIONS['skimage'] = skimage_polygon_fill


# PyMca5
try:
    from PyMca5.PyMcaGraph.ctools import pnpoly as pymca_polygon
except ImportError:
    _logger.warning('PyMca5 polygon fill not found, not included in benchmark')
else:
    def pymca_polygon_fill(vertices, mask_shape):
        """Polygon filling using PyMca"""
        points = numpy.zeros((mask_shape[0] * mask_shape[1], 2))
        x, y = numpy.meshgrid(numpy.arange(mask_shape[1]),
                              numpy.arange(mask_shape[0]))
        x.shape = -1
        y.shape = -1
        points[:, 0] = x
        points[:, 1] = y
        return pymca_polygon(vertices, points).reshape(mask_shape)

    FILL_FUNCTIONS['pymca5'] = pymca_polygon_fill


def main(argv=None):
    """Run the benchmarks of polygon filling"""

    # Test by crossing different number of corners and different shapes
    test_params = [(nbvert, size, polygon_subpart)
                   for nbvert in (10, 50, 100)
                   for polygon_subpart in (1, 2, 4)
                   for size in (32, 64, 128, 256, 512, 1024, 2048, 4096)]

    # Store vertices and size of each test
    tests = []
    # Store time for each test for each implementation
    timings = dict((key, []) for key in FILL_FUNCTIONS)

    for nbvertices, size, polygon_subpart in test_params:
        _logger.info('Test with %d vertices and mask size %d, subpart %d',
                     nbvertices, size, polygon_subpart)
        vertices = numpy.random.randint(
            0, size // polygon_subpart, 2 * nbvertices)
        vertices = vertices.astype(numpy.float32).reshape(-1, 2)

        tests.append((vertices, size))
        results = {}

        for name, polygon_fill in FILL_FUNCTIONS.items():
            t0 = time.time()
            mask = polygon_fill(vertices, (size, size))
            t1 = time.time()
            _logger.info('%s took %.3fs', name, t1 - t0)
            timings[name].append(t1 - t0)
            results[name] = mask

        # Compare results
        # for name_a, name_b in combinations(FILL_FUNCTIONS, 2):
        #     differences = numpy.count_nonzero(
        #         numpy.not_equal(results[name_a], results[name_b]))
        #     _logger.info('%s vs %s differences: %d',
        #                  name_a, name_b, differences)

    _logger.info('Results for: ' + ', '.join(name for name in timings))
    for index in range(len(tests)):
        _logger.info(
            'nbvert:%d size:%d: ' % (len(tests[index][0]), tests[index][1]) +
            ', '.join('%.3fs' % times[index] for times in timings.values()))
    _logger.info('Overall: Min, Mean, Median, Max')
    for name, times in timings.items():
        _logger.info('%s: %f, %f, %f, %f', name,
                     min(times),
                     numpy.mean(times),
                     numpy.median(times),
                     max(times))

    for name, times in timings.items():
        plt.plot(times, label=name)
    plt.legend()
    plt.title(
        """3 Conditions:
        - mask size (fastest variation): [32**2 - 4k**2],
        - mask size / polygon size: (1, 2, 4),
        - nb vertices (slowest variation): (10, 50, 100)""")
    plt.xlabel('test cases: mask size x polygon ratio x nb vertices')
    plt.ylabel('time (seconds)')
    plt.yscale('log')
    plt.show()


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
