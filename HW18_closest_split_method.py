import math
import random
from operator import itemgetter


def sortY(tup):  
      
    # getting length of list of tuples 
    lst = len(tup)  
    for i in range(0, lst):  
          
        for j in range(0, lst-i-1):  
            if (tup[j][1] > tup[j + 1][1]):  
                temp = tup[j]  
                tup[j]= tup[j + 1]  
                tup[j + 1]= temp  
    return tup  

def make_point():
    
    # make tuple of(x,y)
   
        # tuples of -10 to 10
    x = round(random.uniform(-10,10),2)
    y = round(random.uniform(-10,10),2)
    
    point = (x,y)

    return point


def make_list_points():
    a = []

    # list of 64 random points
    for i in range(64):
        a.append(make_point())

    return a



# find closest from delta
def closest_point(a):
    # sort x
    a.sort()
    #print("sorted x\n", a)


    # find middle
    # right side keeps on the line
    middleI = 0
    for i in range(len(a)):
        if a[i][0] < 0:
            print(a[i][0])
            middleI = i
        else:
            break

    firstX=a[:middleI+1]
    print("\nleft side\n",firstX)
    secondX=a[middleI+1:]
    print("\nright side\n",secondX)
    return firstX,secondX
    
def closestPair(lx,ly,rx,ry):
    if lx < 3 and 



a = make_list_points()

closest = closest_point(a)


#print("Non sorted list: \n",a)

# sort x axis
#a.sort()
##print("x axis sort:\n",a)

#sortY(a)
#print("y axis sort:\n",a)
