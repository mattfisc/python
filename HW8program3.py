# program 3

import time



def peak(a):
    n = len(a)
    
    peak = a[0]

    for i in range(1,len(a)):
        if peak < a[i]:
            peak = a[i]
        else:
            return peak

A = [4, 7, 2, 3, 9, 1, 6, 0]

print(peak(A))


# ------ OUTPUT ------
# 7

# ORDER N