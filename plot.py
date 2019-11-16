import matplotlib.pyplot as plt
import random
import math
import decimal

# circle
def circle(a):

    firstX = a[0]
    firstY = a[1]

    # radius center point
    secondX = 0
    secondY = 0

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
