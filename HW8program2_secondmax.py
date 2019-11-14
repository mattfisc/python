
def findSecondMax(a):
    n = len(a)
    max = a[0]

    for i in range(1,n):
        if a[i] > max:
            old_max = max
            max = a[i]
        print(i," ", max)
    return old_max


a = [1,2,3,5,6,8,0,4,42,7,3,1]
print(findSecondMax(a))

# ---- OUTPUT -------
# 8