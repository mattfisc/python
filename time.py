import time


big_list = []
top = 2**10
for i in range(top):
    big_list.append(i)

st = time.time()
linear(big_list,top-1)
print(time.time()-st)

