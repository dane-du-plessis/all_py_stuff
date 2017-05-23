def sum35mults(N):
    t=[]
    for i in range(N):
        if i%3 == 0 or i%5 == 0:
            t.append(i)

    return t
