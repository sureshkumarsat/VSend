drive_dist = float(input("ENTER DISTANCE TO DRIVE : "))
miles_per_gallon = float(input("ENTER MILES PER GALLON : "))
price_per_gallon = float(input("ENTER PRICE PER GALLON : "))

total = (drive_dist / miles_per_gallon) * price_per_gallon

print("THE TOTAL PRICE : ", total)
