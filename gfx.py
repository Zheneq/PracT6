#!-*-coding:utf-8-*-
import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic
import pyqtgraph as pg
import numpy as np
from rk import *
import math


def f(t, y):
    return y


def f_(t, y):
    return y[0]


def f0(t, yv):
    return 2*yv[0] + math.exp(t) / math.cos(t) * (yv[1] + math.exp(t) * math.sin(t)**2)


def f1(t, yv):
    return yv[1] - 4. * math.cos(t) / math.exp(t) * yv[0]


def g0(t, yv):
    return yv[1] - 3*yv[0] + 9*t + 2


def g1(t, yv):
    return 6/7.*yv[0] - 2/7.*yv[1] + 4 * (t + 1)


( Ui_MainWindow, QMainWindow ) = uic.loadUiType('window.ui')


class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def __del__(self):
        self.ui = None

# -----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('Prac')

    # create widget
    w = MainWindow()
    w.setWindowTitle('Prac')
    w.show()

    # connection
    QObject.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))

    h = 1e-2
    numsteps = 1000
    graph2 = []
    # graph = solve([f_], [1.0], h)

    numsteps = 250
    graph1 = solve([f0, f1], [0., 1.], h, numsteps, 0.0)
    graph2 = [ [[h*i, math.exp(2*h*i) * math.sin(h*i)] for i in xrange(numsteps+1)],
               [[h*i, math.exp(h*i) * math.cos(2*h*i)] for i in xrange(numsteps+1)] ]

    # numsteps = 1000
    # graph = solve([g0, g1], [-1., 4.], h, numsteps, 0.0)
    # graph.append([[h*i, (h*i)**2 + 3*(h*i) - 1] for i in xrange(numsteps+1)])
    # graph.append([[h*i, 3*(h*i)**2 + 2*(h*i) + 4] for i in xrange(numsteps+1)])

    # x = [np.random.normal(loc=0., scale=2, size=100)]
    drawable = [np.array(graph1[i]) for i in xrange(len(graph1))]
    for i in xrange(len(drawable)):
        w.ui.graphicsView.plotItem.plot(drawable[i], pen=None, symbolBrush=(255,0,0), symbolPen='w')
    drawable = [np.array(graph2[i]) for i in xrange(len(graph2))]
    for i in xrange(len(drawable)):
        w.ui.graphicsView.plotItem.plot(drawable[i], pen=(i, len(drawable)))
    # x.ass = x.sa

    # execute application
    sys.exit(app.exec_())