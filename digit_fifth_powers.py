def fifth_power_sum(number):
    sum = 0
    while number > 0:
        sum += (number % 10) ** 5
        number //= 10
    return sum

def digit_fifth_powers():
    sum = 0
    for i in range(2, 1000000):
        if i == fifth_power_sum(i):
            sum += i
    return sum

if __name__ == '__main__':
    print(digit_fifth_powers())