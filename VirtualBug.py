import turtle
import numpy as np

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
        if self.x < self.min_x:
            self.x = abs(self.x)
        if self.y > self.max_y
            self.y = 2*self.max_y - self.y
        if self.y < self.min_y:
            self.y = abs(self.y)

            


if __name__ == "__main__":
    bug = VirtualBug()
    print(bug.heading)