# heapify

import math
arr = [10, 20, 15, 12, 40, 25, 18]
parent = len(arr)
length = len(arr)
for i in range(length):
    if 2*parent+1 <= length:
        if arr[2*parent-1] > arr[2*parent] and arr[2*parent-1] > arr[parent-1]:
            arr[2*parent-1], arr[parent-1] = arr[parent-1], arr[2*parent-1]
        elif arr[2*parent] >= arr[2*parent-1] and arr[2*parent] > arr[parent-1]:
            arr[2 * parent], arr[parent - 1] = arr[parent - 1], arr[2 * parent]
    elif 2*parent <= length:
        if arr[2*parent-1] > arr[2*parent] and arr[2*parent-1] > arr[parent-1]:
            arr[2*parent-1], arr[parent-1] = arr[parent-1], arr[2*parent-1]
    parent -= 1
print(arr)
