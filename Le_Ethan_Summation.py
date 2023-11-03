# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 09:33:49 2023

@author: Ethan
"""
import math
print('User Input:')
user_LB = int(input(('Enter a lower bound for the sum: ')))
user_UB = int(input(('Enter an upper bound for the sum: ')))

def summation(f, user_LB, user_UB):
    total = 0
    for k in range(user_LB, user_UB + 1):
        total += f(k)
    return total

def sq(x):
    return x * x

def fourth_power(x):
    return sq(sq(x))

print('Program Output:')
print('The sum of squares of the numbers from', user_LB, 'to', user_UB, 'is', summation(sq, user_LB, user_UB))
print('The sum of fourth powers of the numbers from', user_LB, 'to', user_UB, 'is', summation(fourth_power, user_LB, user_UB))

sum_lambda = summation(lambda x : math.sqrt(x), user_LB, user_UB)
print('The sum of square roots of the numbers from', user_LB, 'to', user_UB, 'is', sum_lambda)