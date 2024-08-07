import pytest
from app.algohub.algorithms.computation.function import (
    quadratic_roots,
    horner_evaluation,
)


class TestQuadraticRootsFinder:
    def test_when_a_coefficient_equals_0(self):
        with pytest.raises(ValueError) as e:
            quadratic_roots(0, 3, 6)
        assert str(e.value) == 'Coefficient a must be a non-zero for a quadratic equation'

    @pytest.mark.parametrize('coefficients, expected_roots', [
        [(2, 10, 12), (-3, -2)],
        [(1, 4, 4), (-2, -2)],
        [(0.5, 3, 5), ((1.0, -1.0))]
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
