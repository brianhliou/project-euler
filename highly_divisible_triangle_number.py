from typing import List

def generate_triangular_number(n: int) -> int:
    """Generate the nth triangular number."""
    return n * (n + 1) // 2

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

def compute_number_of_divisors(factors: List[int]) -> int:
    """Compute the number of divisors from a list of prime factors."""
    # Initialize the number of divisors to 1
    # This will be multiplied by the number of times each prime factor occurs
    # in the prime factorization of n
    num_divisors = 1

    # Count the number of times each prime factor occurs in the prime factorization
    # of n
    count = 1
    for i in range(1, len(factors)):
        if factors[i] == factors[i - 1]:
            count += 1
        else:
            num_divisors *= count + 1
            count = 1

    # Multiply by the number of times the last prime factor occurs
    num_divisors *= count + 1

    return num_divisors

def find_first_triangular_number_with_n_divisors(n: int) -> int:
    """Return the first triangular number with more than n divisors."""
    i = 1
    while True:
        triangular_number = generate_triangular_number(i)
        factors = factorize_optimized(triangular_number)
        num_divisors = compute_number_of_divisors(factors)
        if num_divisors > n:
            return triangular_number
        i += 1
        print(i)
        
if __name__ == '__main__':
    print(find_first_triangular_number_with_n_divisors(500))
    # print(compute_number_of_divisors(factorize_optimized(100)))