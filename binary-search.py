import math

def binary_search(list,target):
    first = 0
    last = len(list) - 1
    
    # check the size of the array 
    while first <= last: 
        # find the halfway value - // is floor division 
        half_value = (first + last) // 2 

        # target found
        if list[half_value] == target: 
            return half_value

        #target is greater than midpoint - discard values lower than midpoint index
        elif list[half_value] < target: 
            first = half_value + 1
        else: 
            last = half_value - 1
    
    return None

# THE LIST NEEDS TO BE SORTED
print(binary_search([1,0,2,9,5,6,7,8,9,10], 1))

print(binary_search([0,1,2,3,4,5,6,7,8,9,10], 1))

def recursive_binary_search(list, target):
    if len(list) == 0: 
        return False
    else: 
        midpoint = (len(list))//2
        if list[midpoint] == target: 
            return midpoint 
        else: 
            if list[midpoint] < target: 
                return recursive_binary_search(list[midpoint + 1:], target)
            else: 
                return recursive_binary_search(list[:midpoint], target)