# Ornithopter Crank Designer Pro
# Basic Staggered Crank Equations
# Version: 1.00 Beta.
# By: Joshua Adcock
# 8/2/2022


# ========== Staggered Crank ==========  << Working >>
# Inputs
import math

H = float(input("H term: "))
W = float(input("W term: "))
D = float(input("D term: "))
Dihedral = float(input("Dihedral: "))
Anhedral = float(input("Anhedral: "))

# Helpers
H2 = (math.sin(math.radians(Dihedral))) * W
H3 = (math.sin(math.radians(Anhedral))) * W
HA = H + H2
HB = H - H3
Y1 = (math.cos(math.radians(Dihedral))) * W
Y2 = (math.cos(math.radians(Anhedral))) * W
Z1 = math.sqrt(((Y1 + D) ** 2) + (HA ** 2))
Z2 = math.sqrt(((Y2 + D) ** 2) + (HB ** 2))

# Outputs
Crank_radii = (Z1 - Z2)/2
Linkage_length = Z1 - Crank_radii
AxD = math.degrees(math.atan((Y1 + D)/HA) * 2)
AxU = math.degrees(math.atan((Y2 + D)/HB) * 2)
Ax = (AxD + AxU)/2

# Print Outputs
print("Crank radii: " + str(Crank_radii))
print("Ax: " + str(Ax))
print("Linkage length: " + str(Linkage_length))