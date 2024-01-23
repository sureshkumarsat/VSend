import math


t1 = float(input("ENTER  T1 : "))
g1 = float(input("ENTER  G1 : "))
t2 = float(input("ENTER  T2 : "))
g2 = float(input("ENTER  G2 : "))


distance = 6371.01 * math.acos(
    math.radians(
        (math.sin(math.radians(t1)) * math.sin(math.radians(t2)))
        + (
            math.cos(math.radians(t1))
            * math.cos(math.radians(t2))
            * math.cos(math.radians(g1 - g2))
        )
    )
)
print(distance)
