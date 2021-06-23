'''
Delete the node at a given position in a linked list and return a reference to the head node. 
The head is at position 0. 
The list may be empty after you delete the node.
 In that case, return a null value.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'deleteNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(llist, position):
    # case: linked list is empty 
    head = llist.head 
    if llist.head == None: 
        head = None 
    else: 
        # create variables to traverse the list 
        temp = llist.head 
        prev_node = None 
        count = 0

        # traverse the list until you get to the node at the given position 
        while temp != None and count < position: 
            prev_node = temp 
            temp = temp.next 
            count += 1
        
        prev_node.next = temp.next 

    return head




