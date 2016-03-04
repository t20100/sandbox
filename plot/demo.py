#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import logging
import sys
import numpy

from PyQt4 import QtGui

logging.basicConfig()
logger = logging.getLogger(__name__)

app = QtGui.QApplication([])


def test_widget():
    """Code with PlotWidget API"""
    from plot.PlotWidget import PlotWidget

    plt = PlotWidget()
    plt.addCurve(x=None, y=(1, 2, 2))
    plt.addImage(data=numpy.arange(100).reshape(10, -1),
                 xScale=(0, 1), yScale=(10, 1))
    plt.setGraphTitle('Procedural Plot API')
    plt.setGraphXLabel('x label')
    plt.setGraphYLabel('y label')
    plt.setGraphXLimits(0, 10)
    plt.setGraphYLimits(0, 20)
    plt.invertYAxis(True)
    plt.show()
    return plt


def test_plot():
    """Code with OO API"""
    from plot import BackendMPL, Plot

    class MyPlotWidget(Plot):
        """Glue class, should be provided by plot"""
        def __init__(self, title=''):
            super(MyPlotWidget, self).__init__(title=title)
            self.backend = BackendMPL(self)

        def show(self):
            self.backend.show()

    #####################

    plt = MyPlotWidget()
    plt.addImage(data=numpy.arange(100).reshape(10, -1), origin=(0, 10))
    curve = plt.addCurve(y=(1, 2, 2))
    plt.title = 'OO Plot API'
    plt.xlabel = 'x left'
    plt.ylabel = 'y left'
    plt.xlimits = 0, 10
    plt.ylimits = 20, 0
    plt.show()

    # Update
    curve.linewidth = 2
    plt.grid = 'both'
    plt.axes.right.ylabel = 'y right'
    return plt


plot = test_widget()
plotOO = test_plot()

sys.exit(app.exec_())
