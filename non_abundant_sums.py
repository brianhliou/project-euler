import math
def generate_abundant_numbers():
    """
    Generate a list of abundant numbers.
    """
    abundant_numbers = []
    for i in range(1, 28123):
        if sum(get_proper_divisors(i)) > i:
            abundant_numbers.append(i)
    return abundant_numbers

def get_proper_divisors(n):
    """
    Get a list of proper divisors for a number.
    """
    if n == 1:
        return []

    proper_divisors = [1]  # 1 is a proper divisor of all numbers except itself

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            proper_divisors.append(i)
            if i != n // i:
                proper_divisors.append(n // i)

    return sorted(proper_divisors)


def sum_of_non_abundant_numbers(n):
    """ Generate the all sums of two abundant numbers. """
    abundant_numbers = generate_abundant_numbers()
    abundant_sums = set()
    for i in abundant_numbers:
        for j in abundant_numbers:
            abundant_sums.add(i + j)
    sum = 0
    for i in range(1, n):
        if i not in abundant_sums:
            sum += i
    return sum

if __name__ == '__main__':
    print(sum_of_non_abundant_numbers(28123))