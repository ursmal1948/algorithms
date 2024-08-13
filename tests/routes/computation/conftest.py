import pytest


@pytest.fixture
def arithmetic_algorithms_path():
    return 'api/algorithms/computation/arithmetic'


@pytest.fixture
def function_algorithms_path():
    return 'api/algorithms/computation/function'


@pytest.fixture
def geometric_algorithms_path():
    return 'api/algorithms/computation/geometric'


@pytest.fixture
def points_distance_path(geometric_algorithms_path):
    return geometric_algorithms_path + '/distance-between-points'


@pytest.fixture
def points_collinearity_path(geometric_algorithms_path):
    return geometric_algorithms_path + '/collinearity'


@pytest.fixture
def valid_triangle_path(geometric_algorithms_path):
    return geometric_algorithms_path + '/valid-triangle'


@pytest.fixture
def rectangular_triangle_path(geometric_algorithms_path):
    return geometric_algorithms_path + '/rectangular-triangle'


@pytest.fixture
def quadratic_roots_path(function_algorithms_path):
    return function_algorithms_path + '/quadratic-roots'


@pytest.fixture
def horner_path(function_algorithms_path):
    return function_algorithms_path + '/horner'


@pytest.fixture
def numeric_algorithms_path():
    return 'api/algorithms/computation/numeric'


@pytest.fixture
def trapezoidal_integration_path(numeric_algorithms_path):
    return numeric_algorithms_path + '/trapezoidal-integration'


@pytest.fixture
def rectangular_integration_path(numeric_algorithms_path):
    return numeric_algorithms_path + '/rectangular-integration'


@pytest.fixture
def binary_search_path(arithmetic_algorithms_path):
    return arithmetic_algorithms_path + '/binary-search'
