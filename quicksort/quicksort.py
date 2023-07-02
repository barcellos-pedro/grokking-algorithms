def quicksort(items):
    if len(items) < 2:  # [] || [1]
        return items
    if len(items) == 2:  # [2, 1]
        a, b = items
        return [a, b] if a < b else [b, a]

    pivot = items.pop()
    left = []  # minor than pivot
    right = []  # higher than pivot

    for value in items:
        if value <= pivot:
            left.append(value)
        else:
            right.append(value)

    # Return joined lists
    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([]))
print(quicksort([2]))
print(quicksort([100, 1]))
print(quicksort([14, 9, 3, 1, 99]))
print(quicksort([5, 3, 6, 2, 10]))
