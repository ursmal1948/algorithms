from algorithms.numbers.divisors import sum_divisors


class ErastothenesSieve:
    """
    Class for checking prime numbers using Erastothenes sieve and another method.
    """

    def __init__(self, n: int):
        """
        Initialize the sieve of Erasthotenes with a given limit
        :param n: the upper limit for the sieve
        :raises ValueError: if n is less than 2
        """
        self._sieve = self._create_sieve(n)

    @staticmethod
    def _create_sieve(n: int) -> list[bool]:

        """
        Create the sieve of Eratosthenes up to a given limit
        :param n: the upper limit for the sieve
        :return list[bool]: the sieve as a boolean list where True indicates a prime number
        :raises ValueError: if n i less than 2
        """
        if n < 2:
            raise ValueError('Eratosthenes sieve must have indexes grater than 1')
        sieve = [False, False] + [True] * (n - 1)
        p = 2
        while p * p <= n:
            if sieve[p]:
                for i in range(p * p, n + 1, p):  # wielokrotnosci p wszystkie zerujemy
                    if sieve[i]:
                        sieve[i] = False
            p += 1
        return sieve

    def is_prime(self, n: int) -> bool:
        """
        Checks if a given number is prime using the sieve
        :param n: the number to check
        :return bool: True if the number is prime, False otherwise
        :raises ValueError: if n is out of the range of the sieve
        """
        if not 0 <= n <= len(self._sieve):
            raise ValueError(f'Number {n} is out of the range')
        return self._sieve[n]


def is_prime_basic(n: int) -> bool:
    """
    Checking if the number is prime
    :param n: int the integer to be checked for a prime number
    :return bool: True if the number is, otherwise False
    """

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_prime_factors(n: int) -> list[int]:
    """
    Determines the prime factors of a given number
    :param n: int the number for which prime factors will be determined. Must be an integer greater than 1.
    :return: A list containing the prime factors of the number n. Each factory may appear in the list more than once,
    depending on its multiplicity in the prime factorization of n.
    """
    if n < 2:
        raise ValueError('The number must be greater than 1')

    prime_factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            prime_factors.append(i)
            n //= i
        i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors


def is_perfect_number(n: int) -> bool:
    """
    Checks if the number is a perfect number.

    Parameters:
        n (int): Number to check.

    Returns:
        bool: True if n is a perfect number, False otherwise.
    """
    return sum_divisors(n, False) == n
