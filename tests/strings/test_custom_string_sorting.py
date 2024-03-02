import pytest
from algorithm_implementations.strings.custom_string_sorting import (
    sort_items,
    compare_chars_sum,
    compare_vowels_count
)


class TestSortItems:
    @pytest.mark.parametrize('items, expected_sorted_items', [
        (['banana', 'apple', 'pear', 'orange'], ['apple', 'pear', 'banana', 'orange']),
        (['hello', 'world', 'pythooon', 'programming'], ['world', 'hello', 'programming', 'pythooon']),
        (['a', 'b', 'e', 'd'], ['b', 'd', 'a', 'e'])
    ])
    def test_sort_items_with_compare_vowels_count_fn(self, items, expected_sorted_items):
        assert sort_items(items, compare_vowels_count) == expected_sorted_items

    @pytest.mark.parametrize('items, expected_sorted_items', [
        (['abcde', 'ABCDE', 'abc', 'ABC'], ['ABC', 'abc', 'ABCDE', 'abcde']),
        (['aaa', 'aAa', 'AaA', 'AAA'], ['AAA', 'AaA', 'aAa', 'aaa']),
        (['123', '789', '456'], ['123', '456', '789'])
    ])
    def test_with_compare_chars_sum_fn(self, items, expected_sorted_items):
        assert sort_items(items, compare_chars_sum) == expected_sorted_items
