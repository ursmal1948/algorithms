from collections import Counter
from typing import Any


def is_anagram(text1: str, text2: str) -> bool:
    """
    Checks if two strings are anagrams of each other.
    An anagram is a word of phrase formed by rearranging the letters of a different word or phrase

    Args:
        text1 (str): The first string to check
        text2 (str): The second string to check
    Returns:
        bool: True if the strings are anagrams, False otherwise
    """
    if len(text1) != len(text2):
        return False
    return Counter(text1) == Counter(text2)


def is_pangram(text: str) -> bool:
    """
    Checks if a string is a pangram.
    A pangram is a sentence or phrase that contains every letter of the alphabet at least once.

    Args:
        text (str): The string to check.

    Returns:
        bool: True if the string is a pangram, False otherwise.
    """
    return len({c.lower() for c in text if c.isalpha()}) == 26


def is_palindrome(text: str) -> bool:
    """
    Checks if the given text is a palindrome.

    A palindrome is a sequence of symbols that reads the same backwards as forwards.

    Args:
        text (str): The text to be checked for palindrome.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    start_index = 0
    end_index = len(cleaned_text) - 1
    while start_index < end_index:
        if cleaned_text[start_index] != cleaned_text[end_index]:
            return False
        start_index += 1
        end_index -= 1
    return True


def is_potential_palindrome(text: str) -> bool:
    """
    Checks if the given string can be rearranged to form a palindrome.

    Args:
        text (str): The text to be checked for potential palindrome.

    Returns:
        bool: True if the text can be rearranged to form a palindrome, False otherwise.
    """
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    chars_counter = Counter(cleaned_text)
    odd_count = sum(count % 2 for count in chars_counter.values())
    return odd_count <= 1


def contains_duplicates(items: list[Any]) -> bool:
    unique_elements = set(item.lower() if isinstance(item, str) else item for item in items)
    if len(unique_elements) == len(items):
        return False
    return True
