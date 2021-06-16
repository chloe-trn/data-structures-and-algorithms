""" 
linear search algorithm function
takes in the list to search in and the target value
returns the index of the target value in the list if found
returns false if target value is not found
"""
def linear_search(list,target):
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None

print(linear_search([2,1,5,3], 7))