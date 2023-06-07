# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:00:55 2023

@author: Ethan
"""

s = 'obfitd'
numVowels = 0
# numCons = 0

for char in s:
    if char in "aeiou":
        numVowels += 1;

print('Number of vowels: ' + str(numVowels));