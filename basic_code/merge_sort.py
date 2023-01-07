# Merge Sort Runtime: 0(nlog(n)) average and worst case. Memory: Depends. 
# The space complexity of merge sort here is 0(n) due to the auxiliary space used to merge parts of the array.

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

def merge_sort(L):
    N = len(L)

    if N == 1: return L 
    
    mid = int(N/2)
    R = merge(merge_sort(L[0:mid]), merge_sort(L[mid:N]))
    return R

L = [14,31,43,15,37,40,42,54,11,43]
R = merge_sort(L)
print(f"sorted list {R}")