# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 08:50:11 2022

@author: 21pc26
"""

import sys, os


def readLastN(file = 'problem7.txt', n = 5):
    if os.path.exists(file):
        with open(file, 'r') as f:
            lines = f.readlines()
        if int(n) > len(lines):
            return "More lines than in file."
        else:
            return lines[-int(n)-1: -1]
    else:
        return "File Does Not Exist."


if len(sys.argv) == 4:
    response = readLastN(sys.argv[1], sys.argv[3])
    if response == "File Does Not Exist." or response == "More lines than in file.":
        print(response)
    else:
        for i in response:
            print(i)

else:
    for i in readLastN():
        print(i)        
    