from typing import List
from typing import List

def generate_primes_up_to(n: int) -> List[int]:
    """Generate a list of all prime numbers less than n."""
    primes: List[int] = []
    is_prime: bool = True
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
        is_prime = True
    return primes

def generate_nth_prime(n: int) -> int:
    """Generate the nth prime number with optimized algorithm."""
    if n == 1:
        return 2  # Directly return 2 for the first prime

    primes = [2]  # Initialize the list with the first prime number
    candidate = 3  # Start checking from the next odd number

    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if prime * prime > candidate:
                break  # Stop checking if the square of the prime is greater than the candidate
            if candidate % prime == 0:
                is_prime = False
                break  # Not a prime if divisible by any of the primes in the list

        if is_prime:
            primes.append(candidate)  # Add the prime to the list

        candidate += 2  # Increment by 2 to check only odd numbers

    return primes[-1]  # Return the nth prime

def generate_primes_up_to_n(n: int) -> list:
    """Generate all prime numbers up to n."""
    if n < 2:
        return []  # Return an empty list if n is less than 2

    primes = [2]  # Initialize the list with the first prime number
    candidate = 3  # Start checking from the next odd number

    while candidate <= n:
        is_prime = True
        for prime in primes:
            if prime * prime > candidate:
                break  # Stop checking if the square of the prime is greater than the candidate
            if candidate % prime == 0:
                is_prime = False
                break  # Not a prime if divisible by any of the primes in the list

        if is_prime:
            primes.append(candidate)  # Add the prime to the list

        candidate += 2  # Increment by 2 to check only odd numbers

    return primes  # Return the list of primes


def is_prime(n: int) -> bool:
    """Return True if n is prime."""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def factorize(n: int) -> List[int]:
    """Return a factorization of n."""
    factors: List[int] = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def factorize_optimized(n: int) -> List[int]:
    """Return a factorization of n with optimizations."""
    factors = []
    
    # Handle factor 2 separately
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check only odd numbers starting from 3
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 2  # Increment by 2 to skip even numbers

    if n > 1:
        factors.append(n)

    return factors

if __name__ == '__main__':
    # primes_up_to_2000000 = generate_primes_up_to_n(2000000)
    # print(sum(primes_up_to_2000000))
    
    print(factorize(1001))
    print(factorize_optimized(1001))
    print(factorize_optimized(100001))
    print(factorize_optimized(999123456999))