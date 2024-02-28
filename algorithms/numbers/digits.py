def get_digit(n: int, position: int) -> int:
    """
    Gets the digit at a specified position in a given integer.

    Parameters:
        n (int): The integer from which to extract the digit.
        position (int): The position of the digit to retrieve.

    Returns:
        int: The digit at the specified position.

    Raises:
        ValueError: If position is a negative number.
    """
    if position < 0:
        raise ValueError('Position must be a non-negative number')
    nn = abs(n) if n < 0 else n

    return (nn // 10 ** position) % 10


def sum_digits(n: int) -> int:
    """
    Calculates the sum of all digits of a number.

    Parameters:
        n (int): The integer for which sum of digits is to be calculated.

    Returns:
        int: The sum of all digits of the number.
    """

    if n == 0:
        return 0
    nn = abs(n) if n < 0 else n
    sum_ = 0
    while nn > 0:
        remainder = nn % 10
        sum_ += remainder
        nn //= 10
    return sum_


def move_zeroes(nums: list[int]) -> list[int]:
    """
    Moves all zeros to the end, maintaining the order of other elements.

    Parameters:
        nums (list[int]): List of integers.

    Returns:
        list[int]: The input list with zeroes at the end.
    """

    index = 0
    for num in nums:
        if num != 0:
            nums[index] = num
            index += 1
    while index < len(nums):
        nums[index] = 0
        index += 1
    return nums
