def move_zeros(l):
    zero_idx = 0
    for i in range(len(l)):
        n = l[i]
        if n != 0:
            l[zero_idx] = n
            if zero_idx != i:
                l[i] = 0
            zero_idx = zero_idx + 1
    return l

l = [99, 0, -7, 0, 16]
move_zeros(l)
print(l)