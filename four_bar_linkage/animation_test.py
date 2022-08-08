from matplotlib import pyplot as plt

from src.planar_configurations import *

#---- test functions

# input parameters
RADIUS_INPUT  = 1      # crank
RADIUS_OUTPUT = 2      # output lever/shoulder
CONROD_LENGTH = 3      # linakge between crank and output
Y_OUTPUT = 3           # vertical offset of output lever
X_OUTPUT = 0.1         # horizontal offset of output lever
X_INPUT  = 0.2         # horizontal offset of crank
ANG_OFFSET = 1.2       # angular offset between cranks - staggered configuration 

# display configurations
anim1 = staggeredCrankAnim(RADIUS_INPUT, RADIUS_OUTPUT, CONROD_LENGTH, X_OUTPUT, Y_OUTPUT, ANG_OFFSET)
anim2 = duelCrankAnim(RADIUS_INPUT, RADIUS_OUTPUT, CONROD_LENGTH, X_INPUT, X_OUTPUT, Y_OUTPUT)
anim3 = insideOutCrankAnim(RADIUS_INPUT, RADIUS_OUTPUT, CONROD_LENGTH, X_OUTPUT, Y_OUTPUT)
plt.show() 

# Note: Run this script to visualize each configuration
