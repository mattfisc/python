# program 4

import time

def peak(a):
    peak = a[0]

    for i in range(1,len(a)):
        if peak < a[i]:
            peak = a[i]
        else:
            return peak

A=[]
for i in range(2**24):
    A.append(i)
for i in range(10):
    A.append(10-i)

st= time.time()
print(peak(A))
print(time.time()-st)

# ---- OUTPUT -----
# 16777215
# 2.81700015068

# COMPLEXITY ORDER N