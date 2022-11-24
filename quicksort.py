# quicksort
import math
arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]
# arr = [10, 5, 8, 3, 9, 6, 12]


def partition(l, h):
    mid = int(math.ceil((l+h)/2))
    pivot = arr[mid]
    i = l
    j = h
    while i < j:
        while arr[i] <= pivot:
            i += 1
            if i > h:
                break
        while arr[j] > pivot:
            j -= 1
            if j < l:
                break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[j] < pivot:
        arr[mid], arr[j] = arr[j], arr[mid]
    return j


def quicksort(l, h):
    if l < h:
        j = partition(l, h)
        quicksort(l, (j-1))
        quicksort((j+1), h)


quicksort(0, (len(arr)-1))
print(arr)
