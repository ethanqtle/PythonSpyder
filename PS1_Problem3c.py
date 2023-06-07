# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:19:50 2023

@author: Ethan
"""
s = 'abcdefghijklmnopqrstuvwxyz'

current = s[0]
best = s[0]

for i in range(1, len(s)):
    if s[i-1] <=  s[i]:
        current += s[i]
        if len(current) > len(best):
            best = current
    else:
        current = s[i]
print('Longest substring in alphabetical order is:', best)