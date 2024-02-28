import unittest

import pytest
from algorithms.strings.string_manipulation import (
    reverse,
    compress,
    custom_join
)


class TestReverse(unittest.TestCase):
    words_for_reversal = ['hello world', '', 'A', 'kAjak']

    def test_reverse_string(self):
        for word in TestReverse.words_for_reversal:
            with self.subTest(word=word):
                self.assertEqual(reverse(word), word[::-1])


class TestCompression:
    @pytest.mark.parametrize("text, expected_compressed_text", [
        ('B', 'B1'),
        ('abccbaA', 'a2b2c2A1'),
        ('cc dc', 'c3 1d1')

    ])
    def test_string_compression(self, text, expected_compressed_text):
        assert compress(text) == expected_compressed_text


class TestCustomJoin:

    def test_when_any_element_is_not_string(self):
        with pytest.raises(ValueError) as e:
            custom_join(['a', 'b', 1], '#')
        assert 'All elements must be strings' == str(e.value)

    @pytest.fixture(params=[
        (['a', 'b', 'c'], '#'),
        (['c', 'b', 'a'], '$'),
        (['garden'], '#'),
        (['north', 'face'], '-'),
        (['hello', 'world'], ''),
        ([], '#'), ([''], '')])
    def words_and_separator_fixture(self, request):
        return request.param

    def test_with_valid_data(self, words_and_separator_fixture):
        words, sep = words_and_separator_fixture
        assert custom_join(words, sep) == f'{sep}'.join(words)
