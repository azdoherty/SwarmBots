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
        self.velocity = np.random.random() * 10
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
            self.heading = 2*np.pi - self.heading
        if self.y < self.min_y:
            self.y = abs(self.y)
            self.heading = 2*np.pi - self.heading

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


class BugZone:
    def __init__(self, nBugs, visualize=False, *args):
        """
        :param nBugs:
        :param xshape:
        :param yshape:
        :param visualize:
        :param args:
        """
        self.nBugs = nBugs

        self.visualize = visualize
        self.canvas = None
        self.bugs = []
        for i in range(self.nBugs):

            self.bugs.append(VirtualBug())
            #self.bugs[-1].max_x = self.xshape
            #self.bugs[-1].max_y = self.yshape
        self.xshape = self.bugs[-1].max_x
        self.yshape = self.bugs[-1].max_y
        if self.visualize:
            self.pad = 100
            self.turtles = []
            self.setup_canvas()
            turtle.tracer(0, 0)
            for b in self.bugs:
                self.turtles.append(turtle.Turtle())
                #self.turtles[-1].tracer(False)
                self.turtles[-1].penup()
                self.turtles[-1].setheading(b.heading * 360. / (2 * np.pi))
                self.turtles[-1].setx(b.x - b.max_x * 1. / 2)
                self.turtles[-1].sety(b.y - b.max_y * 1. / 2)
                r, g, b = np.random.randint(1, 255), np.random.randint(1, 255), np.random.randint(1, 255)
                self.canvas.colormode(255)
                self.turtles[-1].color(r, g, b)

                self.turtles[-1].pendown()
            turtle.update()


    def setup_canvas(self):
        self.canvas = turtle.Screen()
        self.canvas.setup(self.xshape + self.pad, self.yshape + self.pad)
        # coordinate system needs to be transformed by half of the bounds of the box
        # draw box
        t = turtle.Turtle()
        t.penup()
        t.speed("fastest")
        t.setx(-self.xshape * 1. / 2)
        t.sety(-self.yshape * 1. / 2)
        t.pendown()
        t.forward(self.xshape)
        t.left(90)
        t.forward(self.yshape)
        t.left(90)
        t.forward(self.xshape)
        t.left(90)
        t.forward(self.yshape)
        t.penup()

    def simulate_movement(self, nmoves):

        for i in range(nmoves):
            #self.canvas.ontimer(self.move1())
            self.move1()
            turtle.update()

        self.canvas.exitonclick()

    def move1(self):
        for k in range(len(self.bugs)):
            self.bugs[k].move()
            self.turtles[k].setheading((self.bugs[k].heading * 360. / (2 * np.pi)) % 360)
            self.turtles[k].forward(self.bugs[k].last_moved)
            x, y = self.bugs[k].x, self.bugs[k].y
            tx, ty = self.turtles[k].xcor(), self.turtles[k].ycor()

if __name__ == "__main__":
    '''
    pos = move_trial(10000)
    static_plot(pos)
    b = VirtualBug()
    dynamic_tracking(b, 10000)
    '''
    b = BugZone(10, True)
    b.simulate_movement(5000)


