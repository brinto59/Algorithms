# Heap sort
# delete max element
import math


# delete process
def max_element(array, length_array):
    array[0], array[length_array-1] = array[length_array-1], array[0]
    length_array -= 1
    parent = 1
    if length_array < 1:
        return [array[length_array], length_array, array]
    for k in range(math.ceil(math.log2(length_array))):
        if 2*parent+1 <= length_array:
            if array[2*parent-1] > array[2*parent] and array[2*parent-1] > array[parent-1]:
                array[2*parent-1], array[parent-1] = array[parent-1], array[2*parent - 1]
                parent *= 2
            elif array[2*parent] >= array[2*parent-1] and array[2*parent] > array[parent-1]:
                array[2 * parent], array[parent - 1] = array[parent - 1], array[2 * parent]
                parent = 2*parent + 1
        elif 2*parent <= length_array:
            if array[2*parent-1] > array[parent-1]:
                array[2*parent-1], array[parent-1] = array[parent-1], array[2*parent - 1]
                parent = 2*parent
        else:
            break
    return [array[length_array], length_array, array]


def main():
    arr = [10, 20, 15, 40, 30, 1, 60, 40, 2]
    parent = 0
    length = len(arr)
    for i in range(2, len(arr) + 1):
        for j in range(math.ceil(math.log2(len(arr)))):
            parent = math.floor(i / 2)
            if parent < 1:
                break
            if arr[i - 1] > arr[parent - 1]:
                arr[i - 1], arr[parent - 1] = arr[parent - 1], arr[i - 1]
                i = parent
            else:
                break
    print(arr)
    maximum, length, arr = max_element(arr, length)
    print(maximum)
    print(arr)
    print(length)
    maximum, length, arr = max_element(arr, length)
    print(maximum)
    maximum, length, arr = max_element(arr, length)
    print(maximum)
    maximum, length, arr = max_element(arr, length)
    print(maximum)
    maximum, length, arr = max_element(arr, length)
    print(maximum)


if __name__ == "__main__":
    main()

