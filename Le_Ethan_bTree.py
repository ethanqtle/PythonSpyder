# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 22:15:19 2023

@author: Ethan
"""
class Tree:
    def __init__(self, label, branches = []):
        self.label = label
        self.branches = branches
        
    def is_leaf(self):
        return len(self.branches) == 0
    
    def count_leaves(self):
        if self.is_leaf():
            return 1
        else:
            num_leaves = 0
            for branch in self.branches:
                num_leaves += branch.count_leaves()
            return num_leaves
    
    def get_leaves(self):
        if self.is_leaf():
            return [self.label]
    
    def print_tree(self, indent = 0):
        print('  ' * indent + str(self.label))
        for b in self.branches:
            b.print_tree(indent + 1)
    
    def print_branches(self):
        branch_list = []
        for branch in self.branches:
            branch_list.append(branch.label)
        print("Branches:", str(branch_list))
            
    


bTree = Tree(4, [Tree(2, [Tree(1), Tree(3)]), Tree(6, [Tree(5)])])
bTree.print_tree()
print("Label:", bTree.label)
bTree.print_branches()
print("Number of leaves:", bTree.count_leaves())
