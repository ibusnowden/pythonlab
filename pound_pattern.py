for row in range(7):
    for col in range(row + 2):
        if col == 0 or col == row + 1:
            print("#", end='')
        else:
            print(" ", end= '')
    print(" ")

