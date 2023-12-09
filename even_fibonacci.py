def next_fibonacci(a, b):
    return (b, a + b)

def is_even(n):
    return n % 2 == 0

def sum_even_fibonacci_up_to(n):
    """Return the sum of all even Fibonacci numbers less than n."""
    a, b = 1, 1
    sum = 0
    while a < n:
        if is_even(a):
            sum += a
        a, b = next_fibonacci(a, b)
    return sum

if __name__ == '__main__':
    print(sum_even_fibonacci_up_to(4000000))