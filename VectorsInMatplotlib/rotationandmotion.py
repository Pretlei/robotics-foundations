import matplotlib.pyplot as plt
import numpy as np

#rotating a vector fixed on origin over time

plt.rcParams["figure.figsize"] = (5, 5)
plt.rcParams["axes.grid"] = True

angles = np.linspace(0, 2*np.pi, 100) #100 subdivisions of numbers from 0 to ~6.28
length = 3 #scale by 3

xs = length * np.cos(angles)
ys = length * np.sin(angles)

plt.plot(xs, ys, 'k--')

for i in range(0, len(angles), 10): #every 10th (100/10 = 10) angle gets the vector rotated to it 
    plt.quiver(0, 0, xs[i], ys[i], scale=1, scale_units='xy', alpha=0.4)

plt.gca().set_aspect('equal')
plt.title("Rotating vector over time")
plt.show()
