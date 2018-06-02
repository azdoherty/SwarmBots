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
        heading_adjust = (np.random.random() - .5) * self.noise_level
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
            self.heading = -self.heading
        if self.y < self.min_y:
            self.y = abs(self.y)
            self.heading = -self.heading

def move_trial(moves):
    positions = np.zeros((moves, 3))
    bug = VirtualBug()
    for i in range(moves):
        positions[i, 0], positions[i, 1] = bug.x, bug.y
        positions[i, 2] = i
        bug.move()
    return positions

def static_plot(moves):
    fig, ax = plt.subplots()
    ax.scatter(moves[:, 0], moves[:, 1], c=moves[:,1], alpha=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    ax.plot(moves[0, 0], moves[0, 1], 'r*')
    fig.tight_layout()
    plt.show()



if __name__ == "__main__":
    pos = move_trial(1000)
    static_plot(pos)