Principal = float(input("ENTER LOAN AMOUNT : "))
years = int(input("ENTER NUMBER OF YEARS : "))
AnnualInterest = int(input("ENTER ANNUAL INTEREST RATE : "))

Total_Payment = Principal + (Principal * 7 * years) / 100
Monthly_Payment = Total_Payment / 12

print(f"MONTHLY PAYMENT : {Monthly_Payment}\nTOTAL PAYMENT : {Total_Payment}")

print("PAYMENT#\tINTEREST\tPRINCIPAL\tBALANCE")
count = 1
Balance = Principal

while count <= years * 12:
    Interest = Balance * AnnualInterest / 1200
    MonthlyPrincipal = Monthly_Payment - Interest
    Balance -= MonthlyPrincipal
    print(
        f"{count}.\t{Interest}\t{MonthlyPrincipal}\t{Balance}\t{MonthlyPrincipal+Interest}"
    )
    count += 1
