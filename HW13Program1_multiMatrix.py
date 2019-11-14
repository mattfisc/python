#Matthew Fischer
#HW #3

count = 0

def multiply_matrix(n):
    global count
    count += 1
    if n <= 2:
        return 1
    else:
        acc = 0
        for i in range(1,n):
            acc += multiply_matrix(i) * multiply_matrix(n-i)
    return acc

c=[1,2,3,4,5]
print multiply_matrix(5)
print "count =", count

#output
#14
#count = 45

