def is_pythagorean_triple(a, b, c):
    return a**2 + b**2 == c**2

def find_pythagorean_triple_with_sum(n):
    """Returns the product of the Pythagorean triple whose sum is n."""
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if is_pythagorean_triple(a, b, c):
                return a * b * c
            
if __name__ == '__main__':
    print(find_pythagorean_triple_with_sum(1000))
    