StocksPurchased = 1000
CostPrice = 32.87
Commision = 0.02
StocksSold = 1000
SellingPrice = 33.92

AmountStock = StocksPurchased * CostPrice
CommisionPaid = AmountStock * Commision
AmountSold = StocksSold * SellingPrice
CommisionSold = AmountSold * Commision

Total = AmountSold - (AmountStock + CommisionPaid + CommisionSold)

if Total > 0:
    Profit = f"JOE MADE A PROFIT OF {Total}"
else:
    Profit = f"JOE MADE A LOSS OF {0-Total}"

string = f"AMOUNT OF MONEY JOE PAID FOR THE STOCK : {AmountStock}\nAMOUNT OF COMMISION WHILE BUYING STOCK : {CommisionPaid}\nAMOUNT JOE SOLD THE STOCK FOR : {AmountSold}\nAMOUNT OF COMMISION PAID WHILE SELLING STOCK : {CommisionSold}\n{Profit}"
print(string)
