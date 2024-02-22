import unittest

import pytest
from algorithms.numbers.primes import (
    ErastothenesSieve,
    is_prime_basic,
    get_prime_factors
)


class TestErastothenesSieve(unittest.TestCase):
    test_cases = [
        (0, False),
        (1, False),
        (2, True),
        (18, False),
        (41, True),
        (100, False),
    ]

    @classmethod
    def setUpClass(cls):
        cls.sieve = ErastothenesSieve(100)

    def test_invalid_input_for_sieve_creation(self):
        with self.assertRaises(ValueError) as e:
            sieve = ErastothenesSieve(1)
        self.assertEqual('Eratosthenes sieve must have indexes grater than 1', str(e.exception))

    def test_is_prime(self):
        for test_case in TestErastothenesSieve.test_cases:
            with self.subTest(test_case=test_case):
                number, expected_is_prime = test_case
                is_prime = self.sieve.is_prime(number)
                self.assertEqual(is_prime, expected_is_prime)

    def test_is_prime_with_number_out_of_range(self):
        with self.assertRaises(ValueError) as e:
            self.sieve.is_prime(103)
        self.assertEqual(f'Number 103 is out of the range', str(e.exception))


class TestPrimeFunctions:
    @pytest.mark.parametrize('number, expected_is_prime', [
        (1, False),
        (2, True),
        (4, False),
        (25, False),
        (13, True),
        (41, True),
    ])
    def test_is_prime(self, number, expected_is_prime):
        is_prime = is_prime_basic(number)
        assert is_prime is expected_is_prime

    @pytest.mark.parametrize('number, expected_prime_factors', [
        (2, [2]),
        (6, [2, 3]),
        (18, [2, 3, 3]),
        (32, [2, 2, 2, 2, 2]),
        (49, [7, 7]),
        (120, [2, 2, 2, 3, 5]),
    ])
    def test_get_prime_factors(self, number, expected_prime_factors):
        prime_factors = get_prime_factors(number)
        assert prime_factors == expected_prime_factors

    def test_get_prime_factors_with_invalid_input(self):
        with pytest.raises(ValueError) as e:
            get_prime_factors(1)
        assert 'The number must be greater than 1' == str(e.value)
