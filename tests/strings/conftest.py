import pytest


@pytest.fixture(params=[['', True], ['a', True], ['Euston saw I was not Sue!', True], ['aabbccde', False]])
def palindrome_and_potential_palindrome(request):
    return request.param