# My Stack ADT


class Stack:
    def __init__(self):
        self.items = [] # self is now a pointer to an empty list
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []


L = Stack()
'''
L.push("Tom")
L.push("Dick")
L.push("Harry")

while(not L.is_empty()):
    print(L.pop(), end = '')
    if L.is_empty():
        print('.')
    else:
        print(' and ', end = '')
'''
