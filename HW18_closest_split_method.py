import math
import random

# sort by y point
def sortY(tup):  
      
    # getting length of list of tuples 
    lst = len(tup)  
    temp = 0
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
    for i in range(15):
        a.append(make_point())

    return a

def closestPair(Px,Py):
    delta = 0

    m = len(Px)//2
    lx = Px[:m]
    rx = Px[m:]

    ly = Py[:m]
    ry = Py[m:]

    
    #base case if less than 3
    if len(Px) <= 3:
        #brute force compare
        distance = distance(Px[0],Px[1])
        sD = distance(Px[1],Px[2])

        #return closest pair and distance
        if distance > sD:
            #second pair
            return Px[1],Px[2],sD

        #first pair
        return Px[0],Px[1],distance

        
    # all other cases
    else:
        bestL,dl = closestPair(lx,ly)
        bestR,dr = closestPair(rx,ry)
        if dl < dr:
            delta = dl
        else:
            delta = dr
        bestS,ds = closestSplitPair(Px,Py,delta)
    return bestS,ds
        
def closestSplitPair(px,py,delta):
    
    median = len(px)//2
    low = median - delta
    high = median + delta

    sy = []
    for i in range(len(px)):
        if px[i][0] > low and px[i][0] < high:
            sy.append(px[i])

    # worst case senario
    best = 30
    bestPair = []
    for i in range(len(sy)-2):
        for j in range(i+1,min(7,len(sy)-i)):

            # check distance
            d = distance(sy[i],sy[i+j])

            if d < best:
                best = d
                print("best split list",best)
                bestPair = []
                bestPair.append(sy[i])
                bestPair.append(sy[i+j])
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
print(a)
# sort list by y
py = sortY(a)

# find closest point
bestPair,distance = closestPair(px,py)
print("The best pair and distance is: ",bestPair,distance)
#print("Non sorted list: \n",a)

# sort x axis
#a.sort()
##print("x axis sort:\n",a)

#sortY(a)
#print("y axis sort:\n",a)
