day = int(input("\nWhich day of the week does the month start ? "))
tot_days = int(input("\nHow many days does the month have ? "))


if not (day >= 0 and day <= 7):
    print("\nInvalid Number of the Day of the Week .")
    exit(0)
if tot_days == 28 or tot_days == 29 or tot_days == 30 or tot_days == 31:
    d = 0
    v = 1
    print("\nSu Mo Tu We Th Fr Sa \n")
    c = 1
    for i in range(1, tot_days + 1):
        if c == 1:
            for j in range(1, 3 * day + 1, 1):
                print(" ", end="")
                c = c + 1
        if i < 10:
            print(i, end="  ")
        else:
            print(i, end=" ")
        if 7 - day == i:
            print("\n")
            d = i
        if d + v * 7 == i:
            v = v + 1
            print("\n")
else:
    print("\nInvalid Number of Dates for the Month .")
