def multiply_matrix(n):
    acc = 0
    k = 1
    while k < n:
        for i in range(1,n):
            if i <= 2:
                acc += 1 * n-i
            else:
                acc += i * n-i
        k+=1
        
    return acc


print "The count is ",multiply_matrix(5)

#---output
#The count is  140
