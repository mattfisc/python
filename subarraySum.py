# Matthew Fischer
# subarray addition
# what array is the biggest sum
arr = [-2,-4,-3]


max_Sum = 0
f_max_index = 0
l_max_index = len(arr)-1

# check every sub array for highest value
for i in range(len(arr)): 
    sum = 0
    for j in range(i,len(arr)):
        sum += arr[j]
    
        if sum > max_Sum:
            max_Sum = sum
            f_max_index = i
            l_max_index = j

print(max_Sum)
print(f_max_index)
print(l_max_index)


        