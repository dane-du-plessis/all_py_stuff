def isPermutation(a,b):
    bcopy = b.copy()
    if len(a) != len(b):
        return False
    for i in a:
        try:
            bcopy.remove(i)
        except ValueError:
            #print('not permutation')
            return False
        #else:
            #print(i, ' removed from ', b)
    #print('is permutation')
    return True

s = list('11123445') # arrange characters in s alphabetically or it won't work
#s = list('123')

# Try this with a list of integers, not characters. Takes about the same amount of time
#s= [1,1,1,2,3,4,4,5]

N = len(s)
charStart = s[0]
charEnd   = s[len(s)-1]

startCountingFrom = int(charStart*len(s))
stopCountingAt = int(charEnd*len(s))
# To use integers:
#startCountingFrom = 11111111
#stopCountingAt = 55555555


permutations = []
permutationsString = ''

counter = 1
badDigit = False
for i in range(startCountingFrom,stopCountingAt):
    #build a list with candidate permutation i
    testNumberList = []
    badDigit = False
    for place in reversed(range(N)):
        nextDigit = (i//(10**place))  %  10
        testNumberList.append(str(nextDigit))
        #testNumberList.append(nextDigit) #if youre using ints and not chars
        #print(nextDigit)
        if nextDigit == 0 or nextDigit == 6 or nextDigit == 7 or nextDigit == 8 or nextDigit == 9: #or any other digit we don't care about
            del testNumberList
            badDigit = True
            break
    if badDigit:
        #print('bad digit')
        continue
    if isPermutation(s,testNumberList):
        #print(i)
        permutations.append(i)
        permutationsString = permutationsString + str(i)
        print(counter, ' ' , i)
        counter += 1
    del testNumberList
    
        


