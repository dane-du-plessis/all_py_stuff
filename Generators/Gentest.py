def myGen(N):
    for i in range(N):
        if i%2==0:
            yield 1

def myGen2(N):
    counter = 0;
    while True:
        if counter == N:
            yield 3.14
            return
        yield counter
        counter += 1


        
g = myGen(100)
g2 = myGen2(100)

#totalEven =0
#for i in g:
#    totalEven += i


for i in g2:
    print(i)
