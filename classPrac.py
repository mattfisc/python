def fives(n):
    count = 0
    
    if n % 5 != 0:
        return 0
    else:
        count = 0
        while n % 5 == 0:
            n=n//5
            count += 1
        return count

def fives_factorial(n):
    count = 0
    
    if n % 5 != 0:
        return 0
    else:
        return 


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

def twos(n):
    count = 0
    
    if n % 2 != 0:
        return 0
    else:
        count = 0
        while n % 2 == 0:
            n=n//2
            count += 1
        return count

print(fives_factorial(25))

