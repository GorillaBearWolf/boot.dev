def convert_file_format(filename, target_format):
    valid_extensions = ["docx", "pdf", "txt", "pptx", "ppt", "md"]
    valid_conversions = {
    "docx": ["pdf", "txt", "md"],
    "pdf": ["docx", "txt", "md"],
    "txt": ["docx", "pdf", "md"],
    "pptx": ["ppt", "pdf"],
    "ppt": ["pptx", "pdf"],
    "md": ["docx", "pdf", "txt"],
    }
    current_format = filename.split(".")[-1]
    if (
        current_format in valid_extensions
        and target_format in valid_conversions[current_format]
    ):
        return filename.replace(current_format, target_format)
    return None


# Don't edit below this line


run_cases = [
    ("Proposal.docx", "pdf", "Proposal.pdf"),
    ("Invoice.txt", "md", "Invoice.md"),
]

submit_cases = run_cases + [
    ("Presentation.ppt", "pptx", "Presentation.pptx"),
    ("Intro.pptx", "jpeg", None),
    ("Summary.md", "txt", "Summary.txt"),
    ("Contract.pdf", "pdoof", None),
]


def mutate_globals():
    main.valid_conversions = {
        "docx": ["jpeg"],
        "pdf": ["docx", "txt", "md"],
        "txt": ["docx"],
        "pptx": ["ppt", "pdf"],
        "ppt": ["pptx", "jpeg"],
        "md": ["png"],
    }


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * filename: {input1}")
    print(f" * target_format: {input2}")
    print(f"Expecting: {expected_output}")
    result = convert_file_format(input1, input2)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    mutate_globals()
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
