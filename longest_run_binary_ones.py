def binary(num):
    binary = ""
    while(num > 0):
        binary = num%2 + binary
        num = num / 2
    
    return binary

print(binary(4))