import random
def is_prime(x):
    prime = False
    for i in range(2,x-1):

        if x % i == 1:
            prime = True

    if prime:
        return 1
    else:
        return 0

def gcd(y,x):
    while x > 0:
        y,x = x, y % x

    if y == 1:
        return 1
    else:
        return 0
    



count = 0
for i in range(100):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    count += gcd(num1,num2)
print("100 random count = ",count)

count = 0
for i in range(1000):
    num1 = random.randint(1,1000)
    num2 = random.randint(1,1000)
    count += gcd(num1,num2)
print("1000 random count = ",count)

count = 0
for i in range(10000):
    num1 = random.randint(1,10000)
    num2 = random.randint(1,10000)
    count += gcd(num1,num2)
print("10000 random count = ",count)

#  -------- OUTPUT ------
# ('100 random count = ', 71)
# ('1000 random count = ', 626)
# ('10000 random count = ', 6165)
# ODDS ARE A LITTLE OF 60 PERCENT THAT YOU GET PRIME NUMBERS
