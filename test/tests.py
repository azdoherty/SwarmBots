import unittest
import numpy as np
from matplotlib import pyplot as plt
import Filters

def generate_line_2d_data(dist=500, noiseLvl=1.):
    data = np.zeros((dist, 2))
    data[:, 0] = np.arange(dist) + noiseLvl*np.random.randn(dist)
    data[:, 1] = np.arange(dist) + noiseLvl*np.random.randn(dist)
    return data

def generate_parabola_2d_data(dist=500, noiseLvl=1.):
    data = np.zeros((dist, 2))
    data[:, 0] = np.arange(dist) + noiseLvl*np.random.randn(dist) - dist/2
    data[:, 1] = data[:, 0]**2
    return data


class TestFilters(unittest.TestCase):

    def test_kalman_line_2d(self):
        testData = generate_line_2d_data(10, .5)
        x1, y1, x2, y2 = testData[0, 0], testData[0, 1], testData[1, 0], testData[1, 1]
        KF = Filters.Kalman(x1, y1, x2, y2, logger=True)
        predictions = np.zeros((testData.shape[0],2))
        for i in range(2, testData.shape[0]):
            print(testData[i], KF.X)
            KF.updatePredict(testData[i])
            predictions[i, :] = KF.X[0:2]
        print(predictions)
        fig = plt.figure()
        plt.plot(testData[:, 0], testData[:, 1], 'b-')
        plt.plot(predictions[:, 0], predictions[:, 1], 'r--')
        plt.savefig("test_positions_line.png")

