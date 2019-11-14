def combo(a,b):
    # find start columnn
    next_num = a[-1]
    
    # find next combo
    for i in range(len(b)-1,-1,-1):
        
        #find next up
        j = len(a)-1
        while(a[j] > b[i]):
            # compare right column of b array to every a element
            if b[i] < a[j]:
                next_num = a[j]
              
        #up number
        if b[i] < next_num:
            b[i] = next_num
        
        next_smallest = a[0];
        #find lowest possible combo for each element
        for k in range(i+1,len(b)-1,1):
            # find smallest number possible
            for m in range(len(a)):
                if a[m] < next_smallest:
                    next_smallest = a[m]
            b[k] = next_smallest
        
    return b
    

a = [1,2,3,4,5,6]
b =[2,4,6]
print(combo(a,b))
    