#Homework 5

import time
import random

def bubbleSort(a):
    temp = 0
    count = 0
    i = 0

    while i < len(a)-1:
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            i = 0
        else:
            i += 1

        # count number of loops taken
        print(count,"passes")
        count +=1
        #print(a)
        
    return a



print("------Output-----------")
print("array of 2000 \n time to bubble sort")

A = [3,7,1,8,5,6,2]
B =[random.randint(0,10) for i in range(20)]
st = time.time()
bubbleSort(B)

print(time.time()-st)
print(bubbleSort(A))
#PS C:\Python27\cs240> & C:/Python27/python.exe "c:/Users/Matthew Fischer/Documents/HtmlcssJS/Homepage/#bubbleSort.py"
#------Output-----------
#array of 1000 /n time to bubble sort
#32.4270000458
#PS C:\Python27\cs240> & C:/Python27/python.exe "c:/Users/Matthew Fischer/Documents/HtmlcssJS/Homepage/bubbleSort.py"
#------Output-----------
#array of 2000
#time to bubble sort
#237.10800004
#PS C:\Python27\cs240> & C:/Python27/python.exe "c:/Users/Matthew Fischer/Documents/HtmlcssJS/Homepage/#bubbleSort.py"
#------Output-----------
#array of 2000
