import matplotlib.pyplot as plt
import random
import math
import decimal

def distance(a):
    first = a[0]
    firstX = first[0]
    firstY = first[1]

    second = a[1]
    secondX = second[0]
    secondY = second[1]

    distance = math.sqrt((secondY - firstY)**2 + (secondX - secondY)**2)

    return distance


def make_point():
    distance = 2
    while distance > 1:
        x = round(random.random()*2-1,2)
        y = round(random.random()*2-1,2)
        
        point = (x,y)

        distance = distance(point);

    
    return point


def make_list_points():
    a = []
    for i in range(1000):
        a.append(make_point())
    return a



a = make_list_points()
print(a)


# -- OUTPUT
