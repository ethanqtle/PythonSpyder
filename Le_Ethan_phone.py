# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 20:29:35 2023

@author: Ethan
"""

import math
negative = False
plan1_cost = 9.38
plan2_cost = 8.57
plan1_over = 0.045
plan2_over = 0.052
plan1_units = 65
plan2_units = 50
def get_units():
    num_units = float(input('Enter number of units used: '))
    if num_units < 0:
        print('You cannot have negative units.')
    return num_units

def calculate_cost(num_units, plan_cost, plan_units, over):
    result = 0
    if num_units <= plan_units:
        result = plan_cost
    else:
        result = plan_cost + (num_units - plan_units) * over
    return result

num_units = get_units()
plan1_price = calculate_cost(num_units, plan1_cost, plan1_units, plan1_over)
plan2_price = calculate_cost(num_units, plan2_cost, plan2_units, plan2_over)
if num_units > 0:
    print('Cost for plan 1: $ {0:.2f}'.format(plan1_price))
    print('Cost for plan 2: $ {0:.2f}'.format(plan2_price))
    if plan2_price > plan1_price:
        print('Plan 1 is cheaper.')
    else:
        print('Plan 2 is cheaper.')
