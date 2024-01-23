# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 14:27:43 2022

@author: 21pc26
"""

res = "y"
while res == "y":
    stra = input("ENTER BIT STRING : ")
    ressult = ""
    option = int(input("1. SHL\n2. SHR\n3. CIL\n4. CIR\nENTER OPTION NUMBER: "))
    
    if option == 1:
        result = stra[1:len(stra)] + "0"
    elif option == 2:
        result = "0" + stra[0:len(stra)-1]
    elif option == 3:
        result = stra[1:len(stra)] + stra[0]
    elif option == 4:
        result = stra[-1] + stra[0:len(stra)-1]
    
    print(result)
    res = input("ENTER 'y' TO CONTINUE: ")