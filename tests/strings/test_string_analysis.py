import pytest
import unittest
from app.algohub.algorithms.strings.string_analysis import (
    is_anagram,
    is_pangram,
    is_palindrome,
    is_potential_palindrome,
    count_substring_occurences,
    is_substring,
    is_subsequence,
    contains_duplicates
)
from ..conftest import palindrome_and_potential_palindrome


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


class TestSubsequenceAndSubstring:
    @pytest.fixture(params=[
        (['hello', 'el'], True),
        (['hello', 'ho'], True),
        (['world', 'abc'], False),
        (['abc', ''], True),
        (['', ''], True)])
    def text_potential_subsequence_and_result(self, request):
        return request.param

    def test_is_subsequence(self, text_potential_subsequence_and_result):
        sequence_pair, result = text_potential_subsequence_and_result
        assert is_subsequence(sequence_pair[0], sequence_pair[1]) == result

    @pytest.fixture(params=[
        (['abc', 'a'], True),
        (['abc', 'c'], True),
        (['garden', 'gar'], True),
        (['garden', 'gdn'], False),
        (['garden', 'den'], True),
        (['abc', ''], True),
        (['', 'abc'], False),
        (['', ''], True),
        (['', 'a'], False),
    ])
    def text_potential_substring_and_result(self, request):
        return request.param

    def test_is_substring(self, text_potential_substring_and_result):
        sequence_pair, result = text_potential_substring_and_result
        assert is_substring(sequence_pair[0], sequence_pair[1]) == result


class TestCountSubstringOccurences:
    @pytest.mark.parametrize('text, substring, expected_count', [
        ('abDababab', 'ab', 4),
        ('ccc', 'c', 3),
        ('garden garden', 'ard', 2),
        ('world', 'o', 1),
        ('hello', 'abc', 0)
    ])
    def test_substring_occurences(self, text, substring, expected_count):
        assert count_substring_occurences(text, substring) == expected_count


class TestContainsDuplicates:
    @pytest.fixture(params=[[1, 2, 3, 4, 5], ['a', 'b', 'c']])
    def unique_elements(self, request):
        return request.param

    @pytest.fixture(params=[[5, 6, 6, 7, 8], ['b', 'c', 'd', 'D']])
    def duplicate_elements(self, request):
        return request.param

    def test_with_unique_elements(self, unique_elements):
        assert not contains_duplicates(unique_elements)

    def test_with_duplicates(self, duplicate_elements):
        assert contains_duplicates(duplicate_elements)
