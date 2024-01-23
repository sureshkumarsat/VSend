White_List = []
Black_List = []

Letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

for i in range(0, 8):
    for j in range(1, 9):
        if Letters[i] in ["a", "c", "e", "g"]:
            if j % 2 == 0:
                White_List.append(f"{Letters[i]}{j}")
            else:
                Black_List.append(f"{Letters[i]}{j}")
        elif Letters[i] in ["b", "d", "f", "h"]:
            if j % 2 == 1:
                White_List.append(f"{Letters[i]}{j}")
            else:
                Black_List.append(f"{Letters[i]}{j}")

letter = input("ENTER LETTER : ")
number = int(input("ENTER NUMBER : "))
square = f"{letter}{number}"

if square in Black_List:
    print(f"{square} is black.")
elif square in White_List:
    print(f"{square} is white.")
else:
    print("ENTER VALID SQUARE.")
