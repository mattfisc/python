def largest_in_array(arr):
    large = arr[0]
    for i in range(len(arr)):
        if arr[i] > large:
            large = arr[i]
    
    for i in range(len(arr)):
        arr[i] = large
    return arr

def middle_of_array(arr1, arr2):
    if len(arr1)/2 == 0 or len(arr2)/2 == 0:
        return
    middle = [0,0]

    middle[0] = arr1[len(arr1)/2]
    middle[1] = arr2[len(arr2)/2]

    return middle

def double_array_save_last_value(arr):
    if len(arr) < 1:
        return
    
    length  = len(arr) *2
    new_arr = [0] * length

    new_arr[len(new_arr)-1] = arr[len(arr)-1]

    return new_arr
    
def two_array_to_one(a,b):
    ab = [0] * 4
    for i in range(len(ab)):
        if i < 2:
            ab[i] = a[i%2]
        else:
            ab[i] = b[i%2]
    return ab

def odd_array_return_middle_three(a):
    # exception even length or arrays less than 3
    if len(a) / 2 == 0 or len(a) < 3:
        return
    
    index = len(a)/2-1
    b = [0] * 3

    for i in range(3):
        b[i] = a[index]
        index+=1
    return b

def arr_max_first_last_middle(a):
    if len(a) / 2 == 0 and len(a) < 1:
        return
    maxN = 0

    for i in range(0,len(a),len(a)/2):
        if a[i] > maxN:
            maxN = a[i]
    return maxN

#8 problem////
def evenNums(a):
    count = 0
    
    for i in range(len(a)):
        if a[i] % 2 == 0:
            count+=1
    return count

#9
def big_little_dif(a):
    big = a[0] 
    little = a[0]

    for i in range(len(a)):
        if big < a[i]:
            big = a[i]
        if little > a[i]:
            little = a[i]
        
    return(big-little)

#10
def average(a):

    big = -999
    little = 999
    average = 0
    count  = -2 # ignore high and low

    for i in range(len(a)):
        if big < a[i]:
            big = a[i]
        if little > a[i]:
            little = a[i]
        
        average += a[i]
        count+=1

    average = (average - big -little)/count
    return average

#11
def count_array_except_67(a):
    sum = 0
    to_count = True

    for i in range(len(a)):
        if to_count:
            if a[i] != 6:
                sum += a[i]
            else:
                to_count = False
        else:
            if a[i] == 7:
                to_count = True
    return sum

#12
def double_two_tf(a):
    is_two = False

    for i in range(len(a)):
        if a[i] == 2:
            if is_two == True:
                return True
            
            is_two = True
        else:
            is_two = False
    return False
        

# 13
def equal_split_sum(a):
    sum = 0
    half = 0
    # array not empty
    if len(a) < 1:
        return False
    
    for i in range(len(a)):
        sum += a[i]
    half = sum/2

    if sum % 2 != 0:
        return False

    sum = 0
    for i in range(len(a)):
        sum+= a[i]
        if sum == half:
            return True

    return False


#14
def countClumps(a):
    count = 0
    double = False
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            if double == False:
                count+=1
            double = True
        else:
            double = False
    return count
            
a =[1,1,1,1,1,144,4,4,3,12]

print(countClumps(a))

