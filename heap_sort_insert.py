# Heap sort
# insert
import math


# insert process
def insert_element(element, array, length_array):
    array.append(element)
    length_array += 1
    parent = math.floor(length_array/2)
    i = length_array
    for k in range(math.ceil(math.log2(length_array))):
        print(k, parent)
        if parent < 1:
            break
        if array[i-1] > array[parent-1]:
            array[i-1], array[parent-1] = array[parent-1], array[i-1]
            i = parent
            parent = math.floor(parent/2)
        else:
            break
    return [array, length_array]


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
    arr, length = insert_element(100, arr, length)
    print(arr)


if __name__ == "__main__":
    main()

