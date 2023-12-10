def get_next_fibonacci(a,b):
    return a+b

def number_of_digits(n):
    digits = 0
    while n > 0:
        digits += 1
        n //= 10
    return digits

def get_first_fibonacci_number_with_n_digits(n):
    a = 1
    b = 1
    index = 2
    while number_of_digits(b) < n:
        a, b = b, get_next_fibonacci(a, b)
        index += 1
    return index

if __name__ == '__main__':
    print(get_first_fibonacci_number_with_n_digits(1000))