class QuickUnion: 
    def __init__(self, id):
        self.id = id
    
    # method to initialize array to support the quick union algorithm 
    def initArray(self, N):
        for i in range(0,N): 
            self.id.append(i)
        return self.id

    # method to find the root of a node and returns the index of the root 
    # chase a parent pointers until the root is reach 
    # helper method 
    def __root(self, i):
        while i != self.id[i]: 
            i = id[i]
        
        return i

    # check if p and q have the same root - TRUE/FALSE
    # iff p and q have the same root, they are connected
    # depth of p and q array accesses 
    def connected(self, p, q):
        proot = self.__root(p)
        qroot = self.__root(q)

        return True if proot == qroot else False

    # merge components containing p and q
    # set the id of p's root to the root of q 
    def union(self, p, q):
        pid = self.__root(p)
        qid = self.__root(q)
        
        self.id[pid] = qid


# TESTING 
qu1 = QuickUnion([])
qu1.initArray(10)
print(qu1.id)
qu1.union(4,3)
print(qu1.id)
qu1.union(3,8)
print(qu1.id)
qu1.connected(3,8)

# SUMMARY 

# COST MODEL - num. of array accesses (for read or write)
# initArray - N --> N
# find/connected - N --> N
# union - N  --> N  (includes cost of finding roots)
# Therefore the total cost is N*N*1 = N^2 --> QUADRATIC TIME 