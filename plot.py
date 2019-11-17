import matplotlib.pyplot as plt
import random
import math
import decimal

def distance(a):
    #point
    firstX = a[0]
    firstY = a[1]
    #center of cirle
    secondX = 0
    secondY = 0

    #distance formula
    distance = math.sqrt((secondY - firstY)**2 + (secondX - secondY)**2)

    return distance


def make_point():
    distance = 2

    #find point in circle radius
    while distance > 1:
        # tuples of -1 to 1
        # x,y
        x = round(random.random()*2-1,2)
        y = round(random.random()*2-1,2)
        
        point = (x,y)
        
        #check distance from center of circle
        # center is 0,0
        distance = distance(point);

    
    return point


def make_list_points():
    a = []
    for i in range(10):
        a.append(make_point())
    return a



a = make_list_points()
print(a)


# -- OUTPUT
#[(-0.31, -0.44), (0.32, 0.92), (0.97, -0.14), (-0.95, -0.71), (-0.72, -0.45), (-0.83, 0.51), (-0.06, 0.51), (-0.62, 0.58), (0.75, -0.27), (-0.88, 0.71)]
#distance 1.486472334084964
#(-0.31, -0.44) (0.32, 0.92)
#distance 1.1498260738042079
#(-0.31, -0.44) (0.97, -0.14)
#distance 0.3612478373637688
#(-0.31, -0.44) (-0.95, -0.71)
#distance 0.2701851217221259
#(-0.31, -0.44) (-0.72, -0.45)

#closest pair: ((-0.31, -0.44), (-0.72, -0.45))
