import operator
import itertools
import numpy as np
import numpy.matlib
import matplotlib.pyplot as plot

COLOURS, MARKERS = 'kbgrcmy', 'ov^<>1234sp*hH+xDd|_'
FMTS = sorted([operator.add(*i)
               for i in itertools.product(COLOURS, MARKERS)],
              # sorted to let formats of same colours but different markers
              # come firstly, instead same markers but different colours
              # i.e. 'k.' 'k,' 'ko' ... instead of 'k.' 'b.' 'g.' ...
              key = lambda c: abs(ord(c[0])-ord('k'))
              # 'k' (black) comes first
)

def plot(dats):
    """dats = [[[x1, y1], [x2, y2], ...],  (group1)
               [[x1, y1], [x2, y2], ...],  (group2)
               [[x1, y1], [x2, y2], ...],  (group3)
               ...]
    """
    fmts = FMTS
    if len(dats) > len(fmts):
        fmts *= 2
        while len(dat) > len(fmts):
            fmts += FMTS

    plotargs = []
    for points, fmt in zip(dats, fmts):
        x, y = [p[0] for p in points], [p[1] for p in points]
        plotargs += [x, y, fmt]
        
    plt.plot(*plotargs)
    plt.show()

if __name__ == '__main__':
    while True:
        points = np.matlib.rand(20, 2)
        mean0 = np.mean(points, axis=0)
        mean1 = np.mean(points, axis=1)
        print(mean0, mean1)
