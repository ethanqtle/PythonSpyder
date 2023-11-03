# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:18:51 2023

@author: Ethan
"""
import random
currentNumber = 0
user_input = "Y"
def isEven(currentNumber):
    if currentNumber % 2 == 0:
        return True
    else:
        return False

while user_input.upper() == "Y":
    evenCount = 0
    for i in range(0, 100):
        currentNumber = random.randint(1, 1000)
        if isEven(currentNumber):
            evenCount += 1
    oddCount = 100 - evenCount
    print("Out of 100 random numbers,", oddCount, "were odd, and", evenCount, "were even.")
    user_input = input("Would you like to run the program again? (Y/N): ")
