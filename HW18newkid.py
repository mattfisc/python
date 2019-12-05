# new kid on the block
import math

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

# distance of two tuples
def distance(first,second):

    firstX = first[0]
    firstY = first[1]

    secondX = second[0]
    secondY = second[1]

    check = math.sqrt((secondY - firstY)**2 + (secondX - secondY)**2)

    return check

def closestSplitPair(p,newPoint,delta):
    bestPair=[]
    median = newPoint[0]
    low = median - delta
    high = median + delta

    # add x axis away from new point
    sy = []
    sy.append(newPoint)

    for i in range(len(p)):
        if p[i][0] > low and p[i][0] < high:
            sy.append(p[i])

    # add y axis away from new point
    median = len(p)//2
    low = median - delta
    high = median + delta

    sortY(p)

    median = newPoint[1]
    print("\n",sy,"\n")
    for i in range(len(p)):
        if p[i][1] > low and p[i][1] < high:
            sy.append(p[i])

    print(sy, "finished sy\n")
    
    for i in range(len(sy)-2):
        for j in range(i+1,min(7,len(sy)-i)):

            # check distance
            d = distance(sy[i],sy[i+j])

            if d < delta:
                delta = d
                print("best split list",delta,sy[i],sy[i+j])
                bestPair = []
                bestPair.append(sy[i])
                bestPair.append(sy[i+j])
    return bestPair

newPoint = (6.02, 2.02)
A= [(6.52, 5.59), (3.78, 1.55), (4.59, 2.49), (6.53, 1.81), (9.08, 7.26), (3.21, 0.37), (2.07, 0.65), (7.53, 1.98), (8.95, 0.5), (5.72, 3.84), (0.77, 3.65), (1.52, 0.32), (7.23, 8.41), (0.26, 8.83)]


delta = 1.2

new_distance = closestSplitPair(A,newPoint,delta)
if new_distance == []:
    print("new kid on the block is not closer")
else:
    print("the new kid is closer: ", new_distance)

#not working

#output
#new kid on the block is not closer