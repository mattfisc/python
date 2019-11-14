
def singlePermutations(a):
 
    #move one bit
    i = len(a)-1
    while(True):
        if a[i] == 1 and a[i-1] == 0:
            a[i],a[i-1] = a[i-1],a[i]
            i+=1
            print(a)
        # exit
        if a[0] == 1 and a[1] == 1 and a[2] == 1:
            break;

def doublePermutaions(a):
    for i in range(len(a)-1,-1,-1):
        if a[i] == 1 and a[i-1] == 1 and a[i-2] == 0:
            a[i-2],a[i-1] = a[i-1],a[i-2]
            a[i],a[i-1] = a[i-1],a[i]
            print(a)
def triplePermutations(a):
    for i in range(len(a)-1,-1,-1):
        if a[i] == 1 and a[i-1] == 1 and a[i-2] == 1 and a[i-3] == 0:
            a[i] = 0
            a[i-3],a[i-2],a[i-1] = 1
            print(a)

def allPermutations(a):
    print(a)
    singlePermutations(a)
    doublePermutaions(a)
    triplePermutations(a)
    
b=[0,0,0,0,0,1,1,1]

print(allPermutations(b));

# does not work
# i don't know how recursively and this was 
# the only thing I could try to do