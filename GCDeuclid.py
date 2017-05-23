def gcd(a,b):
    """ Find the greatest common divisor of (a,b) using Euclid's algorithm
    BEHOLD: If r is the remainder when a is divided by b, then gcd(a,b) = gcd(b,r). As a base case, we can
    consider gcd(a,0) = a.
    """
    r=a%b
    print(a, ' ', b, ' ', r)
    if r==0:
        return b
    else:
        return gcd(b,r)


print(gcd(1071,462))
