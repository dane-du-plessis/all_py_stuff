class heapermuteClass(object):
    ''' make the permutaiton algorithm work'''
    







def heapermute(A,n):
    ''' Heap algorithm for generating permutations
        Note: It doesn't work! pass by reference, or put all in a class so that the member list is operated on and not just a local copy.
        
    '''
    if n == 0:
        print(A)
        #return A
    else:
        for i in range(0,n):
            #A = heapermute(A,n-1)
            heapermute(A,n-1)
            if (n+1)/2 == 1:
                swap(A,0,n-1)
            else:
                swap(A,i,n-1)


def swap(A,a,b):
    temp = A[b]
    A[b] = A[a]
    A[a] = temp

A = list('pil')
swap(A,0,2)
heapermute(A,3)
