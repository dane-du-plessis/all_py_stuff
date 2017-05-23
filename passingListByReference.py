def chop(t):
    del t[0]
    del t[len(t)-1]
    return None

def middle(t):
    u = t
    chop(u)
    return u
