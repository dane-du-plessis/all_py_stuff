def total(tree):
    if tree is None: return 0
    return total(tree.Left) + total(tree.Right) + tree.cargo

def print_tree(tree):
    if tree is None: return
    print(tree.cargo, end = ' ')
    print_tree(tree.Left)
    print_tree(tree.Right)

def print_tree_postorder(tree):
    if tree is None: return
    print_tree_postorder(tree.Left)
    print_tree_postorder(tree.Right)
    print(tree.cargo, end = ' ')

    
def print_tree_inorder(tree):
    if tree is None: return
    print_tree_inorder(tree.Left)
    print(tree.cargo, end = ' ')
    print_tree_inorder(tree.Right)
    
def print_tree_indented(tree, level = 0):
    if tree is None: return
    print_tree_indented(tree.Right, level+1)
    print("   "* level + str(tree.cargo))
    print_tree_indented(tree.Left, level+1)
