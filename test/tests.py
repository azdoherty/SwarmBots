import unittest
import numpy as np
from matplotlib import pyplot as plt
import Filters
import VirtualBug

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
        testData = generate_line_2d_data(500, 3)
        KF = Filters.Kalman(6, logger=True)
        predictions = np.zeros((testData.shape[0],2))
        for i in range(testData.shape[0]):
            KF.updatePredict(testData[i])
            predictions[i, :] = KF.X[0:2]
        print(predictions)
        fig = plt.figure()
        plt.title("Linear Tracking Test")
        plt.plot(testData[:, 0], testData[:, 1], 'b-', label="True")
        plt.plot(predictions[:, 0], predictions[:, 1], 'r--', label="Tracked")
        plt.legend()
        plt.savefig("test_positions_line.png", dpi=500)
        plt.close()

    def test_kalman_parabola_2d(self):
        testData = generate_parabola_2d_data(50, 3)
        x1, y1, x2, y2 = testData[0, 0], testData[0, 1], testData[1, 0], testData[1, 1]
        KF = Filters.Kalman(x1, y1, x2, y2, logger=True)
        predictions = np.zeros((testData.shape[0],2))
        for i in range(2, testData.shape[0]):
            print(testData[i], KF.X)
            KF.updatePredict(testData[i])
            predictions[i, :] = KF.X[0:2]
        print(predictions)
        fig = plt.figure()
        plt.title("Parabolic Tracking Test")
        plt.plot(testData[:, 0], testData[:, 1], 'b-', label="True")
        plt.plot(predictions[:, 0], predictions[:, 1], 'r--', label="Tracked")
        plt.legend()
        plt.savefig("test_positions_parabola.png", dpi=500)
        plt.close()

    def test_bug(self):
        nmoves = 200
        bugPositions = np.zeros((nmoves, 2))
        trackedPositins  = np.zeros((nmoves, 2))
        testBug = VirtualBug.VirtualBug()
        kf = None
        for i in range(nmoves):
            bugPositions[i, :] = np.array([testBug.x, testBug.y])
            if i == 2:
                kf = Filters.Kalman(bugPositions[0, 0], bugPositions[0, 1], bugPositions[1, 0], bugPositions[1, 1])

            if i > 2:
                trackedPositins[i, 0] = kf.X[0]
                trackedPositins[i, 1] = kf.X[1]
                kf.updatePredict(bugPositions[i, :])

            testBug.move()

        plt.figure()
        plt.title("Bug position tracking test")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.plot(bugPositions[:, 0], bugPositions[:, 1], 'b-', label="Bug")
        plt.plot(trackedPositins[:, 0], trackedPositins[:, 1], 'r--', label="Tracked")
        plt.legend()
        plt.savefig("test_bug_tracking.png", dpi=500)
        plt.close()





