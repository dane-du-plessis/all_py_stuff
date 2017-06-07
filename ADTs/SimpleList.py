'''
This is an exercise in writing linked lists
'''

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

def print_list(node):
    while node is not None:
        print(node, end = " ")
        node = node.next
    print()

def print_backward(list):
    if list is None: return
    head = list
    tail = list.next
    print_backward(tail)
    print(head, end=" ")

n1 = Node('a')
n2 = Node('b')
n3 = Node('c')

n1.next = n2
n2.next = n3
n3.next = None #redundant

print_list(n1)
print_backward(n1)
