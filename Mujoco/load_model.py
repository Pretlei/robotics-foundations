import mujoco
import time

model = mujoco.MjModel.from_xml_path("C:/Users/Presl/Projects/1A_Robotics/Mujoco/simple_pendulum.xml") #import model
data = mujoco.MjData(model) #simulation data creation

for i in range(1000):
    # data.ctrl --> each index corresponds to one actuator
    data.ctrl[0] = 10.0   # apply constant torque
    mujoco.mj_step(model, data)

    if i%100 == 0:
        print("angle:", data.qpos[0])

# paste 
# python -m mujoco.viewer --mjcf="C:/Users/Presl/Projects/1A_Robotics/Mujoco/simple_pendulum.xml" 
# into terminal