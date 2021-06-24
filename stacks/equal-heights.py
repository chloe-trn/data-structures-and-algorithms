#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # reverse stacks so you can remove from the top 
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]

    # get sum of each stack 
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)
    print(sum1)

    # loop through and pop elements off of stacks until the stacks are the same height
    # return that height 
    
    while True: 

        minHeight = min(sum1,sum2,sum3)

        if minHeight == 0: 
            return minHeight
        
        if sum1 > minHeight: 
            sum1 -= h1.pop()
        
        if sum2 > minHeight: 
            sum2 -= h2.pop()

        if sum3 > minHeight: 
            sum3 -= h3.pop()

        if sum1 == sum2 == sum3: 
            return minHeight

        
            




'''
STDIN       Function
-----       --------
5 3 4       h1[] size n1 = 5, h2[] size n2 = 3, h3[] size n3 = 4  
3 2 1 1 1   h1 = [3, 2, 1, 1, 1]
4 3 2       h2 = [4, 3, 2]
1 1 4 1     h3 = [1, 1, 4, 1]
'''

h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]

print(equalStacks(h1, h2, h3))