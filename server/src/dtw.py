import numpy as np
from scipy.spatial.distance import euclidean


def dtw_distance(a, b):
    n, m = len(a), len(b)

    dtw = np.zeros((n + 1, m + 1))
    dtw[0, 1:] = np.inf

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = euclidean(a[i - 1], b[j - 1])
            dtw[i, j] = cost + min(dtw[i-1, j], dtw[i, j-1], dtw[i-1, j-1])

    return dtw[n, m]
