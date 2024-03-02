import unittest

import pytest
from algorithm_implementations.strings.string_manipulation import (
    reverse,
    compress,
    custom_join,
    lower,
    upper
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


class TestLowerAndUpper:
    @pytest.mark.parametrize('text, expected_lowercased_text', [
        ('ABCdef123', 'abcdef123'),
        ('A', 'a'),
        ('Hello#world', 'hello#world'),
    ])
    def test_lower(self, text, expected_lowercased_text):
        lowercased_text = lower(text)
        assert lowercased_text == expected_lowercased_text

    @pytest.mark.parametrize('text, expected_uppercased_text', [
        ('abcDEF8!', 'ABCDEF8!'),
        ('c', 'C'),
        ('north-face', 'NORTH-FACE')
    ])
    def test_upper(self, text, expected_uppercased_text):
        uppercased_text = upper(text)

        assert uppercased_text == expected_uppercased_text
