# partition
import random
import time
count = 0


def partition(A, l, r):
    pivot = A[l]  # the pivot value
    i = l+1       # We assume the pivot has been moved to the front of the
    # array-This is done in the quicksort method

    for j in range(l+1, r):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i = i+1
    A[l], A[i-1] = A[i-1], A[l]

    return i-1

def quicksort(A, l, r):
    if l >= r:
        return

    i = choose_pivot(A, l, r)  # Chooses a pivot randomly from l to r
    # Moves the random pivot to the beginning of the array
    A[l], A[i] = A[i], A[l]
    j = partition(A, l, r)   # Then do the paretitioning

    quicksort(A, l, j)      # 2 recursive calls- this one from l to j-1
    quicksort(A, j+1, r)    # This one from j+1 to the end of the array

def choose_pivot(A, l, r):
    # Randomly pick a value from (l , r)
    rpivot = int((r-l)*random.random()) + l
    return rpivot                        # This is our random pivot
                    

# make random arr
def make_array1():
    arr = []
    for i in range(1000):
        arr.append(random.randint(0,100))
    return arr
    
# make random arr
def make_array():# array in order
    arr = []
    for i in range(1000):
        arr.append(i)
    return arr


a = make_array()

print("Array length", len(a))
st = time.time()#start time
quicksort(a,0,len(a))
print("total time",time.time()-st)#end time


print("Recursive count: ",count)