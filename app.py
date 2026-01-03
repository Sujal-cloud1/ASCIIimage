height = 17
width = 27

for i in range(height):
    for j in range(width):

        # Curly hair
        if i < 4 and 4 < j < 22:
            print("#", end="")

        # Face outline (top & bottom)
        elif (i == 4 or i == 14) and 5 < j < 21:
            print("*", end="")

        # Face sides
        elif (j == 6 or j == 20) and 4 < i < 14:
            print("*", end="")

        # Glasses / eyes
        elif i == 8 and (j == 10 or j == 16):
            print("O", end="")

        # Nose
        elif i == 10 and j == 13:
            print("|", end="")

        # Mouth
        elif i == 12 and 11 < j < 16:
            print("-", end="")

        else:
            print(" ", end="")
    print()
