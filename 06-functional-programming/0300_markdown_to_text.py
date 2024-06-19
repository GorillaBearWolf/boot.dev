def markdown_to_text(doc_content):
    doc_list = doc_content.split('\n')
    removed_hash_whitespace = list(map(remove_hash_and_strip, doc_list))
    result_words = map(lambda x: ' '.join(map(remove_asterisks_from_words, x.split())), removed_hash_whitespace)
    return '\n'.join(result_words)


def remove_asterisks_from_words(doc_list):
    if doc_list == '*':
        return doc_list.strip('')
    return doc_list.strip('*')


def remove_hash_and_strip(line):
    return line.lstrip('#')


""" COURSE SOLUTION
def markdown_to_text(doc_content):
    lines = doc_content.split("\n")

    new_lines = []
    for line in lines:
        header_removed = line.lstrip("#")
        emphasis_removed = remove_asterisks_from_words(header_removed)
        new_lines.append(emphasis_removed)

    return "\n".join(new_lines)


def remove_asterisks_from_words(line):
    words = line.split()
    for i, word in enumerate(words):
        if len(word) > 1:
            word = word.strip("*")
        if len(word) == 0:
            continue
        words[i] = word
    return " ".join(words)

"""


# TESTS


run_cases = [
    (
        """
# Header 1
This is a **bold statement**
I am #1
This is just plain text. No special markdown.

* This is a list
* lists don't need to change

Well sh*t.
""",
        """
Header 1
This is a bold statement
I am #1
This is just plain text. No special markdown.

* This is a list
* lists don't need to change

Well sh*t.
""",
    )
]

submit_cases = run_cases + [
    (
        """
# Todo List
*Wish* *Boots* *a* *Happy* *Birthday*
Buy a #21 Jersey
* Do my best
""",
        """
Todo List
Wish Boots a Happy Birthday
Buy a #21 Jersey
* Do my best
""",
    ),
    (
        """
# Hash header #

*Italics line*
**Bold line**

## Subheader

* List item
* *Italics list item*
* **Bold list item**
""",
        """
Hash header #

Italics line
Bold line

Subheader

* List item
* Italics list item
* Bold list item
""",
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input:")
    print(f'"{input1}"')
    print(f"Expecting:")
    print(f'"{expected_output}"')
    result = markdown_to_text(input1)
    print(f"Actual:")
    print(f'"{result}"')
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
