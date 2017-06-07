class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo=cargo
        self.next= None

    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next is not None:
            self.next.print_backward()
        print(self, end=" ")

def print_list(node):
    print('[', end=' ')
    while node is not None:
        print(node, end = " ")
        node = node.next
    print(']')
