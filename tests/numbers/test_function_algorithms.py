import unittest
import pytest
from algorithms.numbers.function_algorithms import (
    bisection_root_finder,
    quadratic_roots_finder,
    horner_evaluation,
    trapezoidal_integration,
    rectangle_integration
)


class TestBisectionRootFinder2(unittest.TestCase):
    @staticmethod
    def linear_fn(x: int | float) -> int | float:
        return x + 4

    @staticmethod
    def quadratic_fn(x: int | float) -> int | float:
        return x * x - 4 * x

    @staticmethod
    def polynomial(x: int | float) -> int | float:
        return x ** 3 - 6 * x * x + 11 * x - 6

    def test_when_not_correct(self):
        with self.assertRaises(ValueError) as e:
            bisection_root_finder(TestBisectionRootFinder2.polynomial, -4, -6)
        self.assertEqual(str(e.exception), 'The multiplication result must be a negative number')

    test_cases = [
        (linear_fn, -6, 0, -4),
        (quadratic_fn, -13, 3, 0),
        (quadratic_fn, 16, 3, 4),
        (polynomial, -1, 1.5, 1),
        (polynomial, 1.5, 2.5, 2),
        (polynomial, 2.5, 10, 3)
    ]

    def test_with_correct_data(self):
        for case in TestBisectionRootFinder2.test_cases:
            with self.subTest(case=case):
                function, a, b, expected_root = case
                root = bisection_root_finder(function, a, b)
                self.assertEqual(root, expected_root)


class TestQuadraticRootsFinder:
    def test_when_a_coefficient_equals_0(self):
        with pytest.raises(ValueError) as e:
            quadratic_roots_finder(0, 3, 6)
        assert str(e.value) == 'Coefficient a must be a non-zero for a quadratic equation'

    @pytest.mark.parametrize('coefficients, expected_roots', [
        [(2, 10, 12), (-3, -2)],
        [(1, 4, 4), (-2, -2)],
        [(0.5, 3, 5), ((-3 + 1j), (-3 - 1j))]
    ])
    def test_correct_roots_calculation(self, coefficients, expected_roots):
        a, b, c = coefficients
        expected_root1, expected_root2 = expected_roots
        root1, root2 = quadratic_roots_finder(a, b, c)
        assert (root1, root2) == (expected_root1, expected_root2)


class TestHornerEvaluation:
    @pytest.mark.parametrize('coefficients, value, expected_result', [
        ([1, -6, 11, -6], 0, -6),
        ([1, 2, 1], 1, 4),
        ([2, -3, 4], 3, 13),
        ([2, -6], 3, 0)
    ])
    def test_various_cases(self, coefficients, value, expected_result):
        result = horner_evaluation(coefficients, value)
        assert result == expected_result


class TestIntegration(unittest.TestCase):

    @staticmethod
    def linear_fn(x: int | float) -> int | float:
        return x - 3

    @staticmethod
    def quadratic_fn(x: int | float) -> int | float:
        return x * x + 3 * x + 4

    @staticmethod
    def polynomial_fn(x: int | float) -> int | float:
        return x ** 3 + x * x - 3 * x + 4

    test_cases = [
        [(linear_fn, 3, 8, 200), 12.5],
        [(linear_fn, -2, 4, 150), -12],
        [(quadratic_fn, -2, 1, 100), 10.5],
        [(quadratic_fn, 1, 5, 100), 93.33],
        [(polynomial_fn, 0, 5, 100), 180.4],
        [(polynomial_fn, 2, 4, 200), 68.67]
    ]

    def test_integration(self):
        for test_case in TestIntegration.test_cases:
            with self.subTest(test_case=test_case):
                params, expected_result = test_case
                fn, a, b, n = params
                result_rectangle = rectangle_integration(fn, a, b, n)
                result_trapezoidal = trapezoidal_integration(fn, a, b, n)
                self.assertAlmostEqual(result_rectangle, expected_result, places=1)
                self.assertAlmostEqual(result_trapezoidal, expected_result, places=1)
