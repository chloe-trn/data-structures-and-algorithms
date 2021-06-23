#!/bin/python3
# Insert a node at the head of a linked list - HackerRank Practice Problem
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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    # create new Node with data 
    node = SinglyLinkedListNode(data)
    # if linked list is empty, then the new node is becomes the head 
    if head == None:
        head = node 
    else: 
        # the linked list is not empty 
        # traverse through linked list until node.next is null, this is the last node in the linked list 
        temp = head  # make a copy of the head. this is essentially a pointer we will use to traverse the linked list
        while temp.next:
            temp = temp.next

        temp.next = node # set the node that has None as it's next node to have the next node of the new Node 
    
    return head  # return the head of the linked list 
