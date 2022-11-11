# 2-way merge sort
import math
list_A = [9, 3, 7, 5, 6, 4, 8, 2]

def merge(a, b):
    i = 0
    j = 0
    m = len(a)
    n = len(b)
    c = []
    while (i < m) and (j < n):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < m:
        c.append(a[i])
        i += 1
    while j < n:
        c.append(b[j])
        j += 1
    return c


n = len(list_A)
step_num = math.ceil(math.log2(n))
i = 2
for j in range(step_num):  # time taken : logn
    h = int(i/2)
    l = 0
    for k in range(int(n/i)):    # time taken : n/i
        list_B = merge(list_A[l:h], list_A[h:l+i])    # time taken : i
        list_B.extend(list_A[0:l])       # time taken : 1
        list_B.extend(list_A[(l+i):])   # time taken : 1
        list_A = list_B.copy()   # time taken : 1
        print(list_A)
        l += i
        h += i
    i *= 2

# total time : logn*n/i*i+3 = nlogn





