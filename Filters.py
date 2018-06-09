import numpy as np


class Kalman:
    def __init__(self, dims):
        pass


class Particle:
    def __init__(self, nParticles, xMax, yMax):
        self.nParticles = nParticles
        self.xMax = xMax
        self.yMax = yMax
        self.particlesX = np.random.random(self.nParticles) * self.xMax
        self.particlesY = np.random.random(self.nParticles) * self.yMax

    def update(self, mx, my):

if __name__ == "__main__":
    pass

