def binary(num):
    s = ""
    while(num > 0):
        s =  num%2 
        num = num / 2
    
    return binary

number = 5
print(binary(number))