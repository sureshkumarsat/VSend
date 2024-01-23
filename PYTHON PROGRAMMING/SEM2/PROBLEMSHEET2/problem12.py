import random as r

number = r.randrange(1, 100)
# print(number)
while True:
    x = int(input("Guess Number Between 1-100 : "))
    if x < number:
        print("Too Low, Try Again")

    if x > number:
        print("Too High, Try Again")

    if x == number:
        print("CONGRATULATIONS, YOU GUESSED CORRECT!!!")
        break
