new_list = [1,2,3]

if 1 in new_list: 
    print(True)

# linear search
for n in new_list: 
    if n == 1: 
        print(True)

        break 

'''
Array operations : 
'''

# Insert - O(n) - linear time, each element after the one inserted has to be moved to the suceeding index

numbers = []
print(len(numbers))
# Append - O(1) - constant time, element just has to be added at the end
numbers.append(2)
print(len(numbers))

# Extend - O(k) - add one list to another 
numbers.extend([4,5,6])
print(numbers)

# Delete - O(n) - shifts every element to the left, every element before has to be moved to the preceeding index

'''
Summary: 

We see that the built in array data structure has a couple of different operations 
Appending and Extending have constant time
Extending and Delete have linear time

We can build other data structures to improve upon these data structure operations efficiencies

'''

