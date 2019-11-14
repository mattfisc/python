def inversion_longway(a):
    count = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                count += 1
    return count

a=[3,2,1,5,10,6,4,8,7,9]
print "The count is",inversion_longway(a)

# ---- OUTPUT
# The count is 11