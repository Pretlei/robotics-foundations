import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

l1, l2 = 1.0, 0.7

def fk(theta1, theta2):
    x1 = l1 * np.cos(theta1)
    y1 = l1 * np.sin(theta1)
    x2 = x1 + l2 * np.cos(theta1 + theta2)
    y2 = y1 + l2 * np.sin(theta1 + theta2)
    return [0, x1, x2], [0, y1, y2]

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.grid()

line, = ax.plot([], [], 'o-', lw = 4)
#line, assigns the first object that ax.plot returs to line (since ax.plot returns a list)
#empty brackets for data to be filled later
#'o-' to signify that the (x, y) given are circles drawn and the solid line is what is drawn between them
#lw = 4 is line width

#is the function that updates the picture over the given number of framees
def update(frame):
    theta1 = 0.5 * np.sin(frame * 0.05) #oscillates, increases then decreases then...
    theta2 = 0.8 * np.cos(frame * 0.05) #oscillates, decreases then increases then...
    x, y = fk(theta1, theta2)
    line.set_data(x, y) #moves the line to the new spot
    return line, #called blitting, only returns the dynamic parts of the arm

ani = FuncAnimation(fig, update, frames=300, interval=30)
#fig -> which subplot it needs to draw in
#update -> the function that is called again and again to make changes
#frames -> sets the number of iterations update will run
#interval -> delay between frames in ms
plt.show()