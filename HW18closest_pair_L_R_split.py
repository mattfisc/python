
import random
import math
import decimal

#tuple point
def make_point():
    x = round(random.randrange(0,10),2)
    y = round(random.randrange(0,10),2)

    point = (x,y)
    return point

# tuple list of points
def make_list_points():
    a = []
    for i in range(10):
        a.append(make_point())
    return a

# brute force
def find_closest(a):

    firstP = 0
    secondP = 0
    closest = 999
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            first = a[i]
            firstX = first[0]
            firstY = first[1]

            second = a[j]
            secondX = second[0]
            secondY = second[1]

            check = math.sqrt((secondY - firstY)**2 + (secondX - secondY)**2)

            if check < closest:
                closest = check
                print("distance",closest)
                firstP = first
                secondP = second
                print(firstP,secondP)
    return firstP, secondP

a = make_list_points()

# cut list in half

# find closest left pair

# find closest right pair

# closest split pair

# tester
print(a)