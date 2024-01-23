capitals = [
    ["Alabama", "Montgomery"],
    ["Alaska", "Juneau"],
    ["Arizona", "Phoenix"],
    ["Arkansas", "Little Rock"],
    ["California", "Sacramento"],
    ["Colorado", "Denver"],
    ["Connecticut", "Hartford"],
    ["Delaware", "Dover"],
    ["Florida", "Tallahassee"],
    ["Georgia", "Atlanta"],
]
correctcount = 0

for i in range(len(capitals)):
    cap = input("What is the capital of " + capitals[i][0] + "? ")
    if cap.lower() == capitals[i][1].lower():
        correctcount += 1
        print("Your answer is correct")
    else:
        print("The correct answer should be", capitals[i][1])
print("The correct count is", correctcount)
