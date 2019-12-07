import time
import random
import math


count = 0

def partition(A, l, r):
    pivot = A[l]  # the pivot value
    i = l+1       # We assume the pivot has been moved to the front of the
    # array-This is done in the quicksort method
    
    
    for j in range(l+1, r):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[l], A[i-1] = A[i-1], A[l]
    
    
    

    return i-1

def quicksort(A, l, r):
    if l >= r:
        return
    global count
    count += 1
    
    i = random_pivot(A, l, r)  # Chooses a pivot randomly from l to r
    
    # move pivot to the front of array
    A[l], A[i] = A[i], A[l]
    j = partition(A, l, r)   # partition left and right sides of pivot

    quicksort(A, l, j)      # 2 recursive calls- this one from l to j-1

    quicksort(A, j+1, r)    # This one from j+1 to the end of the array


    


def random_pivot(A, l, r):
    # Randomly pick a value from (l , r)
    rpivot = int((r-l)*random.random()) + l
    return rpivot                        

# make random arr
def make_array():
    arr = []
    for i in range(1000):
        arr.append(random.randint(0,1000))
    return arr


a = make_array()

st = time.time()
print(quicksort(a,0,len(a)))
print("total time",time.time()-st)

print("Array length", len(a))
print("count: ",count)