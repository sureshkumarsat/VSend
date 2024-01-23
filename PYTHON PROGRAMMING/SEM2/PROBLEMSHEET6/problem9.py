matrix = []
m = int(input("ENTER NUMBER OF ROWS IN MATRIX : "))
n = int(input("ENTER NUMBER OF COLUMNS IN MATRIX : "))

triples_value = []

for i in range(0, m):
    row = []
    for j in range(0, n):
        element = int(input(f"ENTER ELEMENT[{i}][{j}] : "))
        row.append(element)
        if element != 0:
            triples_value.append((i, j, element))
    matrix.append(row)

print("TRIPLES VALUE : ")
for i in triples_value:
    print(f"{i[0]} {i[1]} {i[2]}")
