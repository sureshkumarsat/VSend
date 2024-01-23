print("What do you want to find? ")
print("")
x = int(
    input(
        """1. Simple Interest
2. Maturity Value
3. Compound Interest

Option : """
    )
)

if x == 1:
    p = float(input("Enter Principle Amount : "))
    r = float(input("Enter Interest Rate : "))
    t = float(input("Enter Time in Years : "))

    simple_interest = p * r * t
    print("The Simple Interest is : ", simple_interest)

if x == 2:
    p = float(input("Enter Principle Amount : "))
    r = float(input("Enter Interest Rate : "))
    t = float(input("Enter Time in Years : "))

    maturity_value = p * (1 + (r * t))
    print("The Maturity Value is : ", maturity_value)

if x == 3:
    p = float(input("Enter Principle Amount : "))
    r = float(input("Enter Interest Rate : "))
    t = float(input("Enter Time in Years : "))

    compound_interest = p * (1 + r) ** t
    print("The Compound Interest is : ", compound_interest)
