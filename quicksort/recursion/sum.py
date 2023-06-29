# Example of sum function to understand recursion

def sumLoop(items):
    """Using for loops"""
    result = 0
    for value in items:
        result += value
    return result


def sum(items):
    """Using for recursion"""
    if len(items) == 0:
        return 0
    if len(items) == 1:
        return items[0]

    first = items.pop(0)
    return first + sum(items)


print("Using for loops")
print(sumLoop([1, 2, 3]))
print(sumLoop([2, 4, 6]))
print(sum([1]))
print(sum([]))

print("Using for recursion")
print(sum([1, 2, 3]))
print(sum([2, 4, 6]))
print(sum([1]))
print(sum([]))
