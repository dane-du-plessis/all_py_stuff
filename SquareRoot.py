def sqrootRecursive(a,x,epsilon):
    y=(x+a/x)/2
    if abs(y-x) < epsilon:
        print('back')
        return y
    else:
        print('lower')
        return sqroot(a,x,epsilon)
    

def sqrootIterative(a,epsilon):
    x=a
    while True:
        print(x)
        y=(x+a/x)/2
        if abs(y-x) < epsilon:
            break
        x=y
    return y
