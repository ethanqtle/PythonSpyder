# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:46:04 2023

@author: Ethan
"""
user_answers = []
incorrect_answers = []

# This will ask the user to provide their answers for each of the 20 questions
for i in range(20):
    user_input = input("Please enter your answer for question " + str(i + 1) + ": ").upper()
    user_answers.append(user_input)
    i += 1

correct_answers = ['D', 'B', 'A', 'C', 'A', 'C', 'B', 'D', 'C', 'A', 'D', 'B', 'C', 'D', 'C', 'A', 'B', 'D', 'C', 'C']
correct = 0
incorrect = 0

# Compares the user's answers to the correct answers and keeps track of what's 
# correct and incorrect
for i in range(0, len(correct_answers)):
    if user_answers[i] == correct_answers[i]:
        correct += 1
    else:
        incorrect += 1
        incorrect_answers.append(str(i + 1))
print('Number of correct answers:', correct)
print('Number of incorrect answers:', incorrect)
# Determines whether the user passed the test or not
if correct >= 15:
    print('You passed the test.')
else:
    print('You did not pass the test.')
print('Questions answered incorrectly:', ", ".join(incorrect_answers))
    