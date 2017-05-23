def dicBuild(filename):
    fin = open(filename)
    dic = dict();
    counter = 0
    for line in fin:
        word = line.strip()
        dic[word]=str(counter)
        counter += 1
    return dic

def histogram(s):
    h = dict()
    for c in s:
        if c not in h:
            h[c] = 1
        else:
            h[c] += 1
    return h


def histogram2(s):
    h = dict()
    for c in s:
        h[c]=h.get(c,0)
        h[c]+=1
    return h

filename = 'WordsA.txt'
dic=dicBuild(filename)

def printHistogram(h):
    print('PRINT HISTOGRAM')
    k = list(h.keys())
    k.sort()
    for i in k: print(i, ' : ' , h[i])
        

#'apple' in dic

vals = dic.values()

for a in dic: print( 'val:', dic[a] , ' : index:' , a )

bigString = ''
for s in dic: bigString += s

hist = histogram(bigString)

for a in hist: print( a , ' : ' , hist[a] )


printHistogram(hist)


ind = []
val = []
for a in hist:
    ind.append(a)
    val.append(hist[a])
    print(ind[len(ind)-1:] , ' , ' , val[len(ind)-1:])
