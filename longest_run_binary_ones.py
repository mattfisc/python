def binary(num):
    string = ""
    while(num > 0):
        string = num%2 + string
        num = num / 2
    
    return binary

number = 5
print(binary(number))