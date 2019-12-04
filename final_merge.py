import random
import time

level = 0

def mergeSort(a):
    if len(a) == 1:
        return a
    else:

        frontEnd = mergeSort(a[:len(a)//2])       
        backEnd = mergeSort(a[len(a)//2:])
        return merge2(frontEnd,backEnd)

def RSelect(arr,l,r,k):
    global level
    level = 0
    return arr




#test
n=1000
a=[]
for i in range(n):
    a.append(i)
t1= time.time()
RSelect(a,0,n-1,n//2)