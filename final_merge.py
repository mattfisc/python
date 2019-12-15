# partition
import random
import time
import sys
sys.setrecursionlimit(100000)


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
    global count
    
    count += 1

    i = choose_pivot(A, l, r)  # Chooses a pivot randomly from l to r
    # Moves the random pivot to the beginning of the array
    A[l], A[i] = A[i], A[l]
    j = partition(A, l, r)   # Then do the paretitioning

    quicksort(A, l, j)      # 2 recursive calls- this one from l to j-1
    quicksort(A, j+1, r)    # This one from j+1 to the end of the array

def choose_pivot(A, l, r):
    # Randomly pick a value from (l , r)# from begining to end
    rpivot = int((r-l)*random.random()) + l
    #return rpivot                        # This is our random pivot
    return r-1
                    

# make random arr
def make_array1():
    arr = []
    for i in range(1000):
        arr.append(random.randint(0,1000))
    return arr
    
# make random arr
def make_array():# array in order
    arr = []
    for i in range(1000):
        arr.append(i)
    return arr

# sort by count
def sort(A,mixer):
    
    
    for i in range(mixer+1):
        r1 = random.randint(0,len(A)-1)
        r2 = random.randint(0,len(A)-1)
        A[r1],A[r2] = A[r2],A[r1]
    return A
    

a = make_array()
sort(a,50)
print("Array length", len(a))
st = time.time()#start time
quicksort(a,0,len(a))
print("total time",time.time()-st)#end time

#print("Recursive count: ",count)