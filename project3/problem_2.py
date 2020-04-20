def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1
    start = 0
    end = len(input_list) - 1
    first_value = input_list[0]
    last_value = input_list[-1]
    while start <= end:
        middle = (start + end) // 2
        middle_value = input_list[middle]
        if middle_value == number:
            return middle
        if middle_value > number:
            if first_value <= number or first_value > middle_value:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if last_value < number and first_value > middle_value:
                end = middle - 1
            else:
                start = middle + 1
    return -1


print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
# should return 0

print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
# should return 5

print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8))
# should return 2

print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1))
# should return 3

print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10))
# should return -1

print(rotated_array_search([], 5))
# should return -1

print(rotated_array_search([3], 3))
# should return 0

print(rotated_array_search([3], 5))
# should return -1

print(rotated_array_search([5, 6, 8, 10, -5, -2, 0, 3], -2))
# should return 5
