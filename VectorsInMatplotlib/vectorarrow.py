import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (5, 5)
plt.rcParams["axes.grid"] = True

v = np.array([3, 2])  # x, y

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')

plt.quiver(
    0, 0,           # start point
    v[0], v[1],     # vector components
    angles='xy',
    scale_units='xy',
    scale=1,
    color='blue'
)

plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.gca().set_aspect('equal')
plt.title("A vector as an arrow")
plt.show()