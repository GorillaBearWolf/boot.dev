def bubble_sort(nums):
    swapping = True
    end = len(nums)

    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1

    return nums

"""
def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        swapped = False  # Track if any swaps occurred

        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:  # If no swaps happened, the array is sorted
            break

    return nums
"""


# TESTS


run_cases = [
    ([5, 7, 3, 6, 8], [3, 5, 6, 7, 8]),
    ([2, 1], [1, 2]),
]

submit_cases = run_cases + [
    ([], []),
    ([1], [1]),
    ([1, 5, -3, 2, 4], [-3, 1, 2, 4, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 3, 2, 5, 4], [1, 2, 3, 4, 5]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input:\n * {input1}")
    print(f"Expecting: {expected_output}")
    result = bubble_sort(input1)
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
