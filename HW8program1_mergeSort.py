# Matthew Fischer
# # Program 1

def mergeSort(a):
    if len(a) == 1:
        return a
    else:

        frontEnd = mergeSort(a[:len(a)//2])
        backEnd = mergeSort(a[len(a)//2:])
        return merge2(frontEnd,backEnd)
        

def merge2(a,b):
    c = []

    #merge arrays
    while (len(a) > 0 or len(b) > 0):
        # if b is empty
        if len(b) <= 0:
            c.append(a.pop(0))
        # if a is empty
        elif len(a) <= 0:
            c.append(b.pop(0))
        # a is equal or less
        elif a[0] <= b[0]:
            c.append(a.pop(0))
        # b is less
        elif a[0] > b[0]:
            c.append(b.pop(0))  
    return c

a = [82,91,55,8,2,7,4,1,9,3,5,15,16,30,22,32]

print(mergeSort(a))

# ---- OUTPUT -------
# [1, 2, 3, 4, 5, 7, 8, 9, 11, 15, 16, 21, 22, 24, 28, 30, 32, 55, 91]

# ORDER 