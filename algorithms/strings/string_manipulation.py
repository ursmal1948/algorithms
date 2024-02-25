from collections import Counter, OrderedDict


def reverse_string(text: str) -> str:
    """
    Reverses a given string.

    Parameters:
        text (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """

    backwards = []
    items_length = len(text)
    for i in range(items_length - 1, -1, -1):
        backwards.append(text[i])
    return ''.join(backwards)


def string_compression(text: str) -> str:
    """
    Compresses a given string by representing the count of occurrences for each character.

    Parameters:
        text (str): The string to be compressed.

    Returns:
        str: The compressed string indicating the count of each character.
    """

    chars_counter = Counter(text)
    ordered_chars_counter = OrderedDict.fromkeys(text)
    return ''.join([c + str(chars_counter[c]) for c in ordered_chars_counter])


def custom_join(words: list[str], separator: str = '') -> str:
    """
    Concatenates a list of strings using the specified separator.

    Parameters:
        words (list[str]): The list of strings to be joined.
        separator (str): The string to be used as a separator between each element in the list. Default is ''.

    Returns:
        str: A string resulting from concatenating the elements of the list with the separator.

    Raises:
        ValueError: If any element in the 'words' list is not a string.
    """

    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements must be strings")
    result = ''
    for i in range(len(words)):
        if i == len(words) - 1:
            result += words[i]
        else:
            result += (words[i] + separator)
    return result


# It will be in ciphers branch after rebasing main.
def lower_string(text: str) -> str:
    return ''.join([chr(ord(c) + 32) if c.isupper() else c for c in text])


def upper_string(text: str) -> str:
    return ''.join([chr(ord(c) - 32) if c.islower() else c for c in text])
