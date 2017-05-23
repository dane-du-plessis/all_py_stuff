#bubble sort a list

def bubbleSort(aList):
    for i in range(0, len(aList)-1):
        for j in range (0, len(aList)-1-i):
            if aList[j] > aList[j+1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]
    return aList

L = list('supercalifragilisticexpialidocious')
print(bubbleSort(L))
