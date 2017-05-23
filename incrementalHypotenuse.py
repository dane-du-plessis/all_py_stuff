def hypotenuse(a,b):
    r = (a**2 + b**2)**0.5
    return r


def is_between(x,y,z):
    if x <= y and y <= z:
        return True
    else:
        return False
