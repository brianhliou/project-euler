def generate_set_of_powers(n):
    powers = set()
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            powers.add(a ** b)
    return powers

if __name__ == '__main__':
    print(len(generate_set_of_powers(100)))