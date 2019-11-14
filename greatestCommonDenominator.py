def gcd(y,x):
    while x > 0:
        y,x = x, y % x
    return y


print(gcd(55,34))
