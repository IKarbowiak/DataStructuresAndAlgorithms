def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return [None, None]
    sorted_input = mergesort(input_list)
    first_number = ""
    second_number = ""

    odd = len(sorted_input) % 2 == 1
    start_index = 0
    if odd:
        first_number = str(sorted_input[0])
        start_index = 1

    for index, num in enumerate(sorted_input[start_index:]):
        if index % 2 == 0:
            first_number += str(num)
        else:
            second_number += str(num)

    second_number = 0 if not second_number else int(second_number)
    first_number = int(first_number)
    return [first_number, second_number]


def mergesort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


print(rearrange_digits([1, 2, 3, 4, 5]))
# should return [542, 31]

print(rearrange_digits([4, 6, 2, 5, 9, 8]))
# should return [964, 852]

print(rearrange_digits([4, 8]))
# should return [8, 4]

print(rearrange_digits([4, 8, 1]))
# should return [84, 1]

print(rearrange_digits([4, 8, 1, 2]))
# should return [82, 41]

print(rearrange_digits([4]))
# should return [4, 0]

print(rearrange_digits([]))
# should return [None, None]
