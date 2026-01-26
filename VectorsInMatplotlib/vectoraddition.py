import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = (5, 5)
plt.rcParams["axes.grid"] = True

v1 = np.array([2, 1])
v2 = np.array([1, 2])
v_sum = v1 + v2

plt.axhline(0, color='gray')
plt.axvline(0, color='gray')

#Blue + Green = Red
plt.quiver(0, 0, v1[0], v1[1], angles = 'xy', scale_units = 'xy', scale = 1, color = 'blue') #plot v1
plt.quiver(v1[0], v1[1], v2[0], v2[1], angles = 'xy', scale_units = 'xy', scale = 1, color = 'green') # plot v2 at tip of v1
plt.quiver(0, 0, v_sum[0], v_sum[1], angles = 'xy', scale_units = 'xy', scale = 1, color = 'red') #plot v_sum

plt.xlim(0, 3)
plt.ylim(-0, 3)
plt.gca().set_aspect('equal')
plt.title("Vector Addition")
plt.show()