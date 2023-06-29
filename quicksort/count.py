# Example of count function to understand recursion

def countLoop(items):
    count = 0
    for _ in range(len(items)):
        count += 1
    return count


def count(items, initial_value=0):
    if len(items) == 0:
        return 0
    if len(items) == 1:
        return initial_value + 1

    items.pop()
    initial_value += 1
    return count(items, initial_value)


print(count([1, 2, 3]))
print(count([1, 2]))
print(count([1]))
print(count([]))
