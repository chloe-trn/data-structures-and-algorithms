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
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(head, data, position):
    # create new Node 
    node =  SinglyLinkedListNode(data)

    # case: list is empty 
    if head == None: 
        head = node
    else:   
        # case: list is not empty 
        # make a copy of the head node to traverse the linked list
        temp = head 
        count = 1
        # case: list is not empty 
        # traverse the linked list up until the node before where we want the new node to be inserted 
        while temp != None and count < position: 
            temp = temp.next 
            count += 1
        
        # reassign pointers so that new node is inserted in the given position 
        node.next = temp.next  
        temp.next = node

    return head 
