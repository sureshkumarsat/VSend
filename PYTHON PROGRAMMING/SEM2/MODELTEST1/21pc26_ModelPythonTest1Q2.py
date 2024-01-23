n = int(input("ENTER ANY ODD NUMBER : "))


def print_matrix(matrix):
    for i in matrix:
        for j in i:
            if j == " ":
                print(f" {j}", end=" ")
            elif j < 10:
                print(f" {j}", end=" ")
            else:
                print(j, end=" ")
        print("\n")


matrix = []
for i in range(n):
    matrix.append([" "] * n)
down = 1
right = 1
up = 2
left = 2
count = 0
pos = [n // 2, n // 2]
matrix[pos[0]][pos[1]] = 1
i = 2
while i < n * n + 1:
    for j in range(down):
        pos[0] += 1
        matrix[pos[0]][pos[1]] = i
        i += 1
        count += 1
    if down + 2 == n:
        down += 1
    else:
        down += 2
    if i > n * n:
        break
    for j in range(right):
        pos[1] += 1
        matrix[pos[0]][pos[1]] = i
        i += 1
        count += 1
    if right + 2 == n:
        right += 1
    else:
        right += 2
    if i > n * n:
        break
    for j in range(up):
        pos[0] -= 1
        matrix[pos[0]][pos[1]] = i
        i += 1
        count += 1
    if up + 2 == n:
        up += 1
    else:
        up += 2
    if i > n * n:
        break
    for j in range(left):
        pos[1] -= 1
        matrix[pos[0]][pos[1]] = i
        i += 1
        count += 1
    if left + 2 == n:
        left += 1
    else:
        left += 2
    if i > n * n:
        break
print_matrix(matrix)
