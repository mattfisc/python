import time
import random
import math


count = 0

def partition(A):
    pivot = A[0]  # the pivot value
    i = 1      # We assume the pivot has been moved to the front of the
    # array-This is done in the quicksort method
    print("A before: ",A)
    for j in range(1,len(A)):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[0], A[i-1] = A[i-1], A[0]
    print("A after: ",A)

    return i-1

def quicksort(A):
    if len(A) <= 1:
        return
    global count
    count += 1
    print("count: ",count)

    i = random_pivot(A)  # random pivot index

    # move pivot to the front of array
    A[0], A[i] = A[i], A[0]

    j = partition(A)   # partition left and right sides of pivot

    quicksort(A[:j])      # 2 recursive calls- this one from l to j-1

    quicksort(A[j:])    # This one from j+1 to the end of the array


    return A


def random_pivot(A):
    # Randomly pick a value from (l , r)
    rpivot = int((len(A))*random.random()) + 0
    print("random index: ",rpivot)
    return rpivot                        

a = [5,2,4,10,6,8,7,1,9,3,11]

print(quicksort(a))