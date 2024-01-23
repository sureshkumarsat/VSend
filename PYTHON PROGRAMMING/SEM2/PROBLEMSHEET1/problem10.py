weight_pounds = float(input("ENTER HEIGHT(pounds) : "))
height_inches = float(input("ENTER WEIGHT(inches) : "))

bmi = (weight_pounds * 0.45359237) / ((height_inches * 0.0254) ** 2)

print(
    "BMI :",
    "{:.2f}".format(bmi),
)
