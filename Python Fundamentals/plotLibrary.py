import matplotlib.pyplot as pl
import numpy as np

x_coords = np.array([1, 3, 5, 7])
y_coords = np.array([2, 4, 6, 8])

pl.scatter(x_coords, y_coords)
pl.title("Scatter Plot")
pl.xlabel("X")
pl.ylabel("Y")
pl.xlim(0, 10)
pl.ylim(0, 10)

pl.show()
