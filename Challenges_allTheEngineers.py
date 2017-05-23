# All the engineers

def swap(i,j,s):
    """ Swap elementis i and j in list s
    """
    # if s[i]==s[j]: don't bother adding this permutation to the list
    temp = s[i]
    s[i]=s[j]
    s[j]=temp

def p1(s):
    #return a list of all the permutations of the list <s>
    if len(s)==1:
        return s
    else:
        return s + givePerm(s[1:])

def p2(slist):
    #print(slist)
    if len(slist) == 1:
        #stop
        print(slist)
        return slist
    for j in range(len(slist)):
        # Copy the list
        subslist = slist.copy() # you'll be needing this...
        # Swap elements 0 and j
        swap(0,j,subslist)
        for i in range(len(slist)):
            print(slist[i])
            #print(type(slist[i]))
            return [slist[i]] + perms2(slist[1:])

def p3(s):
    if something
        #stop
    for i in range(len(s)):
        
        


s = '123'
sl = list(s)

