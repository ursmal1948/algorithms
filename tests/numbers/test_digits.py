import pytest
from algorithm_implementations.numbers.digits import (
    get_digit,
    sum_digits,
    move_zeroes,
    validate_luhn
)


class TestGetDigit:
    @pytest.mark.parametrize("number, position, expected_result", [
        (534, 0, 4),
        (534, 1, 3),
        (534, 2, 5),
        (534, 6, 0),
        (-534, 1, 3),
        (534, -1, ValueError('Position must be a non-negative number')),

    ])
    def test_get_digit(self, number, position, expected_result):
        if isinstance(expected_result, Exception):
            with pytest.raises(type(expected_result)) as e:
                get_digit(number, position)
            assert str(e.value) == str(expected_result)
        else:
            assert get_digit(number, position) == expected_result


class TestSumDigits:
    @pytest.fixture(params=[[12, 3], [987654321, 45], [0, 0], [-123, 6]])
    def number_and_expected_sum(self, request):
        return request.param

    def test_sum_digits(self, number_and_expected_sum):
        number, expected_digits_sum = number_and_expected_sum[0], number_and_expected_sum[1]
        assert sum_digits(number) == expected_digits_sum


class TestMoveZeroes:
    @pytest.fixture(
        params=[([1, 2, 3], [1, 2, 3]), ([0, 1, 0, 2, 4, 0, 5], [1, 2, 4, 5, 0, 0, 0]), ([0, 0, 0], [0, 0, 0]),
                ([0], [0]), ([], [])])
    def numbers_and_expected_result_after_moving_zeroes(self, request):
        return request.param

    def test_move_zeroes(self, numbers_and_expected_result_after_moving_zeroes):
        numbers_list, expected_numbers_with_zeroes_moved_to_the_end = numbers_and_expected_result_after_moving_zeroes
        assert move_zeroes(numbers_list) == expected_numbers_with_zeroes_moved_to_the_end


class TestValidateLuhn:
    @pytest.mark.parametrize('credit_card_number, expected_result', [
        ['1234567890123456', False],
        ['4245110203731942', True],
        ['79927398713', True],
        ['79927398714', False],

    ])
    def test(self, credit_card_number, expected_result):
        validation_result = validate_luhn(credit_card_number)
        assert validation_result == expected_result
