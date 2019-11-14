# program 6

def increasing_decreasing(a):

    countIncrease= 0
    countDecrease = 0
    increase = 0
    decrease = 0

    # end one early 
    for i in range(len(a)-1):

        #increase count
        if a[i]+1 == a[i+1]:
            increase += 1
        # end of increase
        else:
            if countIncrease < increase:
                increase+=1 #count last num
                countIncrease = increase
            increase = 0
        
        #decrease count
        if a[i]-1 == a[i+1]:
            decrease += 1
        else:
            if countDecrease < decrease:
                decrease += 1 #count last num
                countDecrease = decrease
            decrease = 0

    return countIncrease, countDecrease

A=[1,2,4,3,2,5,7,8,12,8,13,14,12,8,6,4,2,3,4] 
print(increasing_decreasing(A))

# ----- OUTPUT ------
# (2,3)

# ORDER 2N