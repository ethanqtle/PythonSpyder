# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 12:33:33 2023

@author: Ethan
"""

def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)

print(a(False, 2, 3))
print(b(3, 2))
print(a(3>2, a, b))
print(b(a, b))
