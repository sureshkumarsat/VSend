# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:48:43 2022

@author: 21pc26
"""

res = 'y'
while res == "y":
    num = int(input("ENTER DECIMAL NUMBER: "))
    option = int(input("1. BINARY\n2. OCTAL\n3. HEXADECIMAL\nENTER OPTION NUMBER: "))
    if option == 1:
        print(bin(num)[2:])
    elif option == 2:
        print(oct(num)[2:])
    elif option == 3:
        print(hex(num)[2:])
    res = input("ENTER 'y' TO CONTINUE: ")
