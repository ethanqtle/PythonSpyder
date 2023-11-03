# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:59:45 2023

@author: Ethan
"""

def display_em(lower, upper):
    """ This recursive function displays the consecutive integers from its lower to its upper bounds """
    if lower > upper:
        return
    print(lower)
    display_em(lower + 1, upper)

def add_em(lower, upper):
    """ This recursive function calculates the sum of the consecutive integers from its lower to its upper bounds"""
    if lower > upper:
        return 0
    return lower + add_em(lower + 1, upper)
        
def applyToEach(f, lower, upper):
    """ This higher-order function applies the included function to it lower and upper bound aruments"""
    return f(lower, upper)

lower = int(input('Enter a lower bound: '))
upper = int(input('Enter a upper bound: '))
print('The consecutive integers:')
applyToEach(display_em, lower, upper)
print('Add up to', applyToEach(add_em, lower, upper))