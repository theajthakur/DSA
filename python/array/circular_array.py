array=[4,8,3,9]


# Clockwise Rotation
for x in range(0,10):
    print(array[x%len(array)])



# AntiClockwise Rotation
for x in range(0,10):
    print(array[(len(array)-1)-x%len(array)])