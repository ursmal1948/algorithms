import pytest


@pytest.fixture(params=[['', True], ['a', True], ['Euston saw I was not Sue!', True], ['aabbccde', False]])
def palindrome_and_potential_palindrome(request):
    return request.param


@pytest.fixture(params=[[0, 1], [1, 1], [2, 2], [5, 120], [6, 720]])
def ge_0_number_and_expected_factorial_result(request):
    return request.param


@pytest.fixture(params=[
    ([10, -5, 29, -300, 200, 12, 45, 90, 33, 120, 17], [-300, -5, 10, 12, 17, 29, 33, 45, 90, 120, 200]),
    (['dog', 'lion', 'cat', 'anaconda', 'tiger'], ['anaconda', 'cat', 'dog', 'lion', 'tiger'])

])
def items_and_expected_sorted_items(request):
    return request.param
