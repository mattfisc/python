import math
import random

# sort by y point
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
    x = round(random.uniform(0,10),2)
    y = round(random.uniform(0,10),2)
    
    point = (x,y)

    return point


def make_list_points():
    a = []

    # list of 64 random points
    for i in range(64):
        a.append(make_point())

    return a

def closestPair(px,py):
    
    lx = px[:len(px)//2]
    rx = px[len(px)//2:]

    ly = py[:len(py)//2]
    ry = py[len(py)//2:]

    
    #base case if less than 3
    if len(px) <= 3:
        #brute force compare
        distance = distance(px[0],px[1])
        sD = distance(px[1],px[2])

        #return closest pair and distance
        if distance > sD:
            #second pair
            return px[1],px[2],sD
        #first pair
        return px[0],px[1],distance

        
    # all other cases
    else:
        bestL,dl = closestPair(lx,ly)
        bestR,dr = closestPair(rx,ry)
        bestS,ds = closestSplitPair(px,py)
        
def closestSplitPair(lx,ly,rx,ry):
    sy = ly + ry
    q = sortY(sy)

    # worst case senario
    best = 30
    bestPair = []
    for i in range(len(sy)-1):
        for j in range(7):

            # check distance
            d = distance(q[i],q[i+j])

            if d < best:
                best = d
                print("best split list",best)
                bestPair = []
                bestPair.append(q[i])
                bestPair.append(q[i+j])
    return bestPair

# distance of two tuples
def distance(first,second):

    firstX = first[0]
    firstY = first[1]

    secondX = second[0]
    secondY = second[1]

    check = math.sqrt((secondY - firstY)**2 + (secondX - secondY)**2)

    
    return check


# make list of points
a = make_list_points()

# sort list by x
px = a.sort

# sort list by y
py = sortY(a)

# find closest point
best = closestPair(px,py)

#print("Non sorted list: \n",a)

# sort x axis
#a.sort()
##print("x axis sort:\n",a)

#sortY(a)
#print("y axis sort:\n",a)
