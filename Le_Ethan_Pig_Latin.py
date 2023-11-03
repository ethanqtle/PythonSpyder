# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:10:04 2023

@author: Ethan
"""
def pig_latin(word):
    word_PL = word.lower()
    if word_PL[0] in "aeiouy":
        word_PL += "way"
    else:
        word_PL = word_PL[1:] + word_PL[0] + "ay"
    return word_PL

sentence = input('Please input a sentence to be converted to Pig Latin: ')
sentence_PL = []
for word in sentence.split():
    word_lc = pig_latin(word)
    sentence_PL.append(word_lc)
print(" ".join(sentence_PL))
        