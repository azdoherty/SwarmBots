import numpy as np
import logging
import time

class Kalman:
    """
    Extended kalman filter for non linear 2-d motion
    """
    def __init__(self, x1, y1, x2, y2, logger=False):
        self.xdot = x2 - x1
        self.ydot = y2 - y1
        self.prev_X = np.array([x1, y1, self.xdot, self.ydot])
        self.X = np.array([x2, y2, self.xdot, self.ydot])
        self.measurement_noise = 1.0
        self.H = np.identity(self.X.shape[0])
        self.P = np.identity(self.X.shape[0]) * 100
        self.R = np.identity(self.X.shape[0]) * self.measurement_noise
        self.I = np.identity(self.X.shape[0])
        self.logger = logger
        if logger:
            logging.basicConfig(filename='example.log', level=logging.DEBUG)
            logging.info(time.time())
            logging.debug("\n{}".format(self.X))
            logging.debug("\n{}".format(self.prev_X))
            logging.debug("\n{}".format(self.H))
            logging.debug("\n{}".format(self.P))
            logging.debug("\n{}".format(self.R))
            logging.debug("\n{}".format(self.I))



    def updatePredict(self, measurement):
        """
        :param measurement: x, y coordinate as 2 element numpy array
        :return:
        """
        # use the new measurement to correct current prediction
        self.prev_X = self.X
        xdotMeasured = measurement[0] - self.X[0]
        ydotMeasured = measurement[1] - self.X[1]
        Z = np.array([measurement[0], measurement[1], xdotMeasured, ydotMeasured])
        Y = Z - np.dot(self.H, self.X)
        S = np.dot(self.H, np.dot(self.P,self.H.transpose()))
        K = np.dot(self.P, np.dot(self.H.transpose(), np.linalg.pinv(S)))
        self.X = self.X + np.dot(K, Y)
        if self.logger:
            logging.debug(self.P)
        self.P = np.dot((self.I - np.dot(K, self.H)), self.P)

        # create new prediction for next measurement
        self.X = np.array([self.X[0] + self.X[2], self.X[1] + self.X[3], self.X[2], self.X[3]])
        # compute jacobian
        jacobian = np.matrix([[1.0, 0.0, 0.0, 0.0],
                             [0.0, 1.0,  0.0, 0.0],
                             [0.0, 0.0, 1.0, 0.0],
                             [0.0, 0.0, 0.0, 1.0]])
        if self.logger:
            logging.debug(self.P)
        self.P = jacobian * self.P * jacobian.transpose()


class Particle:
    def __init__(self, nParticles, xMax, yMax):
        self.nParticles = nParticles
        self.xMax = xMax
        self.yMax = yMax
        self.particlesX = np.random.random(self.nParticles) * self.xMax
        self.particlesY = np.random.random(self.nParticles) * self.yMax

    def update(self, mx, my):
        pass
    

if __name__ == "__main__":
    pass

