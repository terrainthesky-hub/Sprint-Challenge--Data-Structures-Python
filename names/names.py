import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None     

    def insert(self, value):
        # check if the value is less than the current node's value 
        if value < self.value:
            # does the current node have a left child?
            if self.left:
                self.left.insert(value)
            # otherwise, it doesn't have a left child
            # we can park the new node here 
            else:
                self.left = BSTNode(value)
        # otherwise the value is greater or equal to the current node's value 
        else:
            # does the current node have a right child?
            if self.right:
                # if it does, call the right child's `insert` method to repeat the process
                self.right.insert(value)
            # otherwise, it doesn't have a right child 
            # we can park the new node here 
            else:
                self.right = BSTNode(value)

    def dupes(self): 
        seen = []

        
        if self.left:
            self.left.dupes()
        if self.right:
            self.right.dupes()
        seen.append(self.value)
        if self.value in seen:
            duplicates.append(self.value)
        # global previous 
    
        # # If root is null then return 
        # if self is None: 
        #     return
    
        # dupes(self.left) 
    
        # if previous is not None: 
    
            
        #     if self.value == previous.value: 
        #         duplicates.append(self.value)
    
   
        # previous = self 
        # dupes(self.right) 





start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

#This is O(n^2)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

bst = BSTNode(names_1[0])

for x in names_1:
    bst.insert(x)
for x in names_2:
    bst.insert(x)
bst.dupes()


#This is O(n^2log)

# for x in names_1:
#     if x in names_2:
#         duplicates.append(x)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
