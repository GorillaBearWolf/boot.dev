def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        converted_args = []
        converted_kwargs = {}
        for arg in args:
            converted_args.append(convert_md_to_txt(arg))
        for key, value in kwargs.items():
            converted_kwargs[key] = convert_md_to_txt(value)
        return func(*converted_args, **converted_kwargs)
    return wrapper


def convert_md_to_txt(doc):
    processed_lines = []
    for line in doc.split("\n"):
        processed_lines.append(line.lstrip('#').strip())
    return "\n".join(processed_lines)

# Don't edit below this line


@markdown_to_text_decorator
def concat(first_doc, second_doc):
    return f"""First: {first_doc}
Second: {second_doc}
"""


@markdown_to_text_decorator
def format_as_essay(title, body, conclusion):
    return f"""Title: {title}
Body: {body}
Conclusion: {conclusion}
"""

# TESTS

run_cases = [
    (
        ("# We like to play it all", "## Welcome to Tally Hall"),
        {},
        concat,
        "First: We like to play it all\nSecond: Welcome to Tally Hall\n",
    ),
    (
        set(),
        {
            "conclusion": "## That's why Python is great!",
            "title": "Why Python is Great",
            "body": """Python is a great language.

## Reasons:
* It's really easy to learn
* Everyone uses it
""",
        },
        format_as_essay,
        """Title: Why Python is Great
Body: Python is a great language.

Reasons:
* It's really easy to learn
* Everyone uses it

Conclusion: That's why Python is great!
""",
    ),
]

submit_cases = run_cases + [
    (
        ("She's a killer queen",),
        {
            "second_doc": "### Gunpowder, gelatine",
        },
        concat,
        "First: She's a killer queen\nSecond: Gunpowder, gelatine\n",
    ),
    (
        (
            "Boots' grocery list",
            """Don't forget!

## Grocery List:
* Salmon
* Honey
* Quest Scrolls
""",
        ),
        {
            "conclusion": "## Boots is getting ready for the weekend!",
        },
        format_as_essay,
        """Title: Boots' grocery list
Body: Don't forget!

Grocery List:
* Salmon
* Honey
* Quest Scrolls

Conclusion: Boots is getting ready for the weekend!
""",
    ),
]


def test(args, kwargs, func, expected_output):
    print("---------------------------------")
    print(f"\nVariadic Arguments:\n{args}\n")
    print(f"Keyword Arguments:\n{kwargs}\n")
    print(f"Expecting:\n{expected_output}")
    try:
        result = func(*args, **kwargs)
    except Exception as error:
        result = f"Error: {error}"
    print(f"Actual:\n{result}")
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
