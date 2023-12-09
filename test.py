from primes import factorize

def test_factorization():
    # Test case 1: Prime number
    num = 17
    expected_factors = [17]
    assert factorize(num) == expected_factors, f"Failed for {num}"

    # Test case 2: Composite number
    num = 84
    expected_factors = [2, 2, 3, 7]
    assert factorize(num) == expected_factors, f"Failed for {num}"

    # Test case 3: Large number
    num = 999999999999
    expected_factors = [3, 3, 3, 7, 11, 13, 37, 101, 9901]
    assert factorize(num) == expected_factors, f"Failed for {num}"

    print("All test cases passed!")

test_factorization()
