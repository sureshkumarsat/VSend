s1 = float(input("ENTER SIDE 1 : "))
s2 = float(input("ENTER SIDE 2 : "))
s3 = float(input("ENTER SIDE 3 : "))

s = s1 + s2 + s3 / 2

area = (s * (s - s1) * (s - s2) * (s - s3)) ** (1 / 2)

print(f"AREA = {area}")
