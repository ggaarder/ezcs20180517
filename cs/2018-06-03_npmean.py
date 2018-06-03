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
