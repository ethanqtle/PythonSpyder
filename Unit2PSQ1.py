# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:10:31 2023

@author: Ethan
"""

balance = 42
unpaidBalance = 0
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = (annualInterestRate) / 12.0
minimumPayment = 0
interest = 0
i = 1

#Minimum payment = current balance * minimum monthly payment
#Unpaid balance = current balance - minimum payment
#Interest = (annual interest rate) / 12.0 (months per year) * unpaid balance
#Current balance = Unpaid Balance + Interest
while i <= 12:
    minimumPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimumPayment
    interest = monthlyInterestRate * unpaidBalance
    balance = unpaidBalance + interest
    i += 1

print("Remaining balance: ", round(balance, 2))