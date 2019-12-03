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
    x = round(random.randrange(-10,10),2)
    y = round(random.randrange(-10,10),2)
    
    point = (x,y)

    return point


def make_list_points():
    a = []
    for i in range(50):
        a.append(make_point())

    return a



# find closest from delta
def closest_point(a):
    # sort x
    a.sort()

    middleI = 0
    for i in range(len(a)):
        if a[i][0] < 0:
            middleI = i
        else:
            break

    firstX=a[:middleI]
    secondX=a[middleI:]

    # closest left
    closeL = bruteForce(firstX)
    # closest right
    closeR = bruteForce(secondX)
    
    # closest distance by d
    d = 0

    if closeL < closeR:
        d = closeL
    else:
        d = closeR

    # closest cross
    return closest_cross(firstX,secondX,d)

def closest_cross(firstX,secondX,delta):
    
    #left of delta
    leftD =[]
    i = len(firstX)
    #reversed loop
    while(True):
        if a[i][0] > -delta:
            leftD.append(a[i])
            i-=1
        else:
            break
    
    #right of delta
    rightD = []
    i = len(secondX)
    while(True):
        if a[i][0] < delta:
            rightD.append(a[i])
            i+=1
        else:
            break

    #sort deltas by y cordinate
    sortY(leftD)
    sortY(rightD)

    print("left d: ",leftD)
    print("right d:",rightD)

def bruteForce(a):

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
    return closest

a = make_list_points()
closest = closestL_R(a)

print("Non sorted list: \n",a)

# sort x axis
a.sort()
print("x axis sort:\n",a)

sortY(a)
print("y axis sort:\n",a)

