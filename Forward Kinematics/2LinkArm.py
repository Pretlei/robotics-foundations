import numpy as np

def fk_2link(theta1, theta2, l1 = 1.0, l2 = 1.0):
    x1 = l1 * np.cos(theta1)
    y1 = l1 * np.sin(theta1)

    x2 = x1 + l2*np.cos(theta1 + theta2)
    y2 = y1 + l2*np.sin(theta1 + theta2)

    return (0,0), (float(x1), float(y1)), (float(x2), float(y2)) #converting numpy formatting to float

base, joint, tip = fk_2link(np.pi/4, np.pi/4)
print(base)
print(joint)
print(tip)