import math

r = float(input("ENTER DISTANCE FROM ORIGIN : "))
theta = float(input("ENTER ANGLE WITH X-AXIS : "))

x = r * (math.cos(theta))
y = r * (math.sin(theta))

print(f"THE REQUIRED CO-ORDINATES ARE ({x}, {y})")
