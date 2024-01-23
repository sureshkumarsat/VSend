number = int(input("ENTER A 4 DIGIT NUMBER : "))

sum = 0

if 999 < number < 10000:
    r = number
    while r > 0:
        sum += r % 10
        r = r // 10
    print(f"SUM = {sum}")
else:
    print("ENTER VALID NUMBER.")
