import Nodes

class Queue:
    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0
        

    def is_empty(self):
        return self.length ==0

    def insert(self, cargo):
        node = Node(cargo)
        if self.head is None:
            # If this is the only element in the list, head is node
            self.head = node
            self.last = node
        else:
            # attach new node to the end
            last = self.head
            while last.next:
                last = last.next

            # now last is the last node. Append new node to it.
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo

class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items # this will actually work. Not sure why.

    def insert(self,item):
        self.items.append(item)
        print(self.items)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item



'''
So, will it blend?
'''

import random as r

q = PriorityQueue()


for n in range(0,100):
    num = r.randint(0,10)
    print(num)
    q.insert(num)


while(not q.is_empty()):
    print(q.remove())

'''
for i in [11,12,14,13]:
    q.insert(i)

while not q.is_empty():
    print(q.remove())
'''

