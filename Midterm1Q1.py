# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 10:43:48 2023

@author: Ethan
"""

def isMyNumber(guess):
    secretNumber = -50
    if guess < secretNumber:
        return -1
    elif guess > secretNumber:
        return 1
    else:
        return 0
    
def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    min = -100
    max = 100
    if isMyNumber(guess) == 0:
        return guess
    foundNumber = False
    while not foundNumber:
        sign = isMyNumber(guess)
        if sign == -1:
            min = guess
            guess = (min + max)//2
        elif sign == 1:
            max = guess
            guess = (min + max)/2
        elif sign == 0:
            break
    return guess

print(jumpAndBackpedal(isMyNumber))
