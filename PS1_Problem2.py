# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 15:42:43 2023

@author: Ethan
"""
s = 'bobobvyobobobooboobobobmbebonbobbl'

bob = 'bob';
numBob = 0;
for i in range (len(s)):
    #print('i = ',i, s[i : i + 3])
    if s[i : i + 3] == 'bob':
        numBob += 1
print('Number of times bob occurs is: ' + str(numBob));
