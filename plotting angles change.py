import plotting_joint_cycle as pj
import matplotlib.pyplot as plt
import numpy as np

Rjointlist = ["RWristYaw",
"RHipPitch",
"RElbowYaw",
"RShoulderPitch",


"RShoulderRoll",


"RElbowRoll"]

for joint in Rjointlist:
    x = []
    for pos in pj.cycle:
        x.append(np.abs(pos[joint]))


    counter = list(np.arange(1,9))
    plt.plot(counter, x, label = joint[1:])



plt.xticks(fontsize = 19)
plt.yticks(fontsize = 19)

plt.title("Absolute value of joint angle throughout lean forward motion", fontsize = 20)
plt.xlabel("position in cycle", fontsize = 20)
plt.ylabel("Joint angle (radians)", fontsize = 20)
plt.legend(prop={'size': 14})
plt.show()
