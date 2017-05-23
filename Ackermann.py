def ack(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1,1)
    elif m > 0 and n > 0:
        return ack(m-1,ack(m,n-1))
    else:
        print('Something\'s wrong.')
        return None
    


for m in range(4):
    print('')
    for n in range(5):
        val =str(ack(m,n))
        print( (5-len(val))*' ' ,val,end = ' ')
