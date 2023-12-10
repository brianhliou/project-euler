def get_factors(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    return factors

def sum_of_factors(n):
    return sum(get_factors(n))

def is_amicable_number(n):
    sum_of_n_factors = sum_of_factors(n)
    if sum_of_n_factors == n:
        return False
    return sum_of_factors(sum_of_n_factors) == n

def sum_of_amicable_numbers(n):
    sum = 0
    for i in range(1, n):
        if is_amicable_number(i):
            sum += i
    return sum

if __name__ == '__main__':
    print(sum_of_amicable_numbers(10000))