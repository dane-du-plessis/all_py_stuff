class Tree:
    def __init__(self, cargo = None, Left = None, Right = None):
        self.cargo = cargo
        self.Left = Left
        self.Right = Right

    def __str__(self):
        return str(self.cargo)
# ++++++++++++++++++++++++++++++++
def get_token(token_list,expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False

def get_number(token_list):
    if get_token(token_list, '('):
        x = get_sum(token_list)
        if not get_token(token_list,')'):
            raise ValueError('Missing close Apples')
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        del token_list[0]
        return Tree(x, None, None) #have a leaf

def get_product_simple(token_list):
    a = get_number(token_list)
    if get_token(token_list,'*'):
        b = get_number(token_list)
        return Tree('*', a, b)
    return a

def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list,'*'):
        b = get_product(token_list)
        return Tree('*', a, b)
    return a

def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list,'+'):
        b = get_sum(token_list)
        return Tree('+',a,b)
    return a

# ++++++++++++++++++++++++++++++++
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
# ++++++++++++++++++++++++++++++++



token_list = [2, "*", 3, "*", 5 , "*", 7, "end"]
tree = get_product(token_list)
print_tree_postorder(tree)

token_list = [9, "*", 11, "+", 5, "*", 7, "end"]
tree = get_sum(token_list)
print_tree_postorder(tree)


token_list = [9, "*", "(", 11, "+", 5, "(", "*", 7, "end"]
tree = get_sum(token_list)
print_tree_postorder(tree)

