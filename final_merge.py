import time
import random
import math


count = 0

def partition(A, l, r):
    pivot = A[l]  # the pivot value
    i = l+1       # We assume the pivot has been moved to the front of the
    # array-This is done in the quicksort method
    print("A before: ",A)
    for j in range(l+1, r):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[l], A[i-1] = A[i-1], A[l]
    print("A after: ",A)

    return i-1

def quicksort(A, l, r):
    if l >= r:
        return
    global count
    count += 1
    print("count: ",count)
    i = random_pivot(A, l, r)  # Chooses a pivot randomly from l to r

    # move pivot to the front of array
    A[l], A[i] = A[i], A[l]
    j = partition(A, l, r)   # partition left and right sides of pivot

    quicksort(A, l, j)      # 2 recursive calls- this one from l to j-1

    quicksort(A, j+1, r)    # This one from j+1 to the end of the array


    return A


def random_pivot(A, l, r):
    # Randomly pick a value from (l , r)
    rpivot = int((r-l)*random.random()) + l
    print("random index: ",rpivot)
    return rpivot                        

a = [5,2,4,10,6,8,7,1,9,3,11]

print(quicksort(a,0,len(a)))