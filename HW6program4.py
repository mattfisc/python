import math
import time

def karat(x,y):
    length = int(math.log10(x) +1)

    # cut in half

    if length == 1:
        return x*y
    else:
        power = length//2

        a = x // (10 ** (power))
        b = x % (10 ** (power))
        c = y // (10 ** (power))
        d = y % (10 ** (power))

        ac = karat(a,c)
        ad = karat(a,d)
        bc = karat(b,c)
        bd = karat(b,d)
        
    return 10**length *ac + 10**(length//2) * (ad + bc) + bd
    
x= 1234567891011121314151617181920212223242526272829303132333435363
y= 1357911131517192123252729313335373941434547495153555759616365676

st = time.time()
print(karat(x,y))
print("The time for 64 digits: ")
print(time.time()-st)


# ---- OUT PUT -------
# 1676433481817705266129514737418074430686007117601914669622664784839603755332117192533414749453310762762797651012520861917800388

# The time for 64 digits:
# 0.0400002002716
