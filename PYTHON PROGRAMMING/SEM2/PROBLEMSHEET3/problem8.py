Caps = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
Small = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

message = input("ENTER MESSAGE : ")
new_message = ""
for i in range(0, len(message)):
    if message[i] in Small:
        index = Small.index(message[i])
        if index < 23:
            new_message += Small[index + 3]
        else:
            new_message += Small[index - 23]
    elif message[i] in Caps:
        index = Caps.index(message[i])
        if index < 23:
            new_message += Caps[index + 3]
        else:
            new_message += Caps[index - 23]
    else:
        new_message += message[i]

print(f"CAESER'S CIPHER : \n{new_message}")
