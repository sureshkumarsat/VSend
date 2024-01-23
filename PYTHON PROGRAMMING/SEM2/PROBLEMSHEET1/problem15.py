name = input("ENTER MOVIE NAME : ")
AdultTickets = int(input("ENTER NO. OF ADULT TICKETS SOLD : "))
ChildTickets = int(input("ENTER NO. OF CHILD TICKETS SOLD : "))
Profit_Percent = int(input("ENTER PROFIT  PERCENT : "))

GrossProfit = AdultTickets * 6 + ChildTickets * 3

Profit = GrossProfit * Profit_Percent / 100

print(
    f"MOVIE NAME : {name}\nNO. OF ADULT TICKETS : {AdultTickets}\nNO. OF CHILD TICKETS : {ChildTickets}\nGROSS PROFIT : {GrossProfit}\nNET BOX OFFICE PROFIT : {Profit}\nAMOUNT PAID TO DISTRIBUTOR : {GrossProfit-Profit}"
)
