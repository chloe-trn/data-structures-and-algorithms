# Dynamic Connectivity algorithm implementation 1: Quick Find 

# id = array: this is the data structure used to support this quick find algorithm

# QuickFind class and object methods
class QuickFind: 
    def __init__(self, id):
        self.id = id  
    
    # method to initialize the ID array to size N and set each value of the ID array to its index 
    # N array accesses 
    def initArray(self, N):
        for i in range(0,N): 
            self.id.append(i)
        return self.id

    # method to check if p and q have the same id 
    # iff then p and q are CONNECTED 
    # this method uses Python IFELSE ternary operator 
    # this method USES 2 array accesses  
    def find(self,p,q):
        return True if self.id[p] == self.id[q] else False

    # method to connect p and q indexes - UNION operation 
    # To merge components containing p and q, change all entries whose id equals id[p] to id[q]
    # At most 2N + 2 array accesses
    def union(self,p,q):
        
        # 2 array accesses 
        p_id = self.id[p]
        q_id = self.id[q]

        # N array accesses
        for i in range(0, len(self.id)):
            if(self.id[i] == p_id):
                self.id[i] = self.id[q]

        return self.id 
        

qf1 = QuickFind([])
id = qf1.initArray(4)

find01 = qf1.find(0,1)
print("Are p=0 and q=1 connected: ", find01)

u31 = qf1.union(3,1)
print("Connect p=3 and q=1: ", u31)
u10 = qf1.union(1,0)
print("Connect p=1 and q=0: ", u10)

find01 = qf1.find(0,1)
print("Are p=0 and q=1 connected: ", find01)

# SUMMARY ****************************************************************************

# COST MODEL - num. of array accesses (for read or write)
# initArray - N --> N
# find - 2 --> 1
# union - 2N + 2  --> N
# Therefore the total cost is N*N*1 = N^2 --> QUADRATIC TIME 

# Conclusion: Union method is too expensive 

# Quadratic Algorithms are too expensive. They do not scale with larger sets of data 
