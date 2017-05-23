# All the engineers
# Very powerful idiot filter

def swap(i,j,s):
    """ Swap elementis i and j in list s
    """
    if i != j:
        temp = s[i]
        s[i]=s[j]
        s[j]=temp

def permute(s,sp):
    """
    <s>  must be a list containing the elements to permute
    <sp> is a list to which further permutations are added
    """
    i = 0
    while i < len(s):
        stemp = s.copy()
        swap(0,i,stemp) #interchange elements 0 and i
        print('i     =',i)
        print('s     =',s)
        print('stemp =',stemp)
        sp.append(stemp.pop(0))
        print('sp    =',sp)
        permute(stemp,sp)
        #permute(s,sp
        
        #stop case:
        if i == len(s)-1:
            sp.append('!')
        i+=1


def permute2(s,sp):
    """
    <s>  must be a list containing the elements to permute
    <sp> is a list to which further permutations are added
    """
    i = 0
    while i < len(s):
        stemp = s.copy()
        swap(0,i,stemp) #interchange elements 0 and i
        print('i     =',i)
        print('s     =',s)
        print('stemp =',stemp)

        #stop case:
        if i == len(s)-1:
            sp.append('!')
        else:
            sp.append(stemp.pop(0))
            print('sp    =',sp)
            permute2(stemp,sp)
            
        i+=1


def perm(s,sp):
    #issues with this discovered problems ....
    st = s.copy() #local copy of original list
    l = len(st)
    for i in range(l):
        swap(0,i,st)
        if l == 1:
            sp.append(st[i])
        else:
            perm(s,st.copy())
            



def permute3(s,sp,sf):
    """
    <s>  must be a list containing the elements to permute
    <sp> is a list to which further permutations are appended
    """
    stemp = s.copy()
    i = 0
    while i < len(s):
        #stop case:
        if i == len(s)-1:
            print('STOP')
            sf.append(sp)
            sf.append(',')
            print('sf = ', sf)
        else:
            swap(0,i,stemp) #interchange elements 0 and i
            print('i     =',i)
            print('s     =',s)
            print('stemp =',stemp)
            sp.append(stemp.pop(0))
            print('sp    =',sp)
            permute3(stemp.copy(),sp,sf) # must pass copy of string? Careful...
        i+=1



def permute4(s,sp,sf):
    i = 0
    while i < len(s):
        print(''*4*i, i)
        stemp = s.copy()
        if i == len(s)-1: # at the end of a permutation, STOP!
            print('STOP')
            print(sp)
            sf.append(sp)
            sf.append(',')
        else:
            swap(0,i,stemp)
            sp.append(stemp.pop(0))
            permute4(stemp.copy(),sp,sf) # must pass copy of string? Careful...
        i+=1
        if i > 0:
            break




s = list('ABC')
sp = []
sf = []

permute4(s,sp,sf)
#perm(s,sp)




























