def is_power(a,b):
    """ Recursive. Returns True if a is in fact a power of B, False returned otherwise.
    A number, a, is a power of b if it is divisible by b and a/b is a power of b. 
    """
    if a%b==0:
        if a==b:
            print("Is a power!")
            return True
        print("Recursion...")
        is_power(a/b,b)
    else:
        print('Not a power')
        return False
