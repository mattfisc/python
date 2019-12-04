def mergeSort(a):
    if len(a) == 1:
        return a
    else:

        frontEnd = mergeSort(a[:len(a)//2])       
        backEnd = mergeSort(a[len(a)//2:])
        return merge2(frontEnd,backEnd)
    