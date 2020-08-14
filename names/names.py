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
        self.children = {'a':None, 'b':None, 'c':None, 'd':None,
                         'e':None, 'f':None, 'g':None, 'h':None,
                         'i':None, 'j':None, 'k':None, 'l':None,
                         'm':None, 'n':None, 'o':None, 'p':None,
                         'q':None, 'r':None, 's':None, 't':None,
                         'u':None, 'v':None, 'w':None, 'x':None,
                         'y':None, 'z':None, ' ':None} #this would have been easier if base_dict were not mysteriously changing
        
        # names_1 contains 'Alyvia Stevenson', causing the names_2 entry 'Alyvia Stevens' to
        # come back as a duplicate but it isn't. This is a stopgap measure for other 
        # situations like this
        self.is_end_for_short_name = False
    
    def insert(self, name, idx):
        # Call from top_node with the desired name to fill and starting index of 0
        if idx == len(name):
            if [*self.children.values()] != [None]*27:
                # This catches the case of a long name leaving a confusing trail for a shorter name that is up to this point identical
                self.is_end_for_short_name = True
            
            #Reached the end of the name, exit recursion with this
            return True 
        
        # review statement for debugging
        # if idx > 0 and name[idx-1].lower() != self.letter:
        #     return False

        next_letter = name.lower()[idx]
        if not self.children[next_letter]:
            self.children[next_letter] = AlphaTreeNode(next_letter)
        return self.children[next_letter].insert(name, idx+1)
    
    def search(self, name, idx):
        if idx == len(name):
            if [*self.children.values()] == [None]*27:
                # The tree has a path to the end of this name and no further
                return True
            elif [*self.children.values()] != [None]*27 and self.is_end_for_short_name:
                # Even though this is the name's end, the tree continues beyond this point
                # Fortunately, this short name came up in the tree's creation and has been flagged as True
                return True
            else:
                # self.is_end_for_short_name has not been flagged and this is just the rare shortened version of a name that does exist in the tree's creation, but the short version was not
                return False
        
        # review statement for debugging
        # if idx > 0 and name[idx-1].lower() != self.letter:
        #     return False
        
        next_letter = name[idx].lower()
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
###### ^ the above code operates with complexity of O(n^2)

#Make the tree from the top
top_node = AlphaTreeNode(None)
names_idx = 0
for name in names_1:
    if not top_node.insert(name, 0):
        break
    names_idx += 1
print(names_idx,'out of',len(names_1),'names filled')

#Search for the names in names_2
for name in names_2:
    if top_node.search(name,0):
        duplicates.append(name)

### ^ the fixed code operates with complexity of O(log n)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.