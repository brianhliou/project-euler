def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

def power_digit_sum(base, exponent):
    power = 1
    for i in range(exponent):
        print(i)
        power *= base
    return power

if __name__ == '__main__':
    power = power_digit_sum(2, 1000)
    print(power)
    print(sum_of_digits(power))
    