import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = (5, 5)
plt.rcParams["axes.grid"] = True

square = np.array([
    [1, 1],
    [-1, 1],
    [-1, -1],
    [1, -1],
    [1, 1] #close the shape
])

angle = 45 #change angle here
theta = np.deg2rad(angle)

R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

rotated = square @ R.T #transposed to match orientations

#rotate all points of the square
plt.plot(square[:,0], square[:,1], 'b-', label = 'Original')
plt.plot(rotated[:,0], rotated[:,1], 'r-', label = 'Rotated')

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.legend()
plt.gca().set_aspect('equal')
plt.title("Rotating a shape")
plt.show()