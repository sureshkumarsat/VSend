x1 = int(input("ENTER X1 : "))
y1 = int(input("ENTER Y1 : "))
x2 = int(input("ENTER X2 : "))
y2 = int(input("ENTER Y2 : "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)

print(f"DISTANCE BETWEEN ({x1}, {y1}) AND ({x2}, {y2}) IS {distance}")
