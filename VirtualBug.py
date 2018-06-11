import turtle
import numpy as np
from matplotlib import pyplot as plt


class VirtualBug:
    def __init__(self, noise_level=.5):
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
        self.last_moved = 0  # distance moved last

    def move(self):
        """
        advance the bug 1 move, randomly perturb velocity based on noise level prior to doing so.
        :return: Nothing
        """
        heading_adjust = (np.random.random() - .5) * self.noise_level
        self.heading += heading_adjust
        old_x, old_y = self.x, self.y
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

        self.last_moved = np.sqrt((old_x - self.x)**2 + (old_y - self.y)**2)


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
    ax.scatter(moves[:, 0], moves[:, 1], c=moves[:, 2], alpha=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    ax.plot(moves[0, 0], moves[0, 1], 'r*')
    fig.tight_layout()
    plt.show()


def dynamic_tracking(bug, moves):
    canvas = turtle.Screen()
    pad = 100
    canvas.setup(bug.max_x + pad, bug.max_y + pad)
    # coordinate system needs to be transformed by half of the bounds of the box
    # draw box
    t = turtle.Turtle()
    t.penup()
    t.speed("fastest")
    t.setx(-bug.max_x*1./2)
    t.sety(-bug.max_y*1./2)
    t.pendown()
    t.forward(bug.max_x)
    t.left(90)
    t.forward(bug.max_y)
    t.left(90)
    t.forward(bug.max_x)
    t.left(90)
    t.forward(bug.max_y)
    t.penup()
    t.speed("fast")
    t.color("red", "red")
    # simulate moves
    t.setheading(bug.heading*360./(2*np.pi))
    t.setx(bug.x - bug.max_x * 1. / 2)
    t.sety(bug.y - bug.max_y * 1. / 2)
    t.pendown()
    for i in range(moves):
        bug.move()
        t.setheading(bug.heading * 360. / (2 * np.pi))
        t.forward(bug.last_moved)

    canvas.exitonclick()


if __name__ == "__main__":
    pos = move_trial(10000)
    static_plot(pos)
    b = VirtualBug()
    dynamic_tracking(b, 10000)
