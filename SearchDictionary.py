def dicBuild(filename):
    fin = open(filename)
    aList = dict();
    for line in fin:
        word = line.strip()
        aList[word]=None
    return aList
        
filename = 'WordsA.txt'
a=dicBuild(filename)
