import turtle
import numpy as np
from matplotlib import pyplot as plt

class VirtualBug:
    def __init__(self, noise_level=.1):
        """
        A class to model
        :param noise_level:
        """
        self.noise_level = noise_level
        self.min_x = 0
        self.max_x = 1000
        self.min_y = 0
        self.max_y = 500
        self.x = np.random.randint(self.min_x, self.max_x)
        self.y = np.random.randint(self.min_y, self.max_y)
        self.heading = np.random.random() * 2 * np.pi
        self.velocity = np.random.random() * 5


    def move(self):
        heading_adjust = (np.random.random() - 1) * self.noise_level
        self.heading += heading_adjust
        self.x += self.velocity * np.cos(self.heading)
        self.y += self.velocity * np.sin(self.heading)
        if self.x > self.max_x:
            self.x = 2 * self.max_x - self.x
            self.heading = np.pi - self.heading
        if self.x < self.min_x:
            self.x = abs(self.x)
            self.heading = np.pi - self.heading
        if self.y > self.max_y:
            self.y = 2 * self.max_y - self.y
            self.heading = 3*np.pi/2 - self.heading
        if self.y < self.min_y:
            self.y = abs(self.y)
            self.heading = np.abs(np.pi/2 - self.heading)

def move_trial(moves):
    positions = np.zeros((moves, 2))
    bug = VirtualBug()
    for i in range(moves):
        positions[i, 0], positions[i, 1] = bug.x, bug.y
        bug.move()
    print(positions)

def static_plot(moves):
    pass



if __name__ == "__main__":
    move_trial(100)