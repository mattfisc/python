# program 5

def findI(a):
    # termination
    n = len(a)
    if n == 1:
        return a[0];

    elif a[n//2-1] > a[n//2]:
        return findI(a[:n//2]);
    else:
        return findI(a[n//2:]);

A=[-4,-3,1,2,4,8,9,10,11,12,14,18,19,22,50,51]
print(findI(A))

# ----- OUTPUT ------
# [4]

# ORDER N