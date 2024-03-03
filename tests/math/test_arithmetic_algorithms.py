import pytest
from algohub.math.arithmetic_algorithms import (
    iterative_factorial,
    recursive_factorial,
    binary_search,
    binary_exponentiation,
    babylonian_sqrt
)

from tests.conftest import ge_0_number_and_expected_factorial_result


class TestBinarySearch:
    @pytest.mark.parametrize('numbers, looked_number, expected_result', [
        ([10, 20, 30, 40, 50], 10, 0),
        ([10, 20, 30, 40, 50], 30, 2),
        ([10, 20, 30, 40, 50], 50, 4),
        ([10, 20, 30, 40, 50], 60, False),
        ([], 5, False),
    ])
    def test_binary_search(self, numbers, looked_number, expected_result):
        assert binary_search(numbers, looked_number) == expected_result


class TestBabylonianSqrt:
    @pytest.fixture(params=[
        (16, 4.0),
        (25, 5.0),
        (49, 7.0),
        (100, 10.0)
    ])
    def number_and_expected_sqrt_result_with_default_accuracy(self, request):
        return request.param

    def test_with_default_accuracy(self, number_and_expected_sqrt_result_with_default_accuracy):
        number, expected_result = number_and_expected_sqrt_result_with_default_accuracy
        assert babylonian_sqrt(number) == expected_result

    @pytest.fixture(params=[
        (16, 0.1, 4.002),
        (49, 0.1, 7.001),
        (64, 0.1, 8.005),
        (49, 0.01, 7.0),
        (100, 0.01, 10.0),
    ])
    def number_accuracy_and_expected_sqrt_result(self, request):
        return request.param

    def test_with_custom_accuracy(self, number_accuracy_and_expected_sqrt_result):
        number, accuracy, expected_result = number_accuracy_and_expected_sqrt_result
        assert babylonian_sqrt(number, accuracy) == expected_result


class TestBinaryExponentiation:
    @pytest.mark.parametrize('number, power, expected_result', [
        (5, 0, 1),
        (0, 5, 0),
        (1, 10, 1),
        (2, 3, 8),
        (4, 5, 1024),
    ])
    def test_binary_exponentiation(self, number, power, expected_result):
        assert binary_exponentiation(number, power) == expected_result


class TestFactorials:
    def test_iterative_with_negative_number(self):
        with pytest.raises(ValueError) as e:
            iterative_factorial(-10)
        assert 'The number must be a non-negative integer' == str(e.value)

    def test_iterative_with_ge_0_number(self, ge_0_number_and_expected_factorial_result):
        number, expected_factorial_result = ge_0_number_and_expected_factorial_result
        assert iterative_factorial(number) == expected_factorial_result

    def test_recursive_with_negative_number(self):
        with pytest.raises(ValueError) as e:
            recursive_factorial(-5)
        assert 'The number must be a non-negative integer' == str(e.value)

    def test_recursive_with_ge_0_number(self, ge_0_number_and_expected_factorial_result):
        number, expected_factorial_result = ge_0_number_and_expected_factorial_result
        assert recursive_factorial(number) == expected_factorial_result
