import numpy as np


class Kalman:
    """
    Extended kalman filter for non linear 2-d motion
    """
    def __init__(self, x1, y1, x2, y2):
        self.xdot = x2 - x1
        self.ydot = y2 - y1
        self.prev_X = np.matrix([[x1, y1, self.xdot, self.ydot]])
        self.X = np.matrix([[x2, y2, self.xdot, self.ydot]])
        self.measurement_noise = 1.0
        self.H = np.matrix([[1.0, 0.0, 0.0, 0.0],
                                    [0.0, 1.0, 0.0, 0.0],
                                    [0.0, 0.0, 1.0, 0.0],
                                    [0.0, 0.0, 0.0, 1.0]])

        self.P = np.matrix([[100.0, 0.0, 0.0, 0.0],
                            [0.0, 100.0, 0.0, 0.0],
                            [0.0, 0.0, 100.0, 0.0],
                            [0.0, 0.0, 0.0, 100.0]])
        self.R = np.matrix([[self.measurement_noise, 0.0, 0.0, 0.0],
                    [0.0, self.measurement_noise, 0.0, 0.0],
                    [0.0, 0.0, self.measurement_noise, 0.0],
                    [0.0, 0.0, 0.0, self.measurement_noise]])

        self.I = np.matrix([[1.0, 0.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0]])

    def update(self, measurement):
        self.prev_X = self.X
        xdotMeasured = measurement[0] - self.X[0]
        ydotMeasured = measurement[1] - self.X[1]
        Z = np.matrix([[measurement[0], measurement[1], xdotMeasured, ydotMeasured]])
        Y = Z - self.H * self.X
        S = self.H * self.P * self.H.transpose()
        K = self.P * self.H.transpose()


        pass

    def predict(self, movement):
        # state transition
        # F*X + u -- transition times state + motion
        #
        pass


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

