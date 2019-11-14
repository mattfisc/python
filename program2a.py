# Matthew Fischer
# subarray addition
# what array is the biggest sum


a = [34,-50,42,14,-5,86]
b = [10,-12,4,8,6,-20,2,4]

def largest_subarray(arr):
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
    return max_Sum,f_max_index,l_max_index

print(largest_subarray(a))
print(largest_subarray(b))


#output
#PS C:\Python27\cs240> & C:/Python27/python.exe c:/Python27/cs240/program2a.py
#(137, 2, 5)
#(18, 2, 4)
#PS C:\Python27\cs240>
        