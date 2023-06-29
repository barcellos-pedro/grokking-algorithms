def binary_search(items, target, min=0, max=0):
    if len(items) == 0:
        return None
    if len(items) == 1:
        return 0 if items[0] == target else None

    if max == 0:
        max = len(items) - 1

    middle = int((min + max) / 2)
    value = items[middle]

    if value == target:
        return middle
    elif value > target:
        max = middle - 1
    else:
        min = middle + 1

    return None if min > max else binary_search(items, target, min, max)


print(binary_search([1, 2, 3, 4, 5, 6], 1))
print(binary_search([1, 2, 3, 4, 5, 6], 3))
print(binary_search([1, 2, 3, 4, 5, 6], 6))
print(binary_search([1, 2, 3, 4, 5, 6], -1))
print(binary_search([3], 3))
print(binary_search([], 1))
