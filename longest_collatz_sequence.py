cache = {}

def get_collatz_sequence_length(n):
    if n == 1:
        return 1
    elif n in cache:
        return cache[n]
    elif n % 2 == 0:
        length = 1 + get_collatz_sequence_length(n // 2)
    else:
        length = 1 + get_collatz_sequence_length(3 * n + 1)
    cache[n] = length
    return length
    
def get_longest_collatz_sequence_length(n):
    longest_collatz_sequence_length = 0
    longest_collatz_sequence_starting_number = 0
    for i in range(1, n):
        print(i)
        collatz_sequence_length = get_collatz_sequence_length(i)
        if collatz_sequence_length > longest_collatz_sequence_length:
            longest_collatz_sequence_length = collatz_sequence_length
            longest_collatz_sequence_starting_number = i
    return longest_collatz_sequence_starting_number

if __name__ == '__main__':
    print(get_longest_collatz_sequence_length(1000000))