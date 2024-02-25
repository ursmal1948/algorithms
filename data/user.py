import re


def get_str(message: str) -> str:
    """
    Returns a string retrieved from the user
    :param message:  A message to the user
    :return: A string retrieved from the user
    """
    return input(f'{message}:\n')


def get_number_matches_regex(message: str, data_type: type, regex: str | None = None) -> int | float:
    """
    Returns an int number or a float retrieved from the user whose matches the given pattern
    :param message: A message to the user
    :param data_type: The type of number being retrieved
    :param regex: The pattern for the number being retrievec
    :return: an int or the float retrieved from the user
    """
    if data_type not in [int, float]:
        raise TypeError('Incorrect type')
    data_type_regex = {  # struktura przechowujaca dane w postaci klucz wartpsc
        int: r'^-?\d+$',
        float: r'^-?\d+(\.\d+)?$'
    }

    data_regex = regex if regex else data_type_regex[data_type]

    if not re.match(data_regex, v := get_str(message)):
        raise ValueError('Incorrect data format')
    return data_type(v)


def get_number_matches_regex_loop(message: str, data_type: type, regex: str | None = None) -> int | float:
    """
    Retrievs data from the user as long as it is in valid interger or floating point format accorgind
    to the provided pattern
    :param message: A message to the user
    :param data_type: The type of number being retrieved
    :param regex: The pattern for the number being retrievec
    :return: an int or the float retrieved from the user
    """
    if data_type not in [int, float]:
        raise TypeError('Incorrect type')
    data_type_regex = {
        int: r'^-?\d+$',
        float: r'^-?\d+(\.\d+)?$'
    }

    data_regex = regex if regex else data_type_regex[data_type]

    while not re.match(data_regex, v := get_str(message)):
        pass
    return data_type(v)


def get_number(message: str, data_type: type) -> int:
    """
    Retrieves data from the user as long as it is  a valid int or float
    :param message:  A message to the user
    :param data_type: The type of number being retrieved
    :return: An int number or a float number retrieved from the user
    """

    if data_type not in [int, float]:
        raise TypeError('Incorrect type')
    try:
        v = data_type(get_str(message))
    except Exception as e:
        raise ValueError(e.args[0])
    else:
        return v


def get_number_loop(message: str, data_type: type) -> int | float:
    """
    Returns an int number or float retrieved from the user
    :param message:  A message to the user
    :param data_type: The type of number being retrieved
    :return int|float: int or float retrieved from the user
    """

    if data_type not in [int, float]:
        raise TypeError('Incorrect type')
    while True:
        try:
            v = data_type(get_str(message))
        except Exception as e:
            print(e.args[0])
        else:
            return v


def get_n_numbers(n: int, data_type: type) -> list[int] | list[float]:
    """
    Return list of n int numbers or list of n float retrieved from the user
    :param n: the number of the items
    :param data_type: the tpye of number being retrieved
    :return: N int numbers or n float numbers retrieved from the user
    """
    if n <= 0:
        raise ValueError('The number of items is not correct')
    return [get_number(f'Podaj liczbe nr {i + 1}', data_type) for i in range(n)]


def get_n_numbers_loop(n: int, data_type: type) -> list[int] | list[float]:
    """
    Return list of n numbers from the user as long as they are in a valid int or a float format
    :param n:   The number of items
    :param data_type: The type of number being retrieved
    :return:    N int numbers or n float numbers retrieved from the user
    """

    if n <= 0:
        raise ValueError('The number of items is not correct')
    return [get_number_loop(f'Podaj liczbe nr {i + 1}', data_type) for i in range(n)]
