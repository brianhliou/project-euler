def least_common_multiple(a,b): # a and b are positive integers
    """Return the least common multiple of a and b."""
    # The least common multiple of a and b is the product of a and b divided by
    # their greatest common divisor.
    return a * b // greatest_common_divisor(a, b)

def greatest_common_divisor(a,b): # a and b are positive integers
    """Return the greatest common divisor of a and b."""
    # Euclid's algorithm
    while b:
        a, b = b, a % b
    return a

def least_common_multiple_of_range(n):
    """Return the least common multiple of all integers less than or equal to n."""
    a = 1
    for i in range(1, n + 1):
        a = least_common_multiple(a, i)
    return a
    

if __name__ == '__main__':
    print(least_common_multiple_of_range(20))