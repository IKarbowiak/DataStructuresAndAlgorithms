def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None

    if number == 0 or number == 1:
        return number

    start = 1
    end = number
    previous = 0
    while start < end:
        middle = (start + end) // 2
        middle_square = middle ** 2

        if middle_square == number:
            return middle

        if middle_square > number:
            end = middle - 1
        else:
            start = middle + 1
        previous = middle

    return previous


print(sqrt(9))
# should return 3

print(sqrt(0))
# should return 0

print(sqrt(16))
# should return 4

print(sqrt(1))
# should return 1

print(sqrt(27))
# should return 5

print(sqrt(-5))
# should return None

print(sqrt(100000000000000000000000000000000000000000000000000000))
# should return 316227766016837933199889354
