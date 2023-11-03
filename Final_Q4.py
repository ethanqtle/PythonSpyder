# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 14:35:20 2023

@author: Ethan
"""
DEBUG = False
def primes_list(N):
    '''
    N: an integer
    '''
    # Your code here
    prime_list = []
    for i in range(2, N + 1):
        if DEBUG:
            print("i =", i)
        if i == 2:
            prime_list.append(i)
        else:
            found_factor = False
            for n in prime_list:
                if i % n == 0:
                    found_factor = True
                    break
                if n * n > i:
                    break
            if found_factor == False:
                prime_list.append(i)
                if DEBUG:
                    print('Found prime:', i)
               
    return prime_list
print(primes_list(100))