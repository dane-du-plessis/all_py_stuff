""" This is just some random stuff
"""

def countdown(n):
    if n < 0:
        print("All done!")
    else:
        print(n)
        countdown(n-1)


def factorial(n):
    if n == 0:
        return(1)
    else:
        return(n*factorial(n-1))


#print('a', end='')


def spaces(n):
    if n==0:
        return
    else:
        print(' ', end='')
        spaces(n-1)

        

def rjust(aString):
    spaces(70-len(aString))
    print(aString)

