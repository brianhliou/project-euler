def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
    
def get_quadratic_primes(a, b):
    n = 0
    while is_prime(n**2 + a*n + b):
        n += 1
    return n

def get_coefficients_with_longest_quadratic_primes(n):
    longest_quadratic_primes = 0
    longest_quadratic_primes_coefficients = (0, 0)
    for a in range(-n + 1, n):
        for b in range(-n + 1, n):
            quadratic_primes = get_quadratic_primes(a, b)
            if quadratic_primes > longest_quadratic_primes:
                longest_quadratic_primes = quadratic_primes
                longest_quadratic_primes_coefficients = (a, b)
    return longest_quadratic_primes_coefficients

if __name__ == '__main__':
    print(get_coefficients_with_longest_quadratic_primes(1000))