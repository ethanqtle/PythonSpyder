# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:10:26 2023

@author: Ethan
"""

#Practice for Section 2.2
pair = [10, 20]
x, y = pair
print("x =", x)
print("y =", y)
print("pair[0] =", pair[0])
print("pair[1] =", pair[1])

from operator import getitem
print("getitem(pair, 0) =", getitem(pair, 0))
print("getitem(pair, 1) =", getitem(pair, 1))

#Represent Rational Numbers
def rational(n, d):
    return [n, d]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def print_rational(x):
    # print(numer(x), "/", denom(x))
    print(f"{numer(x)}/{denom(x)}")
    
def add_rationals(x, y):
    nx, dy = numer(x), denom(y)
    dx, ny = denom(x), numer(y)
    return rational((nx * dy + ny * dx), (dx * dy))

def mul_rationals(x, y):
    nx, dy = numer(x), denom(y)
    dx, ny = denom(x), numer(y)
    return rational(nx * ny, dx * dy)
    
half = rational(1, 2)
print_rational(half)
thirds = rational(1, 3)
result = add_rationals(half, thirds)
product = mul_rationals(half, thirds)
print_rational(result)
print_rational(product)
print("Another way of printing the result: ")
print_rational(add_rationals(half, thirds))
print("Another way of printing the product: ")
print_rational(mul_rationals(half, thirds))

from math import gcd
def rational(n, d):
    g = gcd(n, d)
    #The return is a list [], NOT a set (), for the sake of consistency with
    #the function
    return [n//g, d//g]

print_rational(add_rationals(thirds, thirds))

def square_rational(x):
    return mul_rationals(x, x)

#Violation: Use of rational function assuming it will multiply the values
#automatically
def square_rational_violating_once(x):
    return rational(numer(x) * numer(x), denom(x) * denom(x))

#On top of the previous violation, this function uses list indexes instead of
#the selector or getter
def square_rational_violating_twice(x):
    return rational(x[0] * x[0], x[1] * x[1])

def pair(x, y):
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
    return get

def select(p, i):
    #Returns the element at index i of pair p
    return p(i)

p = pair(20, 14)
print("select(p, 0) =", select(p, 0))
print("select(p, 1) =", select(p, 1))
p1 = pair(30, 24)
print("select(p1, 0) =", select(p1, 0))
print("select(p1, 1) =", select(p1, 1))