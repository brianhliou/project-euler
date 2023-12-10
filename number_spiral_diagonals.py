def get_sum_of_diagonals(n):
    """
    Get the sum of the diagonals in a number spiral of size n.
    """
    if n == 1:
        return 1

    sum = 1
    for i in range(3, n + 1, 2):
        sum += 4 * i ** 2 - 6 * i + 6

    return sum

if __name__ == '__main__':
    print(get_sum_of_diagonals(1001))