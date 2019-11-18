import math
import random


def make_point():
    
    # make tuple of(x,y)
   
        # tuples of -10 to 10
    x = round(random.random()*11-1,2)
    y = round(random.random()*11-1,2)
    
    point = (x,y)

    return point


def make_list_points():
    a = []
    for i in range(50):
        a.append(make_point())

    return a



# find closest from delta
def split_pair(x,y):

    #create 50 points
    
    delta = 1.1
    
    


a = make_list_points()
print(a)

