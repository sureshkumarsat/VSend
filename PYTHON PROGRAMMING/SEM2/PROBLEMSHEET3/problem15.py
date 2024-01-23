for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("\n")

print("\n")

for i in range(6, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("\n")

print("\n")

for row in range(1, 7):
    for space in range(1, 7 - row + 1):
        print(" ", end=" ")

    for num in range(1, row + 1):
        print(num, end=" ")
    print("\n")
