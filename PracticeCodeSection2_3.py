# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:10:24 2023

@author: Ethan
"""

#Practice Code for Section 2.3
print("Section 2.3.1")

digits = [1, 8, 2, 8]
print("digits =", digits)
print("len(digits) =", len(digits))
print("digits[3] =", digits[3])

new = [2, 7] + digits * 2
print("[2, 7] + digits * 2", new)
pairs = [[10, 20], [30, 40]]
print("pairs[1] =", pairs[1])
print("pairs[1][0] =", pairs[1][0])

print("\nSection 2.3.2")

#Counts how many indexes of a sequence match the value asked
def count(s, value):
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total

print("count(digits, 8) =", count(digits, 8))

#Example of for loop
same_count = 0
pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
for x, y in pairs:
    if x == y:
        same_count = same_count + 1

print("same_count =", same_count)

#Range examples
print(list(range(5, 8)))
print(list(range(4)))

print("\nSection 2.3.3")

#List Comprehensions
odds = [1, 3, 5, 7, 9]
print([x for x in odds if 25 % x == 0])
#General form: [<map expression> for <name> in <sequence expression> if <filter
# expression>]

#Returns the divisors of number n
def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

print(divisors(4))
print(divisors(12))
print([n for n in range(1, 1000) if sum(divisors(n)) == n])

def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)

area = 80
print("width(area, 5) =", width(area, 5))

print("perimeter(16, 5) =", perimeter(16, 5))
print("perimeter(10, 8) =", perimeter(10, 8))
print("minimum_perimeter(area) =", minimum_perimeter(area))
print("[minimum_perimeter(n) for n in range(1, 10)] =", [minimum_perimeter(n) for n in range(1, 10)])

#Higher-order functions
def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced
from operator import mul
print("reduce(mul, [2, 4, 8], 1) =", reduce(mul, [2, 4, 8], 1))

def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))
print("divisors_of(12) =", divisors_of(12))

from operator import add
def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)

def perfect(n):
    return sum_of_divisors(n) == n

print("keep_if(perfect, range(1, 1000)) =", keep_if(perfect, range(1, 1000)))
apply_to_all2 = lambda map_fn, s: list(map(map_fn, s))
keep_if2 = lambda filter_fn, s: list(filter(filter_fn, s))

from functools import reduce
from operator import mul
def product(s):
    return reduce(mul, s)
print("product([1, 2, 3, 4, 5]) =", product([1, 2, 3, 4, 5]))

print("\nSection 2.3.4:")
print("digits =", digits)
print("2 in digits =", 2 in digits)
print("1828 not in digits =", 1828 not in digits)

print("digits[0:2] =", digits[0:2])
print("digits[1:] =", digits[1:])