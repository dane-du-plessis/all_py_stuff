#s = 'abcacbbacbcacabcba'
#s = [123, 132, 213, 231, 312, 321]
s = '123132213231312321'
#s = '12313221'
s = list(s)
#s = [1123, 1132, 1213, 1231, 1312, 1321, 2113, 2131, 2311, 3112, 3121, 3211]
#s = '112311321213123113121321211321312311311231213211'

#delimiter = ''
#delimiter.join(str(s))
v =  list('123')

def findSpellings(word,permutationList,startIndex):
    try:
        startIndex = permutationList[startIndex:].index(word[0])+1
    except ValueError:
        if word == []:# if you've found all the letters...
            # then increment a global counter...
            yield 1
            return
        # now return to calling function...
        #return #or don't return? return None?
    else:
        # pass on a shorter version of the sought word to findSpellings...
        word_pass = word[1:].copy()
        findSpellings(word_pass,permutationList,startIndex)
        # then find the next instance of the first letter in word...
        findSpellings(word,permutationList,startIndex)


def findASpelling(word,permutationList):
    for i in range(len(word)):
        try:
            startIndex = permutationList.index(i)+1
        except ValueError:
            if i < len(word)-1:
                return 0
            elif i == len(word)-1:
                return 1
            else:
                continue

def findASpelling2(word,permutationList):
    print('word = ',word)
    print('permutationList = ', permutationList)
    #print('permutationList.index(word[0]) = ', permutationList.index(word[0]))
    try:
        s = permutationList.index(word[0])
        print(s)
    except ValueError:
        # Can't find v
        print("<<< Can't find v")
    except IndexError:
        print("<<< End of word reached")
    else:
        # Can find v
        print('word[', s, '] = ', word[s]) # no...
        wordPass = word[1:].copy()
        permutationListPass = permutationList[(s+1):].copy()
        findASpelling2(wordPass,permutationListPass)

counter = 0
debug = False
def findS(word,permutationList):
    global counter
    global debug
    if debug: print('word = ',word)
    if debug: print('permutationList = ', permutationList)
    try:
        s = permutationList.index(word[0])
        if debug: print(s)
    except ValueError:
        # Don't increment counter
        if debug: print("<<< Can't find value.")
    except IndexError:
        # Increment counter
        if debug: print("<<< End of word reached. Incrementing global coutner.")
        counter += 1
        print(counter)
    else:
        # Value found, now do two things:
        # 1. Seach for next instance of the same value:
        if debug: print('permutationList[', s, '] = ', permutationList[s])
        permutationListPass = permutationList[(s+1):].copy()
        findS(word,permutationListPass)
        # 2. Seach for next instance of the next value in the word:
        wordPass = word[1:].copy()
        findS(wordPass,permutationListPass)


def findSgen(word,permutationList):
    global debug
    if debug: print('word = ',word)
    if debug: print('permutationList = ', permutationList)
    yield 0
    try:
        s = permutationList.index(word[0])
        if debug: print(s)
    except ValueError:
        # Don't increment counter
        if debug: print("<<< Can't find value.")
        yield 0
    except IndexError:
        # Increment counter
        if debug: print("<<< End of word reached. Yield 1")
        yield 1
    else:
        # Value found, now do two things:
        # 1. Seach for next instance of the same value:
        if debug: print('permutationList[', s, '] = ', permutationList[s])
        permutationListPass = permutationList[(s+1):].copy()
        findS(word,permutationListPass)
        # 2. Seach for next instance of the next value in the word:
        wordPass = word[1:].copy()
        yield findSgen(wordPass,permutationListPass)

#gen = findSpellings(v,s,0)
#counter = 0
#for i in gen:
#    counter += next(gen)

#findASpelling2(v,s)
findS(v,s)


gen = findSgen(v,s)
for i in findSgen:
    print(next(findSgen))



