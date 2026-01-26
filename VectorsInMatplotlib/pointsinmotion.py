import matplotlib.pyplot as plt
import numpy as np

#drawing a group of points, but it's to depict motion

plt.rcParams["figure.figsize"] = (5, 5)
plt.rcParams["axes.grid"] = True

t = np.linspace(0, 2*np.pi, 200)

x = np.cos(t)
y = np.sin(t)

#plot connects the points, scatter just displays a point

plt.plot(x, y) #x2 + y2 = 1, finding (x, y) points to chart
plt.scatter(x[0], y[0], color='red', label="Start")
plt.gca().set_aspect('equal')
plt.title("Point moving in a circle")
plt.legend()
plt.show()