def savings(p, i, t):
    f = p * ((1 + i) ** t)
    return f


p = float(input("Enter Present Value : "))
i = float(input("Enter Monthly Inerest : "))
t = float(input("Enter Number of Months : "))

print(savings(p, i, t))
