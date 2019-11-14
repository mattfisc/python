def add_one_binary(a):
    for i in range(len(a)-1,-1,-1):
        if a[i] == 0:
            a[i] = 1
            for j in range(i+1,len(a),1):
                a[j] = 0
            break
   
    return a


a=[0,1,1,1];
print(add_one_binary(a))

# OUTPUT
# [1, 0, 0, 0]