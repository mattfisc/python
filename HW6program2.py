
def sumBinary(x,y):
    # x is longer
    if len(x) < len(y):
        x,y = y,x

    sum = 0

    for i in range(len(x)-1,-1,-1):
        sum += x[i] + y[i]

        # remainder
        if sum > 1:
            x[i] = sum % 2
            sum /= 2

        # no remainder
        else:
            x[i] = sum % 2
            sum = 0
        
        # end of array with remainder
        if i == 0 and sum != 0:
            x.insert(0,sum)
        
    return x


a = [1,0,1,1,0,1,1,1]
b = [1,1,1,0,1,0,1,0]

print(a)
print(b)
print(sumBinary(a,b))


# ------ OUTPUT --------
#    [1, 0, 1, 1, 0, 1, 1, 1]
#    [1, 1, 1, 0, 1, 0, 1, 0]
# [1, 1, 0, 1, 0, 0, 0, 0, 1]