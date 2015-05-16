a =\
[
    [],
    [1/2.],
    [0,     1/2.],
    [0,     0,      1.]
]
b = [1/6., 1/3., 1/3., 1/6.]
c = [0, 1/2., 1/2., 1]
steps = len(b)


def rungekutta(t, y, f, h):
    k = []
    for i in xrange(steps):
        k.append(h * f(t + c[i]*h, y + reduce(lambda x, y: x+y, map(lambda x, y: x*y, a[i], k), 0)))
    return y + reduce(lambda x, y: x+y, map(lambda x, y: x*y, b, k))