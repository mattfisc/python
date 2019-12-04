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




def distance(first,second):

    # max distance rough
    delta = 30
    closestPair = []

    for i in range(len(a)-1):
        for j in range(i+1,len(a)):

            firstX = first[0]
            firstY = first[1]

            secondX = second[0]
            secondY = second[1]

            check = math.sqrt((secondY - firstY)**2 + (secondX - secondY)**2)

            if check < delta:
                # new closest pair
                closestPair = [] # erase old

                # add new pair
                closestPair.append(first) 
                closestPair.append(second)
                delta = check

                print("distance",delta)
    return delta
def closestPair(px1,px2,py1,py2):
    
    lx = px1[:len(px1)//2]
    rx = px1[len(px2)//2:]
    ly = py1[:len(py1)//2]
    ry = py2[len(py1)//2]

    #median is the largest left side
    median = lx[-1]

    #base case if less than 3
    if lx < 3:
        return lx[0],lx[1]
    elif ly < 3:
        return ly[0], ly[1]
    elif rx < 3:
        return rx[0],rx[1]
    elif ry < 3:
        return ry[0],ry[1]

    # all other cases
    else:
        bestL = closestPair(lx,ly)
        bestR = closestPair(rx,ry)
        bestS = closestSplitPair(px,py)
        
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


# make list of points
a = make_list_points()

# sort list by x
px = a.sort

# sort list by y
py = sortY(a)

# find closest point
best = closestPair(px,px,py,py)

#print("Non sorted list: \n",a)

# sort x axis
#a.sort()
##print("x axis sort:\n",a)

#sortY(a)
#print("y axis sort:\n",a)
