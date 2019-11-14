# Matthew Fischer
# CS 240
# Homework 4 Program 2

def wrap_by_k(a,k):
    
    for i in range(k):
        temp = a[len(a)-1]
        for j in range(len(a)-1,0,-1):
            a[j] = a[j-1]  
        a[0] = temp

    return a

a = [1,2,3,4,5,6,7,8]

print(wrap_by_k(a,3))

#------ OUTPUT -------------

#[6, 7, 8, 1, 2, 3, 4, 5]
