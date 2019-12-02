# This function takes first element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 

import random

def partition(lst, a ,b):
    random_index = random.randint(a,b)  # pick random index, its value will be our 							# pivot val
    lst[b], lst[random_index] = lst[random_index], lst[b]   # swap the value with 										# lst[b]

    pivot = a        # run the rest of the partition code as it was in the original 				 # version
    for i in range(a,b):
        if lst[i] < lst[b]:
            lst[i],lst[pivot] = lst[pivot],lst[i]
            pivot += 1
    lst[pivot],lst[b] = lst[b],lst[pivot]
    return pivot

  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

#  code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
print (arr) 
