# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:13:33 2023

@author: Ethan
"""

class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def count_leaves(self):
        if self.is_leaf():
            return 1
        else:
            return sum(branch.count_leaves() for branch in self.branches)

def print_tree(tree, indent=0):
    print('  ' * indent + str(tree.label))
    for branch in tree.branches:
        print_tree(branch, indent + 1)

# Construct the tree
subtree1 = Tree('C')
subtree2 = Tree('D')
subtree3 = Tree('E')
subtree4 = Tree('F')
subtree5 = Tree('G')
subtree6 = Tree('H')
subtree7 = Tree('I')
subtree8 = Tree('J')
tree = Tree('A', [
    Tree('B', [subtree1, subtree2]),
    Tree('K', [subtree3, subtree4]),
    subtree5,
    subtree6,
    Tree('L', [subtree7, subtree8])
])

# Print the nested tree
print("Nested Tree:")
print_tree(tree)

# Print label and branches
print("\nLabel:", tree.label)
print("Branches:", [branch.label for branch in tree.branches])

# Count the number of leaves
num_leaves = tree.count_leaves()
print("\nNumber of Leaves:", num_leaves)
