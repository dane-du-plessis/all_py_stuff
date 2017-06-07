# Tree
from TraverseTree import *

class Tree:
    def __init__(self, cargo = None, Left = None, Right = None):
        self.cargo = cargo
        self.Left = Left
        self.Right = Right

    def __str__(self):
        return str(self.cargo)


tree = Tree(1, Tree(2), Tree(3))


tree2 = Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))

print('')
print('')
print('')
print('sum of tree 1')
print(total(tree))

print('')
print('')
print('')
print('sum of tree 2')
print_tree(tree2)

print('')
print('')
print('')
print('Indented tree:')
print_tree_indented(tree2)
