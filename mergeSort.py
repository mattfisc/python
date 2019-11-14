def mergeSort(a):
    if len(a) == 1:
        return a
    else:

        frontEnd = mergeSort(a[:len(a)//2])       
        backEnd = mergeSort(a[len(a)//2:])
        return merge2(frontEnd,backEnd)
    

def merge2(a,b):
    c = []
    
    aI = 0
    bI = 0

    # a and b are not empty
    while (aI >= len(a) and bI >= len(b)):
        if aI > len(a)-1:
            c.append(b[bI])
        elif bI > len(b)-1:
            c.append(a[aI])
        if a[aI] < b[bI]:
            c.append(a[aI])
            aI += 1
        elif b[bI] < a[aI]:
            c.append(b[bI])
            b += 1
    return c

        
   

a = [8,3,5,2,7,6,9,1,4,0]

print(mergeSort(a))

