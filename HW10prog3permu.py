def permutations(a):
    b = []
    num = 10000
    indexSwap = 0
    for i in range(len(a)-1,-1,-1):
        #STEP ONE
        #find next switch
        if a[i-1] > a[i]:
            # a[i] is start of next num
            #subarray
            b = a[i:]
            
            #STEP TWO
            #FIND NEXT NUMBER
            for j in range(len(b)):
                if(b[j] > b[0] and b[j] < num):
                    num = b[j]
                    indexSwap = j
            #swap to next num bigger
            a[i],a[i+indexSwap] = a[i+indexSwap],a[i]

            # SORT END
            b = a[i+1:]
            b.sort()
            a = a[:i+1] +b
            break;
        # if all in order next permutation is swaping first and second index
        elif i == 1:
            a[0],a[1]= a[1],a[0]
            break;
    return a


a = [1,4,6,3,2,7,8]

print(permutations(a))

# ------OUTPUT -------
# [1, 4, 6, 3, 7, 2, 8]