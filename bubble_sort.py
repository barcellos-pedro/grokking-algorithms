def bubble_sort(arr):
    """ O(n^2)"""
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    return arr


print(bubble_sort([4, 1, 3]))
print(bubble_sort([300, 400, 100, 200]))
