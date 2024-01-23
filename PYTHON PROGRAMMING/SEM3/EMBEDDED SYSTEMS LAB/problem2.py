# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:03:34 2022

@author: 21pc26
"""



res = "y"
while res == "y":
    stra = input("ENTER BIT STRING 1: ")
    strb = input("ENTER BIT STRING 2: ")
    
    
    if len(stra) < len(strb):
        stra = "0" * (len(strb) - len(stra)) + stra
    elif len(strb) < len(stra):
        strb = "0" * (len(stra) - len(strb)) + strb
    print(stra)
    print(strb)    
    result = ""
    option = int(input("1. OR\n2. AND\n3. XOR\n4. NAND\nENTER OPTION NUMBER: "))
    
    if option == 1:
        for i in range(-len(stra), 0):
            if stra[i] == "1" or strb[i] == "1":
                result += "1"
            else:
                result += "0"
        print(result)

    elif option == 2:
        for i in range(-len(stra), 0):
            if stra[i] == "0" or strb[i] == "0":
                result += "0"
            else:
                result += "1"
        print(result)
    
    elif option == 3:
        for i in range(-len(stra), 0):
            if stra[i] == strb[i]:
                result += "0"
            else:
                result += "1"
        print(result)
    
    elif option == 4:
        for i in range(-len(stra), 0):
            if stra[i] == "0" or strb[i] == "0":
                result += "1"
            else:
                result += "0"
        print(result)

    res = input("ENTER 'y' TO CONTINUE: ")
            
            
