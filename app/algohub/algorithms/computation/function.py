"""
This module provides algorithms related to mathematical functions.
"""

import math


def quadratic_roots(a: int | float, b: int | float, c: int | float) -> \
        list[int | float | complex]:
    """
    Calculates the roots of a quadratic equation ax**2 + bx + c = 0.

    Parameters:
        a (int | float): Coefficient of x^2.
        b (int | float): Coefficient of x.
        c (int | float): Constant term, function value when x = 0.

    Returns:
        tuple[int | float | complex, int | float | complex]: A tuple
         containing the roots of the quadratic equation.The roots
         can be integers, floats, or complex numbers.
    """

    if a == 0:
        raise ValueError(
            'Coefficient a must be a non-zero for a quadratic equation'
        )
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        root_1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root_2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return [root_1, root_2]
    if discriminant == 0:
        root = -b / (2 * a)
        return [root, root]

    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
    root_1 = real_part + imaginary_part * 1j
    root_2 = real_part - imaginary_part * 1j

    return [root_1.imag, root_2.imag]


def horner_evaluation(coefficients: list[int | float], x: int | float) -> int:
    """
    Evaluates a polynomial represented at the specified value of x.
    Used often to check whether x is the root of the equation or
    to calculate the value of polynomial at x.

    Parameters:
        coefficients (list[int | float]): List of coefficients
         representing the polynomial.
        x (int | float): Value at which the polynomial is to be evaluated.

    Returns:
        int | float: Result of the polynomial evaluation at the given value.
    """
    if not coefficients:
        raise ValueError('Coefficients list cannot be empty')
    result = 0
    for coefficient in coefficients:
        result = result * x + coefficient
    return result
