# Heap sort
# min heap
import math
arr = [10, 20, 15, 40, 30, 1, 60, 40, 2]
parent = 0
for i in range(2, len(arr)+1):
    for j in range(math.ceil(math.log2(len(arr)))):
        parent = math.floor(i / 2)
        if parent < 1:
            break
        if arr[i-1] < arr[parent-1]:
            arr[i-1], arr[parent-1] = arr[parent-1], arr[i-1]
            i = parent
        else:
            break
print(arr)
