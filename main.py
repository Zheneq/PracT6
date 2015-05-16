import math
from rk import *

def f(t, y):
    return y

h = 0.01
y = 1.0
for i in xrange(0, 100):
    x = i * h
    y = rungekutta(x, y, f, h)
    print y - math.exp(x + h)