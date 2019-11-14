def findMax(a):

    n = len(a)
    if n <= 1:
        return a[0]
    else:
        return max(findMax(a[1:]),a[0])

def findMaxR(a):
    n = len(a)
    middle = n/2

    print(a[:middle],a[middle:])

    if n <= 1:
        return a[0]
    else:
        return max(findMaxR(a[:middle]), findMaxR(a[middle:]))


a = [1,2,3,5,6,8,0,4,42,7,3,1]
print(findMaxR(a))