from typing import Callable


def create_polynomial_function(coefficients: list[int]) -> Callable[[int | float], int | float]:
    def polynomial_function(x):
        result = 0
        for index, coeff in enumerate(coefficients):
            result += coeff * (x ** (len(coefficients) - 1 - index))
        return result

    return polynomial_function


def execute_function_from_string(expression: str, x_value: int | float) -> int | float:
    try:
        x = x_value
        return eval(expression)
    except Exception as e:
        raise ValueError(f'Error evaluating expression: {e}')
