# Ornithopter Crank Designer Pro
# Perfect Staggered Crank Equations
# Version: 1.00 Beta.
# By: Joshua Adcock
# 8/3/2022


# ========== Perfect Staggered Crank ==========  << Working >>
import math

# Inputs (change these)
H = 3000
W = 400
D = 400
Flap_angle = 35.6

# Helpers

AxP = math.degrees(math.atan(D/H))
Hs = math.sqrt((D ** 2) + (H ** 2))
Aa = Flap_angle / 2
Wr = math.cos(math.radians(Aa)) * W
Ax = 90 - math.degrees(math.acos(Wr/Hs))
Axt = AxP + Ax

# Outputs
Crank_radii = math.sin(math.radians(Aa)) * W
Linkage_length = math.sqrt((Hs ** 2) - (Wr ** 2)) - Crank_radii
Crank_angle = Axt * 2
Dihedral = -1 * (Axt - Aa)
Anhedral = -1 * (Dihedral - Flap_angle)

# Print Outputs
print("Crank radii: " + str(Crank_radii))
print("Crank angle: " + str(Crank_angle))
print("Linkage length: " + str(Linkage_length))
print("Dihedral: " + str(Dihedral))
print("Anhedral: " + str(Anhedral))
