import random
import math
import decimal
import operator
import matplotlib.pyplot as plt

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
