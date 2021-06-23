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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(head, data):
    # head = pointer to head of the linked list 

    # create a new node 
    node = SinglyLinkedListNode(data)

    # check if the linked list is empty 
    if head == None: 
        head = node 
    else: 
        # linked list is not empty 
        node.next = head  # set the next pointer of the new node to the current head of the list 
        head = node  # make the head node the new node 

    return head # return the head node 


