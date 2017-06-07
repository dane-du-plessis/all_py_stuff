from myStack import *
import re

def eval_postfix(exp):
    e = re.split('([^0-9])', exp)
    s = Stack()
    for v in e:
        if v == '' or v ==' ':
            continue
        if v == '*':
            s.push(s.pop()*s.pop())
        elif v == '/':
            s.push(s.pop()/s.pop())
        elif v == '+':
            s.push(s.pop()+s.pop())
        elif v == '-':
            s.push(s.pop()-s.pop())
        elif v == '^':
            s.push(s.pop()**s.pop())
        else:
            s.push(int(v))
    return s.pop()

'''
print("Melons and bannanas!".split(' '))

exp = '11*6/*-'
v = re.split("([^0-9])", exp) # you must put the regex in ()
print(v)
'''


exp = ["12 2 /", '4 3 *', '10 5 -', '6 2 ^', '123 321 + ', '2 3 + 4 *']

for i in exp:
    print(i, ' = ', eval_postfix(i))

