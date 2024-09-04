def power_set(input_set):
    if not input_set:
        return [[]]
    first_element = input_set[0]
    rest_of_list = input_set[1:]
    subsets_minus_first = power_set(rest_of_list)

    subsets = []
    for subset in subsets_minus_first:
        subsets.append([first_element] + subset)
        subsets.append(subset)
    return subsets


# TESTS


run_cases = [
    ([1, 2], [[1, 2], [2], [1], []]),
    ([1, 2, 3], [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]),
]

submit_cases = run_cases + [
    ([], [[]]),
    ([1], [[1], []]),
    (
        [1, 2, 3, 4],
        [
            [1, 2, 3, 4],
            [2, 3, 4],
            [1, 3, 4],
            [3, 4],
            [1, 2, 4],
            [2, 4],
            [1, 4],
            [4],
            [1, 2, 3],
            [2, 3],
            [1, 3],
            [3],
            [1, 2],
            [2],
            [1],
            [],
        ],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    for i in input1:
        print(f" * {i}")
    print(f"Expecting: {expected_output}")
    result = power_set(input1)
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
