def compare(a,b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return "A is greater"
        elif b[i] > a[i]:
            return "B is greater"
    return "A is equal to B"

a = [1,0,0,0]
b = [1,0,0,1]

print(compare(a,b))

# --- OUTPUT ------
# B is greater