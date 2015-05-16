import math
from rk import *


def f(t, y):
    return y


def f_(t, y):
    return y[0]


def f0(t, yv):
    return (2*t*(1 - t**2) + yv[1] * (1 + t**2)) / (1 - t - t**2)


def f1(t, yv):
    return (2 * t * yv[1] + f0(t, yv)) / (1 - t**2)


h = 0.01
y = 1.0
#
# for i in xrange(0, 100):
#     x = i * h
#     y = rungekutta(x, y, f, h)
#     print y - math.exp(x + h)

y = [1.0]
for i in xrange(0, 100):
    x = i * h
    y = rungekuttavec(x, y, [f_], h)
    print y[0] - math.exp(x + h)

# fv = [f0, f1]
# yv = [0., 0.]
# for i in xrange(0, 90):
#     x = i * h
#     y = rungekuttavec(x, yv, fv, h)
#     print y[0] - (x**2 * (1 - x**2)) / (1 - x - x**2)
#     print y[1] - x**2 / (1 - x - x**2)

