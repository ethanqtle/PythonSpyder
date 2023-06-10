# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 22:32:03 2023

@author: Ethan
"""

numGuesses = 0.0
low = 0
high = 100
ans = (high + low) // 2
result = 0.0

print("Please think of a number between 0 and 100!")
while high > low:
    ans = (high + low) // 2
    print("Is your secret number " + str(ans) + "?")
    userInput = input("Enter 'l' if it is too low, 'h' if the guess is too high, or 'c' if it is correct. ")
    print(userInput)
    if userInput == "l":
        low = ans
    elif userInput == "h":
        high = ans
    elif userInput == "c":
        result = ans
        break
    else:
        print("Your input was invalid. Please try again.")
print("Game over. Your secret number is", str(result))