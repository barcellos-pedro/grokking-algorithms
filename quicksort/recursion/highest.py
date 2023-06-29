def highest_num(items, highest=0):
    if len(items) == 0:
        return 0
    if len(items) == 1:
        value = items[0]
        return value if value > highest else highest

    value = items.pop(0)

    if value > highest:
        return highest_num(items, value)

    return highest_num(items, highest)


print(highest_num([1, 2, 3]))
print(highest_num([2, 10, 6]))
print(highest_num([99, 10, 6]))
print(highest_num([1]))
print(highest_num([]))
