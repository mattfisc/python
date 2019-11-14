def permu(a):
    b=[]
    for i in range(len(a)-1,-1,-1):
        if a[i] < a[i-1]:
            b=a[i:]
            # swap numbers
            #find index to next num
            for j in range(len(b)):
                if(b[j] > b[0] and b[j] < num):
                    num = b[j]
                    indexSwap = j
            #swap to next num bigger
            a[i],a[i+indexSwap] = a[i+indexSwap],a[i]
            # sort array to right
        # in order least to greatest
        else:
            a[0],a[1]=a[1],a[0]
            b = a[1:]
            b.sort()
            a=a[0] + b


a=[1,2,3,4,5,6]
print(permu(a))