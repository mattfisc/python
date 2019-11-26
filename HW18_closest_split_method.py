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
def split_pair(a):

    a.sort()

    middleI = 0
    for i in range(len(a)):
        if a[i][0] < 0:
            middleI = i
        else:
            break

    firstX=a[:middleI]
    secondX=a[middleI:]

    delta = 1.1

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


a = make_list_points()
middle = 0
split_pair(a)

print("Non sorted list: \n",a)

# sort x axis
a.sort()
print("x axis sort:\n",a)

sortY(a)
print("y axis sort:\n",a)

