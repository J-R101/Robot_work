import numpy as np
import matplotlib.pyplot as plt


#code to plot the centre of mass of different positions of Nao relative to the seat, information from webots



# centre of mass above seat
heights = {'neutral_pos': 0.11108916903184612, 'TBLO': 0.10402009906673844, 'TFLI': 0.12323499351222672, 'TFLO': 0.128044164734476, 'TBLI':0.0959369967109733, 'prev_TBLI': 0.10160066421912234, 'prev_TBLO': 0.11098698104109651}
#centre of mass along x axis
x = {'neutral_pos': -0.010169540236488125, 'TBLO': -0.07673366861008599, 'TFLI': 0.0044895709090564395, 'TFLO': 0.03073794496618163, 'TBLI': -0.09191656472137516, 'prev_TBLI': -0.053402984233875433, 'prev_TBLO': -0.03268460500535892}

for key in heights:
    plt.scatter(x[key], heights[key], label = key)


#plotting
plt.ylim(0,0.15)
plt.xlim(-0.15, 0.1)
plt.ylabel("Z-position")
plt.title("Nao's centre of mass for varying positions")
plt.xlabel("x-Position ")
plt.grid()
plt.legend()
plt.show()




