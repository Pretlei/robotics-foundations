import math
from point2d import point

def findDist(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y -b.y) ** 2)

a = point(2, 3)
b = point (5, 4)

b.changeX(3)

print("Points:")
a.print()
b.print()
print()

dist1 = findDist(a, b)

print("Distance:")
print(dist1)
print(findDist(b,a))

print(findDist(a, a))

print(round(dist1, 2))