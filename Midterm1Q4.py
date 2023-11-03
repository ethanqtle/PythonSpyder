# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 11:27:59 2023

@author: Ethan
"""
aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def flatten(aList):
    newList= []
    for element in aList:
        if type(element) != list:
            newList.append(element)
        else:
            newList.extend(flatten(element))
    return newList

print(flatten(aList))