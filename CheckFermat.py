a = int(input('a'))
b = int(input('b'))
c = int(input('c'))
n = int(input('n'))

def checkFermat(a, b, c, n):
    if a**n + b**n == c**n:
        print('This works because')
        print('a**n + b**n = ', a**n + b**n, ' = c**n = ', c**n);
    elif a**n + b**n == c**n and n > 2:
        print('Fermat was a twit!')
    else:
        print("doesnt work")


        
checkFermat(a,b,c,n)
