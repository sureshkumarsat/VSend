print("0  1  2  3  4  5  6  7  8  9  10")
for i in range(1, 11):
    print(i, end="  ")
    for j in range(1, 11):
        print(i * j, end="  ")
    print("\n")
