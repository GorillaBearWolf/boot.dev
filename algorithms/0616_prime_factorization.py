import math


def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 2  # Only check odd numbers

    if n > 2:
        factors.append(n)

    return factors



# TESTS


run_cases = [(8, [2, 2, 2]), (10, [2, 5]), (24, [2, 2, 2, 3])]

submit_cases = run_cases + [
    (49, [7, 7]),
    (77, [7, 11]),
    (4, [2, 2]),
    (64, [2, 2, 2, 2, 2, 2]),
    (63, [3, 3, 7]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    result = prime_factors(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
