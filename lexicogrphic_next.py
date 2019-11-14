def lexico(a):
    index = 0
    nextV = 0
    last_of_arr = []

    # end at index 1 for out of bounds
    for i in range(0,len(a)-1,-1):
        if(a[i-1] < a[i]):
            index = i-1
            last_of_arr = a[i:]
            nextV = a[index];

            # find next biggest
            for j in range( (len(last_of_arr)-1) ):
                if(last_of_arr[j] > a[index] and last_of_arr[j] < nextV):
                    nextV = last_of_arr[j]
    a[index],nextV = nextV,a[index] 

    # sort end

    # arr combined
    return last_of_arr

a = [8,9,3,6,5,4,2,1]
print(lexico(a))

# last_of_arr = a[i:]
 #           last_of_arr.sort
  #          a = a[:i+1] + last_of_arr