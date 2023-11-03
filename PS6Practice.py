# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:09:47 2023

@author: Ethan
"""

def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
numbers = [1, 5, 3, 7, 6, 2, 8, 10]
modSwapSort(numbers)
