
import random
import math
import decimal

def make_point():
    x = round(random.random()*2-1,2)
    y = round(random.random()*2-1,2)
    point = (x,y)
    return point


def make_list_points():
    a = []
    for i in range(10):
        a.append(make_point())
    return a


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

b = [(6.52, 5.59), (3.78, 1.55), (4.59, 2.49), (6.53, 1.81), (9.08, 7.26), (3.21, 0.37), (2.07, 0.65), (7.53, 1.98), (8.95, 0.5), (5.72, 3.84), (0.77, 3.65), (1.52, 0.32), (7.23, 8.41), (0.26, 8.83)]
a = make_list_points()
print(b)
print("closest pair: ",find_closest(b))

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