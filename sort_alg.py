def find_smallest(arr):
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return arr.index(smallest)


def selectionSort(arr):
    new_arr = []
    [new_arr.append(arr.pop(find_smallest(arr))) for x in range(len(arr))]
    return new_arr


print(selectionSort([5, 3, 6, 2, 10]))
# time 9.724000000000051e-06
# O(n2)
