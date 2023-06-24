# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:45:02 2023

@author: Ethan
"""
def calculateBalance (balance, annualInterestRate, minimumFixedMonthlyPayment):
    monthlyInterestRate = (annualInterestRate) / 12.0
    for i in range(12):
        monthlyUnpaidBalance = balance - minimumFixedMonthlyPayment
        balance = (monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance))
    return balance

balance = 4773
annualInterestRate = 0.2
minimumFixedMonthlyPayment = 10
result = balance

while True:
    result = calculateBalance(balance, annualInterestRate, minimumFixedMonthlyPayment)
    if result <= 0:
        break
    else:
        minimumFixedMonthlyPayment += 10

print("Lowest Payment:", minimumFixedMonthlyPayment)