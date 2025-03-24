def inters(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    return list(s1 & s2)  # return list(s1.intersection(s2))

l1 = [45, 5, 22, 31, 7, 19]
l2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]
print(inters(l1, l2))