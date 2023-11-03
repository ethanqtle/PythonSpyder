# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 11:03:47 2023

@author: Ethan
"""
listA = [1, 3, 5]
listB = [2, 4, 6]
def dotProduct(listA, listB):
    i = 0
    result = 0
    # while i < len(listA):
    #     result += listA[i] * listB[i]
    #     i += 1
    for i in range(len(listA)):
        result += listA[i] * listB[i]
    return result


print(dotProduct(listA, listB))