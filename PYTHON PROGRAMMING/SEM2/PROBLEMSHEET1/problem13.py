x1 = int(input("ENTER X1 : "))
y1 = int(input("ENTER Y1 : "))
x2 = int(input("ENTER X2 : "))
y2 = int(input("ENTER Y2 : "))

dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)

print(f"Distance between ({x1}, {y1}) and ({x2}, {y2}) is {dist}")
