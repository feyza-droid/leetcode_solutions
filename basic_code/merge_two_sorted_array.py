def merge(L1, L2):
    R = []
    
    a = 0
    b = 0

    while(a < len(L1) and b < len(L2)):
        if L1[a] < L2[b]: # L1 is min
            R.append(L1[a])
            a += 1
        else: # L2 is min
            R.append(L2[b])
            b += 1

    while(a < len(L1)):
        R.append(L1[a])
        a += 1

    while(b < len(L2)):
        R.append(L2[b])
        b += 1

    return R


L1 = [14,31,43,65]
L2 = [15,37,40,42]
R = merge(L1,L2)
print(f"sorted list {R}")