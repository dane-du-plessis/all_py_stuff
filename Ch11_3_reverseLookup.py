#d = { 'one': 'vwan', 'two':'tooh', 'three':'sghree'}

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
        h[c]=h.get(c,0)
        h[c]+=1
    return h

def printHistogram(h):
    print('PRINT HISTOGRAM')
    k = list(h.keys())
    k.sort()
    for i in k: print(i, ' : ' , h[i])

def reverse_lookup(d,v):
    ''' find keys k in dictionary d corresponding to value v '''
    keys = []
    for k in d:
        if d[k] == v:
            keys.append(k)
    return keys

def invert_dictionary(h):
    ''' inverts histogram h '''
    inv = dict()
    for k in h:
        v = h[k] # v is value in h corresponding to k
        if not inv.get(v,0): inv[v] = [] # if v is not a key in inv, create it and assign it a singleton
        inv[v].append(k)
    return inv


filename = 'WordsA.txt'
dic=dicBuild(filename)

#h=histogram('thisisanexparrot')
#h=histogram('parrot')
#h=histogram('Absolutely fabulous dictionary inverter!')
h=histogram('Lists can appearas values in a dictionary. For example, if you were given a dictionary that maps from letters to frequencies, you might want to invert it; that is, create a dictionary that maps from frequencies to letters. Since there might be several letters with the same frequency, each value in the inverted dictionary should be a list of letters.')
printHistogram(h)
k=reverse_lookup(h,4)

i=invert_dictionary(h)
printHistogram(i)
