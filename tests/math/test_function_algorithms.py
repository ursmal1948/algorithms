import logging
import unittest
import pytest
from algorithms.math.function_algorithms import (
    bisection_root,
    quadratic_roots,
    horner_evaluation,
    trapezoidal_integration,
    rectangular_integration
)


class TestBisectionRootFinder(unittest.TestCase):
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
            bisection_root(TestBisectionRootFinder.polynomial, -4, -6)
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
        for case in TestBisectionRootFinder.test_cases:
            with self.subTest(case=case):
                function, a, b, expected_root = case
                root = bisection_root(function, a, b)
                self.assertEqual(root, expected_root)


class TestQuadraticRootsFinder:
    def test_when_a_coefficient_equals_0(self):
        with pytest.raises(ValueError) as e:
            quadratic_roots(0, 3, 6)
        assert str(e.value) == 'Coefficient a must be a non-zero for a quadratic equation'

    @pytest.mark.parametrize('coefficients, expected_roots', [
        [(2, 10, 12), (-3, -2)],
        [(1, 4, 4), (-2, -2)],
        [(0.5, 3, 5), ((-3 + 1j), (-3 - 1j))]
    ])
    def test_correct_roots_calculation(self, coefficients, expected_roots):
        a, b, c = coefficients
        expected_root1, expected_root2 = expected_roots
        root1, root2 = quadratic_roots(a, b, c)
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

    test_cases_trapezoidal_integration = [
        [(linear_fn, 3, 8, 200), 12.5],
        [(quadratic_fn, -2, 1, 100), 10.5],
        [(polynomial_fn, 0, 5, 100), 180.4],
    ]

    test_cases_rectangular_integration = [
        [(linear_fn, 2, 15, 200), 71.5],
        [(quadratic_fn, 5, 15, 150), 1423.32],
        [(polynomial_fn, -2, 2, 50), 21.3],
    ]

    def test_trapezoidal_integration(self):
        for test_case in TestIntegration.test_cases_trapezoidal_integration:
            with self.subTest(test_case=test_case):
                params, expected_result = test_case
                fn, a, b, n = params
                integration_result = trapezoidal_integration(fn, a, b, n)
                logging.info(f'RESULT RECTANGLE: {integration_result}')
                self.assertAlmostEqual(integration_result, expected_result, places=1)

    def test_rectangular_integration(self):
        for test_case in TestIntegration.test_cases_rectangular_integration:
            params, expected_result = test_case
            fn, a, b, n = params
            integration_result = rectangular_integration(fn, a, b, n)
            self.assertAlmostEqual(integration_result, expected_result, places=1)
