'''
Nicer linked list class
'''

class LinkedList:
    def __init__(self, head=None, length=0):
        self.length = length # if length == 0 then list is empty
        self.head = head

    def print_backward(self):
        print("[", end=" ")
        if self.head is not None:
            self.head.print_backward()
        print("]")

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

    def add_last(self,cargo):
        # Shiny new node to append
        node = Node(cargo)
        
        # Will need a pointer to first element
        n = self.head

        # Traverse list to the end, so that n points to the last node
        while n.next is not None: n = n.next

        # Now append our shiny new node
        n.next = node
        
        # ... and increment the list length
        self.length += 1

    def add_node_at(self, cargo, index=0):
        ''' inserts node with cargo at index specified '''
        # is this a valid position? If not return None.
        if index < 0 or index >= self.length:
            print('invalid index')
            return None

        # make a new node
        node = Node(cargo, None)

        # if index is 0, make the new node the head
        if index == 0:
            self.add_first(cargo)
            return None

        # if index = length-1, make the new node the tail
        if index == self.length-1:
            self.add_last(cargo)
            return None

        # Set n to point at the element preceeding <index>
        n = self.head
        counter = 0
        while counter < index-1: #HERE
            n = n.next
            counter += 1

        # point the new node at the thing in position <index>
        node.next = n.next
        
        # set n to point at the new node
        n.next = node

        # increment length
        self.length += 1

        
        
    def remove_node(self, index=0):
        return None

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


n1 = Node('a')
n2 = Node('b')
n3 = Node('c')


n1.next = n2
n2.next = n3
n3.next = None

L = LinkedList(n1,3)

print_list(L.head)
L.print_backward()


L.add_node_at('now!',2)
print_list(L.head)
