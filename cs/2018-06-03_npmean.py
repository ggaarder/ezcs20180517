import numpy as np
import numpy.matlib

if __name__ == '__main__':
    points = np.matlib.rand(20, 2)
    mean0 = np.mean(points, axis=0)
    mean1 = np.mean(points, axis=1)
    print(mean0, mean1)

    points = np.matlib.rand(40, 2)
    mean0 = np.mean(points, axis=0)
    mean1 = np.mean(points, axis=1)
    print(mean0, mean1)

    points = np.matlib.rand(40, 3)
    mean0 = np.mean(points, axis=0)
    mean1 = np.mean(points, axis=1)
    mean2 = np.mean(points, axis=2)
    print(mean0, mean1, mean2)

    points = np.matlib.rand(40, 4)
    mean0 = np.mean(points, axis=0)
    mean1 = np.mean(points, axis=1)
    mean2 = np.mean(points, axis=2)
    mean3 = np.mean(points, axis=3)
    print(mean0, mean1, mean2, mean3)
