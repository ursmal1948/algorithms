import pytest


@pytest.fixture(params=[[0, 1], [1, 1], [2, 2], [5, 120], [6, 720]])
def ge_0_number_and_expected_factorial_result(request):
    return request.param
