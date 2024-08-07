import pytest


@pytest.fixture
def string_analysis_path():
    return '/api/algorithms/strings/analysis'


@pytest.fixture
def palindrome_path(string_analysis_path):
    return string_analysis_path + '/palindrome'


@pytest.fixture
def pangram_path(string_analysis_path):
    return string_analysis_path + '/pangram'


@pytest.fixture
def anagrams_path(string_analysis_path):
    return string_analysis_path + '/anagrams'


@pytest.fixture
def string_manipulation_path():
    return '/api/algorithms/strings/manipulation'


@pytest.fixture
def custom_join_path(string_manipulation_path):
    return string_manipulation_path + '/join'


@pytest.fixture
def transformation_path(string_manipulation_path):
    return string_manipulation_path + '/transform'


@pytest.fixture
def compress_path(string_manipulation_path):
    return string_manipulation_path + '/compress'


@pytest.fixture
def reverse_path(string_manipulation_path):
    return string_manipulation_path + '/reverse'
