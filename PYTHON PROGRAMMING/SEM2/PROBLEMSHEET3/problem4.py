s1 = int(input("ENTER SIDE 1 : "))
s2 = int(input("ENTER SIDE 2 : "))
s3 = int(input("ENTER SIDE 3 : "))


if s1 == s2 and s2 == s3 and s3 == s1:
    print("EQUILATERAL TRIANGLE")
elif s1 == s2 or s2 == s3 or s3 == s1:
    print("ISOSCELOUS TRIANGLE")
else:
    print("NEITHER EQUILATERAL NOR ISOSCELOUS TRIANGLE")
