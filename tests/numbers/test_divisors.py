import unittest
import pytest
from algohub.numbers.divisors import count_divisors, count_common_divisors, sum_divisors


class TestCountDivisors:

    @pytest.fixture(params=[[-5, 2], [-10, 4], [0, float('inf')], [1, 1], [3, 2], [23, 2], [26, 4], [49, 3], [100, 9]])
    def number_and_divisor_count(self, request):
        return request.param

    def test_positive_numbers(self, number_and_divisor_count):
        number, expected_divisors_count = number_and_divisor_count[0], number_and_divisor_count[1]
        assert count_divisors(number) == expected_divisors_count


class TestCountCommonDivisors:
    @pytest.mark.parametrize('number1, number2, expected_common_divisors_count', [
        (0, -16, 5),
        (-28, 0, 6),
        (-36, -12, 6),
        (0, 0, float('inf')),
        (0, 8, 4),
        (9, 0, 3),
        (24, 4, 3),
        (36, 12, 6),
        (10, 10, 4)
    ])
    def test_count_common_divisors(self, number1, number2, expected_common_divisors_count):
        common_divisors_count = count_common_divisors(number1, number2)
        assert common_divisors_count == expected_common_divisors_count


class TestSumDivisors(unittest.TestCase):
    def setUp(self):
        self.negative_numbers_data = [[-4, 7], [-10, 18]]
        self.positive_numbers_data = [[6, 12], [7, 8], [10, 18], [13, 14], [20, 42]]
        self.special_cases = [[0, float('inf')], [1, 1], [2, 3], [3, 4]]

    def test_when_number_equals_zero(self):
        self.assertEqual(sum_divisors(0), float('inf'))

    def test_negative_numbers_divisors_sum_including_number(self):
        for number, expected_divisors_sum in self.negative_numbers_data:
            with self.subTest(number=number):
                self.assertEqual(sum_divisors(number), expected_divisors_sum)

    def test_negative_numbers_divisors_sum_excluding_number(self):
        for number, expected_divisors_sum in self.negative_numbers_data:
            with self.subTest(number=number):
                self.assertEqual(sum_divisors(number, False), expected_divisors_sum + number)

    def test_positive_numbers_divisors_sum_including_number(self):
        for number, expected_divisors_sum in self.positive_numbers_data:
            with self.subTest(number=number):
                self.assertEqual(sum_divisors(number), expected_divisors_sum)

    def test_positive_numbers_divisors_sum_excluding_number(self):
        for number, expected_divisors_sum in self.positive_numbers_data:
            with self.subTest(number=number):
                self.assertEqual(sum_divisors(number, False), expected_divisors_sum - number)

    def test_with_special_cases(self):
        for number, expected_divisors_sum in self.special_cases:
            with self.subTest(number=number):
                self.assertEqual(sum_divisors(number), expected_divisors_sum)

    def tearDown(self):
        self.positive_numbers_data = None
        self.negative_numbers_data = None
