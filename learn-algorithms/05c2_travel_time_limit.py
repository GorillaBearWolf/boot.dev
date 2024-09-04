def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1

    while time_left >= time_in_country:
        count += 1
        time_left -= time_in_country
        time_in_country = time_in_country * factor

    return count


# TESTS


run_cases = [
    (2, 1.2, 1),
    (3, 1.2, 2),
]

submit_cases = run_cases + [
    (10, 1.2, 6),
    (100, 1.2, 16),
    (200, 1.2, 20),
    (1000, 1.3, 21),
    (0, 1.5, 0),
    (1, 0.5, 1),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Max days: {input1}")
    print(f" * Time factor: {input2}")
    print(f"Expecting: {expected_output}")
    result = num_countries_in_days(input1, input2)
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
