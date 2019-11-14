# print all permutations recursively


def permutations(lst):

    
    if len(lst) == 1:
        return lst
    list1 = []

    for i in range(len(lst)):
        m = lst[i]
        small_lst = lst[:i] + lst[i+1:]

        for p in permutations(small_lst):
            # print([m],[p])

            list1.append([m] + [p])

            # list1.extend([p]+m)

    return list1


# calling permutations
list4 = [1,1,1,0,0,0,0,0]
print(list4)
for i in range(24):
    print(permutations(list4)[i])
