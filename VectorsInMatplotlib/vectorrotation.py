import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = (5, 5)
plt.rcParams["axes.grid"] = True

angle = 180 #change angle here
theta = np.deg2rad(angle)

R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

v = np.array([3, 1])
v_rot = R @ v

plt.axhline(0, color = 'gray')
plt.axvline(0, color = 'gray')

plt.quiver(0, 0, v[0], v[1], angles = 'xy', scale=1, scale_units='xy', color='blue', label="Original") #original vector
plt.quiver(0, 0, v_rot[0], v_rot[1], angles = 'xy', scale=1, scale_units='xy', color='red', label="Rotated") #rotated vector

plt.legend()
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.gca().set_aspect('equal')
plt.title("Vector Rotation")
plt.show()