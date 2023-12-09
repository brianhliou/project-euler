def sum_up_to_n(n):
    """Return the sum of all numbers less than n."""
    return n * (n + 1) // 2

def sum_of_squares_up_to_n(n):
    """Return the sum of the squares of all numbers less than n."""
    return n * (n + 1) * (2 * n + 1) // 6

def sum_square_difference(n):
    """Return the difference between the sum of the squares of all numbers less
    than n and the square of the sum of all numbers less than n."""
    return sum_up_to_n(n) ** 2 - sum_of_squares_up_to_n(n)

if __name__ == '__main__':
    print(sum_square_difference(100))