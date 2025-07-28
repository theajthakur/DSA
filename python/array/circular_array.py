array = [4, 8, 3, 9]

# Number of rotations
n = 10

# Clockwise Rotation
print("Clockwise Rotation:")
for x in range(0, n):
    print(array[(x + n) % len(array)])

# AntiClockwise Rotation
print("\nAntiClockwise Rotation:")
for x in range(0, n):
    print(array[(x - n) % len(array)])
