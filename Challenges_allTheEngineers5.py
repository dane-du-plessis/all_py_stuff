def mygen():
    i = 0
    while i < 100:
        yield i
        i += 1

#https://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python/35871989#35871989?newreg=60cb10ba2b6e4ed69d0f7f0acbc9a46a
# Does not handle duplicates.
def stringPermutations(s):
    if len(s) < 2:
        yield s
        return
    for pos in range(0,len(s)):
        char = s[pos]
        permForRemaining = list(stringPermutations(s[0:pos]+s[pos+1:]))
        for perm in permForRemaining:
            yield char + perm
    
#s ='ENGINEER'
s ='ENGINEER'
gen = stringPermutations(s)

for i in gen:
    print(next(gen))
