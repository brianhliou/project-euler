def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

def factorial_digit_sum(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return sum_of_digits(factorial)

if __name__ == '__main__':
    print(factorial_digit_sum(100))