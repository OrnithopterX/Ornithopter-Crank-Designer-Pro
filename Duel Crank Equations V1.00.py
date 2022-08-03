# Ornithopter Crank Designer Pro
# Duel Crank Equations
# Version: 1.00 Beta.
# By: Joshua Adcock
# 8/3/2022


# ========== Duel Crank ==========  << Working >>
# Inputs
import math

H = float(input("H term: "))
W = float(input("W term: "))
D1 = float(input("D1 term: "))
D2 = float(input("D2 term: "))
Dihedral = float(input("Dihedral: "))
Anhedral = float(input("Anhedral: "))

# Helpers
Y1 = (math.cos(math.radians(Dihedral))) * W
Y2 = (math.cos(math.radians(Anhedral))) * W
D3 = (Y1 + D1)-D2
D4 = (Y2 + D1)-D2
H2 = (math.sin(math.radians(Dihedral))) * W
H3 = (math.sin(math.radians(Anhedral))) * W
HA = H + H2
HB = H - H3
Z1 = math.sqrt((D3 ** 2) + (HA ** 2))
Z2 = math.sqrt((D4 ** 2) + (HB ** 2))

# Outputs
Crank_radii = (Z1 - Z2)/2
Linkage_length = Z1 - Crank_radii
AxD = math.degrees(math.atan(D4/HB))
AxU = math.degrees(math.atan(D3/HA))
Ax = (AxD + AxU)/2

# Print Outputs
print("Crank radii: " + str(Crank_radii))
print("Ax: " + str(Ax))
print("Linkage length: " + str(Linkage_length))
