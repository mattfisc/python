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

    firstX=a[:len(a)//2]
    secondX=a[len(a)//2:]

    delta = 1.1


    



a = make_list_points()

split_pair(a)





print("Non sorted list: \n",a)

# sort x axis
a.sort()
print("x axis sort:\n",a)

sortY(a)
print("y axis sort:\n",a)


