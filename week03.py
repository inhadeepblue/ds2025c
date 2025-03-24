def inters(l1, l2):
    l3 = list()
    for v in l1:
        if v in l2:
            l3.append(v)
    return l3

l1 = [45, 5, 22, 31, 7, 19]
l2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]
print(inters(l1, l2))