import matplotlib.pyplot as plt
import random
import math
import decimal
import operator


# distance check from center
def distance(a,r):
    #point
    firstX = a[0]
    firstY = a[1]

    #center point
    secondX = r[0]
    secondY = r[1]

    #distance formula
    distance = math.sqrt((secondY - firstY)**2 + (secondX - secondY)**2)

    return distance


def make_point():
    
    # make tuple of(x,y)
   
        # tuples of -1 to 1
    x = round(random.random()*2-1,2)
    y = round(random.random()*2-1,2)
    
    point = (x,y)

    return point


def make_list_points():
    a = []
    for i in range(1000):
        a.append(make_point())

    return a

a = make_list_points()
print(a)


# -- OUTPUT