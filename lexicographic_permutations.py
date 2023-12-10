def next_permutation(a):
    # Find the largest index k such that a[k] < a[k + 1]
    for k in range(len(a) - 2, -1, -1):
        if a[k] < a[k + 1]:
            break
    else:
        return False

    # Find the largest index l such that a[k] < a[l]
    for l in range(len(a) - 1, k, -1):
        if a[k] < a[l]:
            break

    # Swap the value of a[k] with that of a[l]
    a[k], a[l] = a[l], a[k]

    # Reverse the sequence from a[k + 1] up to and including the final element a[n]
    a[k + 1:] = a[len(a) - 1: k: -1]

    return True

if __name__ == '__main__':
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(999999):
        next_permutation(a)

    print(''.join(str(x) for x in a))