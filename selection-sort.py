def selection_sort(items):
    """ O(n^2) """
    items_sorted = []

    for _ in range(len(items)):
        minor = items[0]
        minor_index = 0
        for j in range(1, len(items)):
            if items[j] < minor:
                minor = items[j]
                minor_index = j
        items_sorted.append(items.pop(minor_index))

    return items_sorted


print(selection_sort([5, 3, 6, 2, 10]))
