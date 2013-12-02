for asseX in range(0, 40):
    for assY in range(0, 30):
        if asseX == 0 or asseX == 39 or assY == 0 or assY == 29:
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print()