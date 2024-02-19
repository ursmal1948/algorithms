import pytest
import unittest
from algorithms.strings.string_analysis import (
    is_anagram, is_pangram, is_palindrome, is_potential_palindrome, contains_duplicates)


class TestIsAnagram(unittest.TestCase):
    test_cases = [
        ('meat', 'team', True),
        ('saw', 'sam', False),
        ('', '', True),
        ('cat', 'cats', False)
    ]

    def test_is_anagram(self):
        for test_case in TestIsAnagram.test_cases:
            with self.subTest(test_case=test_case):
                text1, text2, expected_result = test_case
                self.assertEqual(is_anagram(text1, text2), expected_result)


class TestIsPangram:
    @pytest.mark.parametrize('text, expected_result', [
        ('', False),
        ('abcde12', False),
        ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', True),
        ('The quick brown fox jumps over the lazy dog!', True),
        ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', True)
    ])
    def test_is_pangram(self, text, expected_result):
        assert is_pangram(text) == expected_result


class TestPalindromeFunctions:
    def test_palindrome_and_potential_palindrome(self, palindrome_and_potential_palindrome):
        text, expected_result = palindrome_and_potential_palindrome
        assert is_palindrome(text) == expected_result
        assert is_potential_palindrome(text) == expected_result

    def test_potential_palindrome_but_not_actual_palindrome(self):
        assert not is_palindrome('batat')
        assert is_potential_palindrome('batat')


class TestContainsDuplicates:
    @pytest.fixture(params=[[1, 2, 3, 4, 5], ['a', 'b', 'c']])
    def unique_elements(self, request):
        return request.param

    @pytest.fixture(params=[[5, 6, 6, 7, 8], ['b', 'c', 'd', 'd']])
    def duplicate_elements(self, request):
        return request.param

    def test_with_unique_elements(self, unique_elements):
        assert not contains_duplicates(unique_elements)

    def test_with_duplicates(self, duplicate_elements):
        assert contains_duplicates(duplicate_elements)