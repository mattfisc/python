import math

def karatsuba(x,y):
    power = int(math.log10(z)+1)/2

    x = z // (10 ** power)
    y = z % (10 ** power)

    # cut in half
    a = x // (10 ** (power/2))
    b = x % (10 ** (power/2))
    c = y // (10 ** (power/2))
    d = y % (10 ** (power/2))

    ac = a*c
    bd = b*d

    #single digit termination
    if a % 10 == a:
        return 10**(power) * ac + (10 ** (power/2) * ((a+b) * (c+d) -ac -bd)) +bd
    else:
        return karatsuba(a,b) + karatsuba(b,c)

x = 1234
y = 5678

karatsuba(x,y)