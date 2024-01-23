number = int(input("ENTER NUMBER : "))

factor = 2
while factor <= number:
    if number % factor == 0:
        print(factor)
        number /= factor
    else:
        factor += 1
