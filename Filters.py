import numpy as np
import logging
import time

class Kalman:
    def __init__(self, dim, logger=False):
        """
        :param dims: integer, number of dimensions in the filter, always d1 d1/dt d^21/dt^2, d2, d2/dt etcetera
        :param logger: log a bunch of things if true
        """

        self.measurement_noise = 5.
        self.dim = dim
        self.H = np.array(np.identity(dim))
        self.P = np.array(np.identity(dim) * 100)
        self.R = np.array(np.identity(dim) * self.measurement_noise)
        self.I = np.array(np.identity(dim))
        self.logger = logger
        self.i = 0
        self.X = None
        self.measurements = []
        if logger:
            logging.basicConfig(filename='example.log', level=logging.DEBUG, filemode='w')
            logging.info(time.time())
            logging.debug("H:\n{}".format(self.H))
            logging.debug("P:\n{}".format(self.P))
            logging.debug("R:\n{}".format(self.R))
            logging.debug("I:\n{}".format(self.I))
            logging.debug("\n\n\n\n")

    def measure_non_observable(self, measurement):
        if self.d


    def updatePredict(self, measurement):
        """
        :param measurement: x, y coordinate as 2 element numpy array or x,y,z numpy array
        :return:
        """
        # use the new measurement to correct current prediction
        if len(self.measurements) < 2 or ( len(self.measurements) < 3 and self.dim==6):
            self.measurements.append(measurement)
            self.X = np.empty(measurement.shape[0])
            return self.X
        elif len(self.measurements) == 2 and self.dim==4:
            velocity = self.measurements[1] - self.measurements[0]
            self.X = np.array([measurement[0], velocity[0], measurement[1], velocity[1]])

        elif len(self.measurements) == 3 and self.dim==6:
            velocity1 = self.measurements[1] - self.measurements[0]
            velocity2 = self.measurements[2] - self.measurements[1]
            acceleration = velocity2 - velocity1
            self.X = np.array([measurement[0], velocity2[0], acceleration[0], measurement[1], velocity2[1],
                               acceleration[1]])

        self.prev_X = self.X
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

