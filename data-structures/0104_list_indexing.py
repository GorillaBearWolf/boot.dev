import random


def last_item(inventory):
    if not inventory:
        return None
    return "".join(inventory[-1:])


# TESTS



run_cases = [
    (10, "Bread"),
    (100, "Healing potion"),
]

submit_cases = run_cases + [
    (1000, "Leather scraps"),
    (10000, "Leather scraps"),
    (100000, "Chainmail Armor"),
    (0, None),
]


def get_inventory(num):
    random.seed(1)
    options = [
        "Short sword",
        "Bread",
        "Healing potion",
        "Leather scraps",
        "Chainmail Armor",
    ]
    inventory = []
    for _ in range(num):
        optionI = random.randint(0, len(options) - 1)
        inventory.append(options[optionI])
    return inventory


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input} Inventory Items")
    print(f"Expecting: {expected_output}")
    inventory = get_inventory(input)
    result = last_item(inventory)
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
