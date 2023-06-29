def binary_search(items, target):
    min = 0
    max = len(items) - 1

    while min <= max:
        middle = int((min + max) / 2)
        value = items[middle]

        if value == target:
            return middle
        elif value > target:
            max = middle - 1
        else:
            min = middle + 1

    return None


print(binary_search([1, 2, 3, 4, 5, 6], 2))
print(binary_search([1, 2, 3, 4, 5, 6], 4))
print(binary_search([1, 2, 3, 4, 5, 6], 6))
print(binary_search([1, 2, 3, 4, 5, 6], -1))
