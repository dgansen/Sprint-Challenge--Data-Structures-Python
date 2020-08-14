import time
letters = 'abcdefghijklmnopqrstuvwxyz '
base_dict = {}
for let in letters:
    base_dict[let] = None

class AlphaTreeNode:
    def __init__(self, letter):
        # The node's letter is what got a name to reach this point in traversal
        self.letter = letter
        # Dictionary of the node's children
        # They only exist if the tree creation had a name at one point that followed this order of letters
        self.children = base_dict
    
    def insert(self, name, idx):
        if idx == len(name):
            #Reached the end of the name, exit recursion with this
            return True

        next_letter = name.lower()[idx]
        if not self.children[next_letter]:
            self.children[next_letter] = AlphaTreeNode(next_letter)
        return self.children[next_letter].insert(name, idx+1)
    
    def search(self, name, idx):
        if idx == len(name):
            #Reached the end of the name, return True and exit recursion
            #All letters in this name are accounted for in proper order
            return True
        next_letter = name.lower()[idx]
        if self.children[next_letter]:
            #The tree has a connecting node for the next letter in the name
            return self.children[next_letter].search(name,idx+1)
        else:
            #The tree does not have a node established for the name's next letter
            return False
        
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#Make the tree from the top
top_node = AlphaTreeNode(None)
names_idx = 0
for name in names_1[0:3]:
    if not top_node.insert(name, 0):
        break
    names_idx += 1
print(names_idx,'out of',len(names_1),'names filled')

#Search for the names in names_2
for name in names_2:
    if top_node.search(name,0):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
