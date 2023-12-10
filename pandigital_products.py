# checks if the product is valid
def is_product_valid(a,b,c):
    return a*b == c

# splits the string containing 1,2,3,4,5,6,7,8,9 into a * b = c
def split_string(s):
    validProducts = {}
    for i in range(1, len(s) - 1):
        for j in range(i + 1, len(s)):
            a = int(s[:i])
            b = int(s[i:j])
            c = int(s[j:])
            if is_product_valid(a,b,c):
                validProducts[c] = True
    return validProducts

# get next permutation of a string containing 1,2,3,4,5,6,7,8,9
def next_permutation(s):
    s = list(s)  # Convert string to list

    # Find the largest index k such that s[k] < s[k + 1]
    for k in range(len(s) - 2, -1, -1):
        if s[k] < s[k + 1]:
            break
    else:
        return False

    # Find the largest index l such that s[k] < s[l]
    for l in range(len(s) - 1, k, -1):
        if s[k] < s[l]:
            break

    # Swap s[k] and s[l]
    s[k], s[l] = s[l], s[k]

    # Reverse the sequence from s[k + 1] up to and including the final element s[n]
    s[k + 1:] = reversed(s[k + 1:])

    return ''.join(s)

# returns the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital
def get_sum_of_products():
    sum = 0
    # initialize the string
    s = '123456789'
    # loop through all permutations of the string
    validProducts = {}
    while s:
        validProducts.update(split_string(s))
        # update s to the next permutation
        s = next_permutation(s)
    # add all the valid products
    for product in validProducts:
        sum += product
    return sum

if __name__ == '__main__':
    print(get_sum_of_products())