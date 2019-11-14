def binary_to_decimal(x):
    num = 0
    twoPower = 1

    for i in range(len(x)-1,-1,-1):
        num += x[i] * (2**twoPower)
        twoPower += 1
    return num

def compare_two_binary(binary1,binary2):
    b1 = binary_to_decimal(binary1)
    b2 = binary_to_decimal(binary2)
    if b1 > b2:
        return binary1, " Is greater"
    elif b2 > b1:
        return binary2, " Is greater"
    else:
        binary1, " Is equal ", binary2


arr = [1,0,1]
arr2 = [1,1,1]
print(binary_to_decimal(arr))
print(compare_two_binary(arr,arr2))


# ------ OUTPUT --------
#    10
# ([1, 1, 1], ' Is greater')