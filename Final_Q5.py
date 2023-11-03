# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 15:24:47 2023

@author: Ethan
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    # Your code here
    # cipher("abcd", "dcba", "dab") returns ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
    key_code = {}
    decode = ''
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
    for letter in code:
        decode += key_code[letter]
    return (key_code, decode)
print(cipher("abcd", "dcba", "dab"))