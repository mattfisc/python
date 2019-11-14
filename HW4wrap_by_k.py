def wrap_by_k(a,k):
    
    for i in range(k):
        temp = a[len(a)-1]
        for j in range(len(a)-1,0,-1):
            a[j] = a[j-1]  
        a[0] = temp

    return a

a = [1,2,3,4,5,6,7,8]

print(wrap_by_k(a,3))

#PS C:\Users\Matthew Fischer\Documents\HtmlcssJS\Homepage> & C:/Python27/#python.exe c:/Python27/cs240/wrap_by_k.py
#[6, 7, 8, 1, 2, 3, 4, 5]
#PS C:\Users\Matthew Fischer\Documents\HtmlcssJS\Homepage>
