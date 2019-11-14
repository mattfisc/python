# Matthew Fischer
# Project 1

nums = [1,2,3,4,5]

frontProduct = [0,0,0,0,0]
backProduct = [0,0,0,0,0]

# array frontward product
for i in range(0,len(nums)):
    sum = 1
    for j in range(0,i+1):
        sum *= nums[j]
    frontProduct[i] = sum

# array backward product
for i in range(len(nums)-1,-1,-1):
    sum = 1
    for j in range(len(nums)-1,i-1,-1):
        sum *= nums[j]
    backProduct[i] = sum 
   
# new array of products
productArr = [1,1,1,1,1]
for i in range(0,len(productArr)):
    #left marker
    if i > 0:
        productArr[i] *= frontProduct[i-1]
    # right marker
    if i < 4:
        productArr[i] *= backProduct[i+1]

print(frontProduct)
print(backProduct)
print("Product except position")
print(productArr)

#------OutPut--------
#PS C:\Users\Matthew Fischer\Documents\Python\Python> & C:/Python27/python.exe "c:/Users/Matthew Fischer/Documents/Python/CS240/Program#1.py"
#Product except position
#[120, 60, 40, 30, 24]
#PS C:\Users\Matthew Fischer\Documents\Python\Python>
#--------------------