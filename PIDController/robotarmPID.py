import numpy as np
import matplotlib.pyplot as plt

# state
theta = 0.0
omega = 0.0

# desired
thetaDesired = 1.0

# PID gains
# want very fast rise times (P), small controlled overshoot (D), almost no oscillations (D), no steady-state error (I
# in real hardware, make sure Kp and Ki isn't too aggressive
Kp = 30.0 #increase until response is fast but stable 
Ki = 10.0 #increase to remove steady-state error (when the joint doesn't quite reach the target, there's a little bit left)
Kd = 20.0 #increase to reduce oscillation

#errors
integral_error = 0.0
prev_error = 0.0

thetaLog = []
timeLog = []

# parameters
dt = 0.01 # time per frame
T = 5.0 # simulation time
steps = int(T / dt) #number of frames

# Joint parameters
b = 0.2           

# run simulation
for i in range(steps):
    error = thetaDesired - theta
    integral_error += error*dt
    derivative_error = (error - prev_error)/dt

    u = (Kp*error + Ki*integral_error + Kd*derivative_error)

    omega += (u - b*omega) * dt
    theta += omega * dt

    prev_error = error

    thetaLog.append(theta)
    timeLog.append(i * dt)

# plot
plt.plot(timeLog, thetaLog, label="Joint angle")
plt.axhline(thetaDesired, color="r", linestyle="--", label="Desired angle")
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.title("PID Control of Joint Angle")
plt.legend()
plt.grid()
plt.show()
