# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 19:43:43 2023

@author: Ethan
"""

import math


def subtotal(a, b):
    return a * b


def discount(quantity, item_price):
    drop = 0
    if quantity < 10:
        drop = 0
    elif quantity < 20:
        drop = 10
    elif quantity < 50:
        drop = 20
    elif quantity < 100:
        drop = 25
    else:
        drop = 30
    result = item_price * quantity * drop/100.0
    return result


item_price = float(input('What is the price of each item? '))
quantity = float(input('How many are you ordering? '))
print('Subtotal: $ {0:.2f}'.format(subtotal(item_price, quantity)))
print('Discount: $ {0:.2f}'.format(discount(quantity, item_price)))
final_price = subtotal(item_price, quantity) - discount(quantity, item_price)
print('Total: $ {0:.2f}'.format(final_price))
