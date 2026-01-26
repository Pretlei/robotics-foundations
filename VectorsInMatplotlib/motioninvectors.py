import matplotlib.pyplot as plt
import numpy as np

#drawing a group of points, but it's to depict motion
#i don't understand it totally

plt.rcParams["figure.figsize"] = (5, 5)
plt.rcParams["axes.grid"] = True

t = np.linspace(0, 2*np.pi, 200) # 200 subdivisions of numbers up to PI*2

x = np.cos(t)
y = np.sin(t)

dt = t[1] - t[0]

#derivative
vx = np.gradient(x, dt)
vy = np.gradient(y, dt)

plt.plot(x, y, 'k-')

plt.quiver(
    x[::15], y[::15],#every 15th element in x and y
    vx[::15], vy[::15],
    color='blue'
)

plt.gca().set_aspect('equal')
plt.title("Motion with velocity vectors")
plt.show()