# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 11:15:02 2023

@author: Ethan
"""

d = {1:10, 2:20, 3:30}
d = {4:True, 2:True, 0:True}
d = {1:10, 2:20, 3:30, 4:30}
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    If d = {1:10, 2:20, 3:30} then dict_invert(d) returns 
    {10: [1], 20: [2], 30: [3]}
    
    If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns 
    {10: [1], 20: [2], 30: [3, 4]}
    
    If d = {4:True, 2:True, 0:True} then dict_invert(d) returns 
    {True: [0, 2, 4]}
    '''
    # Your code here
    newD = {}
    for key in d:
        val = d[key]
        if val not in newD:
            newD[val] = [key]
        else:
            newD[val].append(key)
    for key in newD:
        newD[key] = sorted(newD[key])
    return newD

print(dict_invert(d))
        