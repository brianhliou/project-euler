def find_largest_prime_factor(n):
    """Returns the largest prime factor of n."""
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

if __name__ == '__main__':
    print(find_largest_prime_factor(600851475143))