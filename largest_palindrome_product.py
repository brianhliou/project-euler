def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_largest_palindrome_product():
    """Returns the largest palindrome product of two 3-digit numbers."""
    largest_palindrome_product = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome_product:
                largest_palindrome_product = product
    return largest_palindrome_product

if __name__ == '__main__':
    print(find_largest_palindrome_product())