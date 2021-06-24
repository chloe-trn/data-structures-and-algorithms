#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.


# expected output 
# [26, 91]

def getMax(operations):
    
    stack = [] # stack to store elements defined by input operations
    
    for i in range(0, len(operations)):
        q = list(map(int, operations[i].split()))
        # push element x into stack 
        
        if q[0] == 1:
           #isolate number x from the operation string and push to stack
            x = q[1]
            if len(stack) == 0: 
                stack.append(x)
            else:
                stack.append(max(stack[-1], x))
        elif q[0] == 2:
            # pop from stack 
           stack.pop()
        else: 
           # get maximum value from stack and return it 
           print(stack[-1])


operations = [
'1 97', 
'2', 
'1 20', 
'2',
'1 26',
'1 20',
'2',
'3',
'1 91',
'3'
]

getMax(operations)

