import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None, None

    min_value = ints[0]
    max_value = ints[0]
    for i in ints[1:]:
        if i < min_value:
            min_value = i
        if i > max_value:
            max_value = i
    return min_value, max_value


l1 = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l1)
print(get_min_max(l1))
# should return (0, 9)

l2 = [i for i in range(-20, 20)]  # a list containing 0 - 9
random.shuffle(l2)
print(get_min_max(l2))
# should return (-20, 19)

l3 = []
print(get_min_max(l3))
# should return (None, None)

l4 = [-1]
print(get_min_max(l4))
# should return (-1, -1)

l5 = [1, 1]
print(get_min_max(l5))
# should return (1, 1)

l6 = [-3, 10]
print(get_min_max(l6))
# should return (-3, 10)
