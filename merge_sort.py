# merge sort
# recursive method
list_A = [9, 3, 7, 5, 6, 4, 10, 2, 8, 1]


def mergesort(l, h):
    if l < h:
        mid = int((l+h)/2)
        list1 = mergesort(l, mid)
        list2 = mergesort(mid+1, h)
        return merge(list1, list2)
    elif l == h:
        return [list_A[l]]


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


list_A = mergesort(0, len(list_A)-1).copy()
print(list_A)
