# Matthew Fischer
# CS240
# Home Work 4 Program 3


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def count_zeros(num):
    if num % 10 != 0:
        return 0
    if num % 10 == 0:
        return 1 + count_zeros(num/10)

n = factorial(100)
print(n)
print(count_zeros(n))

#------- OUTPUT ---------
#PS C:\Python27\cs240> & C:/Python27/python.exe c:/Python27/cs240/factorialRecusion.py
#93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
# 24
# PS C:\Python27\cs240>