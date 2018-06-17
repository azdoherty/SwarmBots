import unittest
import numpy as np

import Filters

def generate_line_2d_data(dist=500, noiseLvl=1):
    data = np.zeros((dist, 2))
    data[:, 0] = np.arange(dist) + noiseLvl*np.random.randn(dist)
    data[:, 1] = np.arange(dist) + noiseLvl*np.random.randn(dist)
    return data



class TestFilters(unittest.TestCase):

    def test_kalman_line_2d(self):
        testData = generate_line_2d_data()
        x1, y1, x2, y2 = testData[0, 0], testData[0, 1], testData[1, 0], testData[1, 1]
        KF = Filters.Kalman(x1, y1, x2, y2)