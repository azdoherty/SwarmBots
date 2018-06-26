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
        self.measurement_noise = 2.
        self.H = np.array(np.identity(self.X.shape[0]))
        self.P = np.array(np.identity(self.X.shape[0]) * 100)
        self.R = np.array(np.identity(self.X.shape[0]) * self.measurement_noise)
        self.I = np.array(np.identity(self.X.shape[0]))
        self.logger = logger
        self.i=0
        if logger:
            logging.basicConfig(filename='example.log', level=logging.DEBUG, filemode='w')
            logging.info(time.time())
            logging.debug("H:\n{}".format(self.H))
            logging.debug("P:\n{}".format(self.P))
            logging.debug("R:\n{}".format(self.R))
            logging.debug("I:\n{}".format(self.I))
            logging.debug("\n\n\n\n")




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
        Y = Z - self.H @ self.X
        S = self.H @ self.P @ self.H.transpose() + self.R
        K = self.P @ self.H.transpose() @ np.linalg.pinv(S)
        self.i+=1
        if self.logger:
            logging.debug("start {}".format(self.i))
            logging.debug("K:\n{}".format(K))
            logging.debug("S:\n{}".format(S))
            logging.debug("S inverse:\n{}".format(np.linalg.pinv(S)))
            logging.debug("speed: {},{}".format(xdotMeasured, ydotMeasured))
            logging.debug("Y:\n{}".format(Y))
            logging.debug("X:\n{}".format(self.X))
            logging.debug("K dot Y:\n{}".format(K @ Y))
        self.X = self.X + np.dot(K, Y)
        if self.logger:
            logging.debug("update {}".format(self.i))
            logging.debug("P:\n{}".format(self.P))
            logging.debug("X:\n{}".format(self.X))
            logging.debug("K dot H:\n{}".format(K @self.H))
            logging.debug("K:\n{}".format(K))

        self.P = (self.I - K @ self.H) @ self.P


        # create new prediction for next measurement
        # state transition funciton = [x + xdot, y + ydot, xdot, ydot]
        self.X = np.array([self.X[0] + self.X[2], self.X[1] + self.X[3], self.X[2], self.X[3]])
        # compute jacobian
        jacobian = np.array([[1.0, 0.0, 1.0, 0.0],
                             [0.0, 1.0,  0.0, 1.0],
                             [0.0, 0.0, 1.0, 0.0],
                             [0.0, 0.0, 0.0, 1.0]])

        self.P = np.dot(jacobian, np.dot(self.P, jacobian.transpose()))
        if self.logger:
            logging.debug("end {}".format(self.i))
            logging.debug("P:\n{}".format(self.P))
            logging.debug("P dot jac:\n{}".format(self.P @ jacobian.transpose()))
            logging.debug("X:\n{}".format(self.X))
            logging.debug("\n\n\n\n")
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

