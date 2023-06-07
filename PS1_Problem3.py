# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:07:34 2023

@author: Ethan
"""

s = 'azcbobobegghakl'
#    az
#      c
#       bo
#         bo
#           beggh
#                akl
s = 'abcbcd'
s = 'abcdefghijklmnopqrstuvwxyz'

left, right, length = 0, 0, 0
bestLeft, bestRight, bestLength = 0, 0, 0
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        right = i
    else:
        right = i
        length = right - left + 1
        if length > bestLength:
            bestLength = length
            bestLeft = left
            bestRight = right        
        left = i + 1

length = right - left + 1
if length > bestLength:
    bestLength = length
    bestLeft = left
    bestRight = right

# print('Best Length, Best Left, Best Right:', bestLength, bestLeft, bestRight)
print('Longest substring in alphabetical order is:', s[bestLeft:bestRight + 1])