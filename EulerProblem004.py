'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPallindrome(arg):
    st = str(arg)
    for i in range(int(len(st)/2)):
        if st[i] != st[len(st)-i-1]:
            return 0
    return 1


'''
a=999
b=999
prod = 0
searching = 1

while(searching):
    prod = a*b
    if isPallindrome(prod):
        searching = 0
        print(prod, ' = ' , a , ' * ' , b)
        break
    b  -= 1
'''
    
'''
searching = 1
for a in range(999,99,-1):
    for b in range(999,99,-1):
        if isPallindrome(a*b):
            searching = 0
            break
    if not searching:
        break
'''

pallindromes = list();
biggest = 0

for a in range(999,99,-1):
    for b in range(999,99,-1):
        if isPallindrome(a*b):
            #print(a*b, ' = ' , a , ' * ' , b)
            pallindromes.append(a*b)
            if a*b >= biggest:
                biggest = a*b
                facs = a,b

