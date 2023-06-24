# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:23:27 2023

@author: Ethan
"""
def calculateBalance (balance, annualInterestRate, minPayment):
    monthlyInterestRate = (annualInterestRate) / 12.0
    for i in range(12):
        monthlyUnpaidBalance = balance - minPayment
        balance = (monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance))
    return balance

def calculatePayment (balance, annualInterestRate):
    monthlyInterestRate = (annualInterestRate) / 12.0
    MPlowerBound = balance / 12
    MPupperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0   
    while True:
        minPayment = (MPlowerBound + MPupperBound) / 2
        newBalance = calculateBalance(balance, annualInterestRate, minPayment)
        if round(MPlowerBound, 2) == round(MPupperBound, 2):
            return minPayment
        elif newBalance > 0:
            MPlowerBound = minPayment
        elif newBalance < 0:
            MPupperBound = minPayment
        
        

#Case 1
balance = 320000
annualInterestRate = 0.2
result = balance

#Case 2
balance = 999999
annualInterestRate = 0.18

result = calculatePayment(balance, annualInterestRate)
print("Lowest Payment:", round(result, 2))