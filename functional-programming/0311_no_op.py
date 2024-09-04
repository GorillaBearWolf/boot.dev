# TODO
def remove_emphasis_from_word(word):
    pass


def remove_emphasis_from_line(line):
    pass


def remove_emphasis(doc_content):
    pass


# TESTS


run_cases = [
    (
        "*Don't* panic.",
        "Don't panic.",
    ),
    (
        "The **answer to the ultimate question** of life, the universe and everything is *42*",
        "The answer to the ultimate question of life, the universe and everything is 42",
    ),
]

submit_cases = run_cases + [
    (
        "",
        "",
    ),
    (
        "In the beginning the *universe* was created. This has made a lot of people very *angry* and been widely regarded as a bad move.",
        "In the beginning the universe was created. This has made a lot of people very angry and been widely regarded as a bad move.",
    ),
    (
        "Ford, you're turning into a *penguin*",
        "Ford, you're turning into a penguin",
    ),
    (
        "*Space* is big. You just won't **believe** how vastly, hugely, mind-bogglingly big it is.",
        "Space is big. You just won't believe how vastly, hugely, mind-bogglingly big it is.",
    ),
]


def test(input_doc, expected_output):
    print("---------------------------------")
    print(f"Input document:\n{input_doc}")
    print(f"Expected output:\n{expected_output}")
    result = remove_emphasis(input_doc)
    print(f"Actual output:\n{result}")
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
