import copy
import csv
import random
import itertools
import operator
import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt

def load_irisdata(col1, col2, filename='iris-dataset.csv'):
    COLS = list(range(0, 4))
    if not col1 in COLS or not col2 in COLS:
        raise IndexError('Iris data column should be in [0, 4)')

    dat = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dat.append([float(row[col1]), float(row[col2])])
    return dat

def getd(points, dimension):
    return [p[dimension] for p in points]

COLOURS, MARKERS = 'kbgrcmy', 'ov^<>1234sp*hH+xDd|_'
FMTS = [operator.add(*i) # concat string
        for i in itertools.product(COLOURS, MARKERS)]
random.shuffle(FMTS)

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
        x, y = getd(points, 0), getd(points, 1)
        plotargs += [x, y, fmt]
        
    plt.plot(*plotargs)
    plt.show()

def kmeans_iter(points, means,
                dist = lambda a, b: (a[0]-b[0])**2+(a[1]-b[1])**2):
    k_cnt = len(means)
    groups = [[] for i in range(0, k_cnt)]
    
    for point in points:
        dists = [dist(means[i], point) for i in range(0, k_cnt)]
        mindist = min(dists)
        argmin = dists.index(mindist)
        groups[argmin].append(point)

    return groups

def calc_means(groups):
    return [list(np.mean(group, axis=0)) for group in groups]

def means_equal(m1, m2, delta=0.00001):
    for (p1, p2) in zip(m1, m2):
        if abs(p1[0]-p2[0]) > delta or abs(p1[1]-p2[1]) > delta:
            return False
    return True

if __name__ == '__main__':
    K_CNT = 3
    testdats = []
    
    for col1 in range(0, 4):
        for col2 in range(col1+1, 4):
            dat = load_irisdata(col1, col2)
            testdats.append(dat)

    for i, ti in enumerate(testdats):
        print('test data #{}'.format(i))
        plot([ti])
        xmax, xmin = max(getd(ti, 0)), min(getd(ti, 0))
        ymax, ymin = max(getd(ti, 1)), min(getd(ti, 1))
        means = [[random.uniform(xmin, xmax),
                  random.uniform(ymin, ymax)]
                 for i in range(0, K_CNT)]
        itercnt = 0

        while True:
            groups = kmeans_iter(ti, means)
            itercnt = itercnt+1
            print('iter #{}'.format(itercnt))
            newmeans = calc_means(groups)

            if means_equal(means, newmeans):
                break

            means = newmeans
            print('new means: {}'.format(newmeans))
            plot(groups + [[i] for i in newmeans])
