
def coeffient(n , k): 
  
    # termination 
    if k==0 or k ==n : 
        return 1
  
    # recursive call
    return coeffient(n-1 , k-1) + coeffient(n-1 , k) 
  

n = 6
k = 2
print "Value of C(%d,%d) is (%d)" %(n , k , coeffient(n , k)) 

# ----- OUTPUT --------
# Value of C(6,2) is (15)
