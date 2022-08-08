from matplotlib import pyplot as plt

from src.planar_configurations import *

#---- test functions

# input parameters
RADIUS_INPUT    = 1          # crank
RADIUS_OUTPUT   = 2          # output lever/shoulder
CONROD_LENGTH   = 3          # linkage between crank and output
Y_OUTPUT        = 3          # vertical offset of output lever
X_OUTPUT        = 0.1        # horizontal offset of output lever
X_INPUT         = 0.2        # horizontal offset of crank
ANG_OFFSET_DUAL = 0.55       # angular offset between cranks - staggered configuration 
ANG_OFFSET_STAG = 1.2

# display configurations
anim1 = staggeredCrankAnim(RADIUS_INPUT, RADIUS_OUTPUT, CONROD_LENGTH, X_OUTPUT, Y_OUTPUT, ANG_OFFSET_STAG)
anim2 = duelCrankOppositeAnim(RADIUS_INPUT, RADIUS_OUTPUT, CONROD_LENGTH, X_INPUT, X_OUTPUT, Y_OUTPUT)
anim3 = duelCrankCommonAnim(RADIUS_INPUT, RADIUS_OUTPUT, CONROD_LENGTH, X_INPUT, X_OUTPUT, Y_OUTPUT, ANG_OFFSET_DUAL)
anim4 = insideOutCrankAnim(RADIUS_INPUT, RADIUS_OUTPUT, CONROD_LENGTH, X_OUTPUT, Y_OUTPUT)
plt.show() 

# Note: Run this script to visualize each configuration
