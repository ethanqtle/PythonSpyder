# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 14:12:52 2023

@author: Ethan
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    n = 0
    number = n * (n + 1)/2
    while k != number:
        number = n * (n + 1)/2
        if number == k:
            return True
        elif number < k:
            n += 1
        elif number > k:
            return False

import math
def is_triangular_f(k):
    nVal = (math.sqrt(8*k+1)-1)/2
    return math.floor(nVal) == nVal
     
# print(is_triangular(1))

upperTest = 10
for i in range(1,upperTest + 1):
    k = sum(range(i+1))
    print("i ==", i, "k", k, "is_triangular ", is_triangular(k),  "is_triangular_f ", is_triangular_f(k))

            