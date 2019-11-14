# Matthew Fischer
# CS 240
# Homework 4 Program 1



def reverse_array(a):
    j = len(a) -1

    for i in range(len(a)/2):
        a[i],a[j] = a[j],a[i]
        j = j-1
    return a
    

a = [1,2,3,4,5]
b = [44,21,66,77,99,33,11]

print(reverse_array(a))
print(reverse_array(b))


#---------- OUTPUT -----------------

# [5, 4, 3, 2, 1]
# [11, 33, 99, 77, 66, 21, 44]
