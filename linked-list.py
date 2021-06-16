'''

Singly Linked List: 
- Elements in list are called nodes, contain the element and a pointer 
- First node = head 
- Last node = tail 
- Every node in the list only points to the next node in the list 
- Tail node does not point to anything

Doubly Linked List: 
- Each node points to the node before and the node after itself 

'''

# Single linked list 
class Node: 
    ''' 
    An object for storing a single node of a linked list. 
    Models the data and the link to the next node in the list
    '''
    data = None # holds onto data we are storing 
    next_node = None # holds the next node info 

    # constructor 
    def __init__(self, data):
        self.data = data 
    
    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList: 
    """
    Singly linked list 
    """
    def __init__(self):
        self.head = None 

    # if the head is empty, then the linked list is empty
    def is_empty(self):    
        return self.head == None 

    def size(self):
        """
        Returns the number of nodes in the list.  
        Takes linear time O(n)
        """
        current = self.head 
        count = 0

        while current != None: 
            count += 1
            current = current.next_node 
        
        return count 

    def add(self, data):
        """
        Takes in data and adds it as a new node at the head of the linked list 
        takes O(1) time 
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        '''
        Search for the first node containing data that matches the key
        Returns the node or 'None' if not found
        Runs in linear time O(n)
        '''
        current = self.head
        while current != None: 
            if current.data == key: 
                return current 
            else: 
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position 
        Insertion takes O(1) time but seraching for the insertion point 
        takes O(n)

        Overall O(n)
        """
        if index == 0: 
            self.add(data)

        if index > 0: 
            new = Node(data)
            position = index
            current = self.head 
            
            # This position > 1 allows us to be accurate near the beginning of the linked list 
            while position > 1: 
                current = current.next_node 
                position -= 1 
            
            prev_node = current 
            next_node = current.next_node 
            
            prev_node.next_node = new 
            new.next_node = next_node 
            
    def remove(self, key):
        """
        Removes node containing data that matches key 
        Return the node or None if the key does not exist 
        """
        current = self.head 
        previous = None 
        found = False 

        while current and not found: 
            if current.data == key and current is self.head: 
                found = True 
                self.head = current.next_node
            elif current.data == key: 
                found = True 
                previous.next_node = current.next_node
            else: 
                previous = current 
                current = current.next_node
        
        return current


    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current != None:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return  '-> '.join(nodes)

 
# create linked list 
l = LinkedList()

# create node and make it the head of the linked list 
n1 = Node(10)
l.head = n1
print(l)

# add a new node 
l.add(2)
print(l)
l.add(6)
print(l)

# search for node values  
print(l.search(2))
print(l.search(12))



'''
Summary: 

Linked lists: 

- Inserting and deleting operations takes constant time O(1) rather than linear time with an Array 
- This is because you only have to change the references of the elements before and after the node deleted
and do not have to shift the entire array to the right 


- However, to insert or delete. 
- you first must search through the linked list to find the element you want to add or delete
- Our search method is linear time O(n)

'''