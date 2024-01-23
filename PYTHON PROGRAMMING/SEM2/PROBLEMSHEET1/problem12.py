name = input("ENTER EMPLOYEE NAME : ")
Hours_per_week = float(input("ENTER HOURS PER WEEK : "))
pay_per_hour = float(input("ENTER PAY PER HOUR : "))
FederalTax = float(input("ENTER RATE OF FEDERAL TAX : "))
StateTax = float(input("ENTER RATE OF STATE TAX : "))

GrossPay = pay_per_hour * Hours_per_week
FederalWitholding = FederalTax * GrossPay / 100
StateWitholding = StateTax * GrossPay / 100
TotalDeduction = FederalWitholding + StateWitholding
NetPay = GrossPay - TotalDeduction

display_string = f"EMPLOYEE NAME : {name}\nHOURS WORKED : {Hours_per_week}\nPAY RATE : $ {pay_per_hour}\nGROSS PAY : $ {GrossPay}\nDEDUCTIONS :\n\tFEDERAL WITHOLDING : $ {FederalWitholding}\n\tSTATE WITHOLDING : $ {StateWitholding}\n\tTOTAL DEDUCTION : $ {TotalDeduction}\nNET PAY : $ {NetPay}"

print(display_string)
