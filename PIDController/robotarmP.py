import numpy as np
import matplotlib.pyplot as plt

#robot arm to be kept at a desired angle (prevent overshoot or undershoot using a PID Controller)

dt = 0.01
T = 5.0
steps = int(T/dt) #number of iterations

b = 0.99 # damping coefficient (D in PID)

#state
theta = 0.0 #initial angle
omega = 0.0 #initial angular velocity

#desired
thetaDesired = 1.0 #around 57 degrees

thetaLog = []
timeLog = []

Kp = 10.0 #proportional gain

for i in range(steps):
    error = thetaDesired - theta
    u = Kp*error  # the motor torque outputted by the controller to the actuator

    omega += (u - b * omega) * dt # acceleration to velocity, subtracted by the damping coefficient
    theta += omega * dt # angular velocity to angle

    thetaLog.append(theta)
    timeLog.append(i * dt)

#plot
plt.plot(timeLog, thetaLog, label="Joint angle") # (x, y, label of line)
plt.axhline(thetaDesired, color="r", linestyle="--", label="Desired angle") # desired y level (angle) line
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.title("P Control of Joint Angle")
plt.legend()
plt.grid()
plt.show()