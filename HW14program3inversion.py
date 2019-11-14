   
# merge two arrays in order
def mergeInversion(a,b):
    c = []
    count = 0
    #merge arrays
    while (len(a) > 0 or len(b) > 0):
        # if b is empty
        if len(b) <= 0:
            count += len(a)
            c.append(a.pop(0))
        # if a is empty
        elif len(a) <= 0:
            count += len(a)
            c.append(b.pop(0))
        # a is equal or less
        elif a[0] <= b[0]:
            c.append(a.pop(0))
        # b is less
        elif a[0] > b[0]:
            # count length of left array
            count += len(a)
            c.append(b.pop(0))
    return count


a=[1,2,4,7]
b=[0,3,5,6]

print "count a and b", mergeInversion(a,b)

c=[2,3,5,7]
d=[0,1,4,6]
print "count c and d", mergeInversion(c,d)

# ----OUTPUT
# count a and b 9
# count c and d 12