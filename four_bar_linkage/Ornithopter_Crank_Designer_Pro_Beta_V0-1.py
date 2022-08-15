# Ornithopter Crank Designer Pro
# Version 0.1 Beta
# Last update: 8/15/2022

# Find the latest release at:
# https://github.com/OrnithopterX/Ornithopter-Crank-Designer-Pro

# todo: Test all systems
# todo: Add perfect inside-out staggered crank
# todo: Add Crank_offset term for inside-out staggered crank

# Supported Types:
Staggered_Crank = 0
Perfect_staggered_Crank = 1
Duel_Crank = 0
Insideout_staggered_Crank = 0


import math
from matplotlib import pyplot as plt
from src.planar_configurations import *


if Staggered_Crank == 1:
    print()
    print("Inputs for Staggered Crank")
    Dihedral = float(input("Dihedral: "))
    Anhedral = float(input("Anhedral: "))
    H = float(input("H: "))
    W = float(input("W: "))
    D = float(input("D: "))

    # helpers
    H2 = (math.sin(math.radians(Dihedral))) * W
    H3 = (math.sin(math.radians(Anhedral))) * W
    HA = H + H2
    HB = H - H3
    Y1 = (math.cos(math.radians(Dihedral))) * W
    Y2 = (math.cos(math.radians(Anhedral))) * W
    Z1 = math.sqrt(((Y1 + D) ** 2) + (HA ** 2))
    Z2 = math.sqrt(((Y2 + D) ** 2) + (HB ** 2))
    AxD = math.atan((Y1 + D) / HA) * 2
    AxU = math.atan((Y2 + D) / HB) * 2

    Crank_radii = (Z1 - Z2) / 2
    Linkage_length = Z1 - Crank_radii
    Crank_offset = (AxD + AxU) / 2

    # Print Output data
    print()
    print("Outputs")
    print("linkage Length: " + str(Linkage_length))
    print("Crank Offset: " + (str(math.degrees(Crank_offset))) + " degrees")
    print("Crank Radii: " + str(Crank_radii))

    anim = staggeredCrankAnim(Crank_radii, W, Linkage_length, D, H, Crank_offset)
    plt.show()

if Perfect_staggered_Crank == 1:
    # inputs
    print()
    print("Inputs for Perfect Staggered Crank")
    Flap_angle = float(input("Flap angle: "))
    H = float(input("H: "))
    W = float(input("W: "))
    D = float(input("D: "))

    # helpers
    Hs = math.sqrt((D ** 2) + (H ** 2))
    Aa = Flap_angle / 2
    Wr = math.cos(math.radians(Aa)) * W
    Axt = math.degrees(math.atan(D / H)) + (90 - math.degrees(math.acos(Wr / Hs)))

    # outputs
    Crank_radii = math.sin(math.radians(Aa)) * W
    Linkage_length = math.sqrt((Hs ** 2) - (Wr ** 2))
    Crank_offset = math.radians(Axt * 2)
    Dihedral_output = -(Axt - Aa)
    Anhedral_output = -(Dihedral_output - Flap_angle)

    # print output data
    print()
    print("Outputs")
    print("linkage Length: " + str(Linkage_length))
    print("Crank Offset: " + (str(math.degrees(Crank_offset))) + " degrees")
    print("Crank Radii: " + str(Crank_radii))
    print("Dihedral: " + str(Dihedral_output) + " degrees")
    print("Anhedral: " + str(Anhedral_output) + " degrees")

    anim = staggeredCrankAnim(Crank_radii, W, Linkage_length, D, H, Crank_offset)
    plt.show()


if Duel_Crank == 1:
    print()
    print("Inputs for Duel Crank")
    Dihedral = float(input("Dihedral: "))
    Anhedral = float(input("Anhedral: "))
    H = float(input("H: "))
    W = float(input("W: "))
    D = float(input("D: "))
    D2 = float(input("D2: "))

    # helpers
    Y1 = (math.cos(math.radians(Dihedral))) * W
    Y2 = (math.cos(math.radians(Anhedral))) * W
    D3 = (Y1 + D) - D2
    D4 = (Y2 + D) - D2
    H2 = (math.sin(math.radians(Dihedral))) * W
    H3 = (math.sin(math.radians(Anhedral))) * W
    HA = H + H2
    HB = H - H3
    Z1 = math.sqrt((D3 ** 2) + (HA ** 2))
    Z2 = math.sqrt((D4 ** 2) + (HB ** 2))
    AxD = math.atan(D4 / HB)
    AxU = math.atan(D3 / HA)

    # Outputs
    Crank_radii = (Z1 - Z2) / 2
    Linkage_length = Z1 - Crank_radii
    Crank_offset = (AxD + AxU) / 2

    # Print Output data
    print()
    print("Outputs")
    print("linkage Length: " + str(Linkage_length))
    print("Crank Offset: " + (str(math.degrees(Crank_offset))) + " degrees")
    print("Crank Radii: " + str(Crank_radii))

    anim = duelCrankOppositeAnim(Crank_radii, W, Linkage_length, D2, D, H)
    # anim = duelCrankCommonAnim(Crank_radii, W, Linkage_length, D2, D, H, Crank_offset)
    plt.show()


if Insideout_staggered_Crank == 1:
    print()
    print("Inputs for Inside-out staggered Crank")
    Dihedral = float(input("Dihedral: "))
    Anhedral = float(input("Anhedral: "))
    H = float(input("H: "))
    W = float(input("W: "))
    D = float(input("D: "))

    # helpers
    Y1 = D / 2 - (math.cos(math.radians(Anhedral))) * W
    Y2 = D / 2 - (math.cos(math.radians(Dihedral))) * W
    H2 = (math.sin(math.radians(Anhedral))) * W
    H3 = (math.sin(math.radians(Dihedral))) * W
    HA = H + H2
    HB = H - H3
    Z1 = math.sqrt((Y1 ** 2) + (HA ** 2))
    Z2 = math.sqrt((Y2 ** 2) + (HB ** 2))
    AxD = math.atan(Y1 / HA) * 2
    AxU = math.atan(Y2 / HB) * 2

    # outputs
    Crank_radii = (Z1 - Z2) / 2
    Linkage_length = Z1 - Crank_radii
    Crank_offset = (AxD + AxU) / 2

    # Print Output data
    print()
    print("Outputs")
    print("linkage Length: " + str(Linkage_length))
    print("Crank Offset: " + (str(math.degrees(Crank_offset))) + " degrees")
    print("Crank Radii: " + str(Crank_radii))

    anim = insideOutCrankAnim(Crank_radii, W, Linkage_length, D, H)    #todo: add crank offset for animation
    plt.show()
