from math import sqrt, floor

def is_prime_brute(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

is_prime_brute(2) # -> True
is_prime_brute(4) # -> False


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

is_prime(3) # -> True
is_prime(6) # -> False
