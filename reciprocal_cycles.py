def get_reciprocal_cycle(n):
    remainder = 1
    remainders = []
    while remainder not in remainders:
        remainders.append(remainder)
        remainder = (remainder * 10) % n
    return len(remainders) - remainders.index(remainder)

def get_longest_reciprocal_cycle(n):
    longest_reciprocal_cycle = 0
    longest_reciprocal_cycle_denominator = 0
    for i in range(1, n):
        reciprocal_cycle = get_reciprocal_cycle(i)
        if reciprocal_cycle > longest_reciprocal_cycle:
            longest_reciprocal_cycle = reciprocal_cycle
            longest_reciprocal_cycle_denominator = i
    return longest_reciprocal_cycle_denominator

if __name__ == '__main__':
    print(get_longest_reciprocal_cycle(1000))