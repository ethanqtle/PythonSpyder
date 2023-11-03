# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 11:36:28 2023

@author: Ethan
"""
import math

def reciprocal(number):
    recip = 1.0/number
    return recip

def mean(a, b, c):
    return (a + b + c)/3.0

def geometric_mean(a, b, c):
    return (a * b * c)**(1.0/3.0)

def harmonic_mean(a, b, c):
    return 3.0/(reciprocal(a) + reciprocal(b) + reciprocal(c))

def main():
    print("Reciprocal of 8 is", reciprocal(8), "[should be 0.125]")
    print("Reciprocal of 4/3 is", reciprocal(4/3), "[should be 0.75]")
    print("Reciprocal of -3 is", reciprocal(-3), "[should be -0.3333...]")

    print("Mean of 1, 13, 4 is", mean(1, 13, 4), "[should be 6.0]")
    print("Mean of -5, -12, -9 is", mean(-5, -12, -9), "[should be -8.666...]")

    print("Geometric mean of 144, 2, 6 is", geometric_mean(144, 2, 6), \
        "[should be 11.9999..]")
    print("Geometric mean of 2.1, 16.8, 16.8 is", geometric_mean(2.1, 16.8, 16.8), \
        "[should be 8.3.999...]")
  
    print("Harmonic mean of 1, 2, 3 is", harmonic_mean(1, 2, 3), \
        "[should be 1.636363...]")
    print("Harmonic mean of -2, 1, 1 is", harmonic_mean(-2, 1, 1), \
        "[should be 2.0]")

main()
