from typing import Callable
import math


def bisection_root_finder(func: Callable[[int | float], int | float], a: int | float, b: int | float, tolerance=1e-6,
                          max_iterations: int = 100) -> int | float:
    """
    Finds a root of the given function within the interval [a,b] using the bisection method
    :param func: Callable[[int|float],int|float] the function for which root is to be found
    :param a: int|float the left endpoint of the interval
    :param b: int|float the right endpoint of the interval
    :param tolerance: float the acceptable level of error in the root approximation. Default is to 1e-6
    # akceptowalny poziom bledu lub precyzji w wyniku obliczen
    :param max_iterations: int the maximum number of iterations. Default is 100.
    :return flaot: an approximation of the root within the specified tolerance
    :raises ValueErrpr: if the function has the same sign at both endpoints (func(a) * func(b) >0)
    """
    if func(a) * func(b) > 0:
        raise ValueError('The multiplication result must be a negative number')
    iteration = 0
    if a > b:
        a, b = b, a
    while (b - a) / 2 > tolerance and iteration < max_iterations:
        c = (a + b) / 2
        if func(c) == 0:
            return c
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
        iteration += 1
    return round((a + b) / 2, 3)


def quadratic_roots_finder(a: int | float, b: int | float, c: int | float) -> \
        tuple[int | float | complex, int | float | complex]:
    """
    Calculates the roots of a quadratic equation ax*2 + bx + c = 0
    :param a: int|float coefficient of x^2
    :param b: int|float coefficient of x
    :param c: int|float constant term, function value when x = 0
    :return tuple[int|float|commplex, int|float|complex]: a tuple containing the roots of the quadratic equation.
    The roots can be integers, floats or complex numbers.
    """
    if a == 0:
        raise ValueError('Coefficient a must be a non-zero for a quadratic equation')
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        root_1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root_2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return root_1, root_2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        return real_part + imaginary_part * 1j, real_part - imaginary_part * 1j


def horner_evaluation(coefficients: list[int | float], x: int | float) -> int | float:
    """
    Evaluates a polynomial represented at the specifiec value of x.
    Used often to check whether x is the root of the equation or to calculate the
    value of polynomial at x
    :param coefficients: list[int] list of coefficients representing the polynomial
    :param x: value at which the polynomial is to be evaluated
    :return int: result of the polynomial evaluation at the given value
    """
    result = 0
    for coefficient in coefficients:
        result = result * x + coefficient
    return result


def trapezoidal_integration(func: Callable[[int | float], int | float], a: int | float, b: int | float,
                            n: int | float) -> int | float:
    """
    Approximate the definite integral of a function using the trapezoidal rule
    Evaluates area under the curve by dividing the total area into smaller trapezoids
    :param func: Callable[[float],float] function to be integrate
    :param a: float the lower limit of integration
    :param b: float the upper limit of integration
    :param n: the number of trapezoids used to divide the area under the curve
    :return float: the estimated value of the definite integral
    """

    h = (b - a) / n

    integral_approximation = 0.5 * (func(a) + func(b))

    for i in range(1, n):
        x = a + i * h
        integral_approximation += func(x)
    return integral_approximation * h


def rectangle_integration(func: Callable[[int | float], int | float], a: int | float, b: int | float,
                          n: int | float) -> int | float:
    """
    Approximate the definite integral of a function using the rectangle rule. In other words evaluates the area under
    the curve by dividing the total area into smaller rectangles
    :param func: Callanle[[float],float] function to integrate
    :param a: float the lower limit of integration
    :param b: float the upper limit of integration
    :param n: int the number of rectangles used to divide the area under the curve
    :return float: the estimated value of the definite integral
    """
    h = (b - a) / n
    integral_approximation = 0
    for i in range(n):
        x = a + (i + 0.5) * h
        rectangle_area = func(x) * h
        integral_approximation += rectangle_area
    return integral_approximation
