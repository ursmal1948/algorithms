import re
from typing import Type


# from randomm import rand_number


# DEcimal number precision.
# Do algorytmow mozna jeszcze dodac is_fibonacci
def does_number_match_regex(
        n: int,
        data_type: Type[int | float],
        regex: str | None = None) \
        -> int | float:
    """
    Checks if n matches a specified regular expression pattern based on
    its data type.

    Parameters:
        n (int | float): The number to be checked.
        data_type (Type[int | float]): The type of the number (int or float).
        regex (str, optional): Regular expression pattern to match against.
            If not provided, a default pattern based on the data type will be used.

    Returns:
        int | float: True if number matches the specified regular expression
         pattern, otherwise False.

    Raises:
        TypeError: If data_type is not int or float.
    """

    if data_type not in [int, float]:
        raise TypeError('Incorrect type')

    data_type_regex = {
        int: r'^-?\d+(\.0+)?$',
        float: r'^-?\d+\.\d+$'
    }

    data_regex = regex if regex else data_type_regex[data_type]
    if not re.match(data_regex, str(n)):
        return False
    return True


def does_string_match_regex(text: str, pattern: str = r'^[A-Z][a-z]+$') -> bool:
    """
    Checks if a string matches a specified regular expression pattern.

    Parameters:
        text (str): The string to be checked.
        pattern (str, optional): Regular expression pattern to match against.
            The default pattern checks if the string follows a specific naming convention where
            the first letter is capitalized and the rest are lowercase.

    Returns:
        bool: True if the string matches the specified regular expression pattern, otherwise False.
    """
    return True if re.match(pattern, text) else False


# co zrobilam
# Number matches regex, -> is_float, is_integer,
# String matches regex.

# Co do zrobienia
# todo Password validation, . NUmeric range validation.If a char falls withhin a specific range.

def does_char_fall_within_range(char: str, min_char: str, max_char: str) -> bool:
    if len(char) != 1:
        raise ValueError('Char must consist of one letter')
    if ord(min_char) > ord(max_char):
        raise ValueError('The range is not correct')
    return min_char <= char <= max_char
