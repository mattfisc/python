# Matthew Fischer
# Project 2

arr = [3,7,5,6,9]

max_so_far = arr[0]
left = 99
right = 99

# max so far
for i in range(0,len(arr)):
    if max_so_far < arr[i]:
        max_so_far = arr[i]
    else:
        arr[i] = max_so_far
    
# find left and right window
double = False
for i in range(0,len(arr)-1):
    # find left
    if arr[i] == arr[i+1] and double == False:
        left = i
        double = True
    # find right
    if arr[i] != arr[i+1] and double == True:
        right = i



# output answer
print(left)
print(right)
print(arr)

#-------OutPut--------
#Windows PowerShell
#Copyright (C) Microsoft Corporation. All rights reserved.
#
#PS C:\Users\Matthew Fischer\Documents\Python\Python> & C:/Python27/python.exe "c:/Users/Matthew Fischer/Documents/Python/CS240/Program#2.py"
#1
#3
#[3, 7, 7, 7, 9]
#PS C:\Users\Matthew Fischer\Documents\Python\Python>
#
