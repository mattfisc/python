   
# merge two arrays in order
def mergeInversion(a,b,count):
    c = []
    
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


def inversion_count(a):
    b = a[:len(a)//2]
    c = a[len(a)//2:]
    count = 0
    # left half array count
    for i in range(len(b)):
        for j in range(i+1,len(b)):
            if b[i] > b[j]:
                count += 1
                
    # left half array count
    for i in range(len(c)):
        for j in range(i+1,len(c)):
            if c[i] > c[j]:
                count += 1
    return mergeInversion(b,c,count)

a=[3,2,1,5,10,6,4,8,7,9]
print "The count is ",inversion_count(a)

# ----OUTPUT
# The count is  11


