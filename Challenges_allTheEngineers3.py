def swap(i,j,s):
    """ Swap elementis i and j in list s
    """
    if i != j:
        temp = s[i]
        s[i]=s[j]
        s[j]=temp


def permute(s,sp,sf):
    i = 0
    while i < len(s):
        stemp = s.copy()
        swap(0,i,stemp)
        sp.append(stemp.pop(0))
        if i == len(s)-1: # at the end of a permutation, STOP!
            #print('STOP')
            #print(sp)
            sf.append(sp.copy()) #needs to be a COPY!
            sf.append(',')
            return
        else:
            permute(stemp.copy(),sp.copy(),sf) # must pass copy of string? Careful...
            sp.pop()
        i+=1


def stringPermutations(s):
    if len(s) < 2:
        yield s
        return
    for pos in range(0, len(s)):
        char = s[pos]
        permForRemaining = list(stringPermutations(s[0:pos] + s[pos+1:]))
        for perm in permForRemaining:
            yield char + perm


s = list('ABC')
sp = []
sf = []

s ='ABC'
gen = stringPermutations(s)

#for i in gen:
#    print(next(gen))

print(next(gen))

