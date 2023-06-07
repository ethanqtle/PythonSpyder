# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 17:08:27 2023

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
# s = 'abcdefghijklmnopqrstuvwxyz'

#P# Keep track of the longest substring found so far
longest = s[0]
current = s[0]

#P# Iterate over the string, skipping the first character
for i in range(1, len(s)):
    # If the current character is greater than or equal to the last character
    # in the longest string, then add the current character to the current string
    if s[i] >= current[-1]:
        current += s[i]
    #P# Otherwise, start a new current string with the current character
    else:
        current = s[i]
    # If the current string is longer than the longest string, then update 
    # the longest string
    if len(current) > len(longest):
        longest = current

print("Longest substring in alphabetical order is: " + longest)
