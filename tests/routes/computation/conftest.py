import pytest


@pytest.fixture
def arithmetic_algorithms_path():
    return 'api/algorithms/computation/arithmetic'


@pytest.fixture
def binary_search_path(arithmetic_algorithms_path):
    return arithmetic_algorithms_path + '/binary-search'
