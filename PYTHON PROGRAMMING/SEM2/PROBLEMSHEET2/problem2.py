import math

NoSides = int(input("ENTER NUMBER OF SIDES : "))
Sides = float(input("ENTER LENGTH OF SIDE : "))

pi = 3.14
area = (NoSides * Sides * Sides) / (4 * (math.tan(pi / NoSides)))
print(f"AREA IS {area}")
