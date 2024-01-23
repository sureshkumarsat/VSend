def LatinSquare(n):
    Latinsquare = []
    k = n + 1
    for i in range(1, n + 1):
        temp = k
        row = []
        while temp <= n:
            row.append(temp)
            temp += 1
        for j in range(1, k):
            row.append(j)
        k -= 1
        Latinsquare.append(row)
    return Latinsquare


n = int(input("ENTER n : "))
user_square = []
for i in range(0, n):
    row = []
    for j in range(0, n):
        element = int(input(f"ENTER ELEMENT[{i}][{j}] : "))
        row.append(element)
    user_square.append(row)

flag = 1
for i in user_square:
    if i not in LatinSquare(n):
        flag = 0
        break

if flag == 1:
    print("USER HAS ENTERED A LATIN SQUARE")
else:
    print("USER HAS NOT ENTERED A LATIN SQUARE")
