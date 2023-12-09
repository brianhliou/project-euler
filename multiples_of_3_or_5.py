from functools import reduce

def is_multiple_of_3_or_5(n: int) -> bool:
    """Return True if n is a multiple of 3 or 5."""
    return reduce(lambda x, y: x or y, [n % 3 == 0, n % 5 == 0])

def sum_multiples_of_3_or_5_up_to(n: int) -> int:
    """Return the sum of all multiples of 3 or 5 less than n."""
    return reduce(lambda x, y: x + y, filter(is_multiple_of_3_or_5, range(n)))

if __name__ == '__main__':
    print(sum_multiples_of_3_or_5_up_to(1000))
    