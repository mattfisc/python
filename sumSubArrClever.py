# Matthew Fischer
# subarray addition
# what array is the biggest sum
# using O(n)


arr = [34,-50,42,14,-5,86]
arr2 = [10,-12,4,8,6,-20,2,4]

left_sum = 0
right_sum = 0
sum = 0

left_index = 0
right_index = 0

# left to right sum max
for i in range(len(arr)):
    sum += arr[i]



    # find max sum
    if sum > left_sum:
        left_sum = sum
        right_index = i # right index

#reset
sum = 0

# right to left sum max
for i in range(len(arr)-1,-1,-1):
    sum += arr[i]

    if sum < 0:
        sum = 0

    # find max sum
    if sum > right_sum:
        right_sum = sum
        left_index = i  # left index
        

sum = 0
for i in range(left_index,right_index+1):
    sum+=arr[i]

print("-----------")
print("total sum")
print(sum)

print("left index")
print(left_index)
print("right index")
print(right_index)


