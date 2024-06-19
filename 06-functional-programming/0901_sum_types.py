doc_type_pdf = "pdf"
doc_type_txt = "txt"
doc_type_docx = "docx"
doc_type_md = "md"
doc_type_html = "html"


def conversion_type(doc_type):
    if doc_type == doc_type_pdf:
        return doc_type_html
    if doc_type == doc_type_txt:
        return doc_type_pdf
    if doc_type == doc_type_docx:
        return doc_type_md
    if doc_type == doc_type_md:
        return doc_type_pdf
    if doc_type == doc_type_html:
        return doc_type_txt
    raise Exception('Unknown document type')


run_cases = [
    (doc_type_pdf, doc_type_html),
    (doc_type_txt, doc_type_pdf),
    (doc_type_docx, doc_type_md),
    ("pptx", "Unknown document type"),
    ("xls", "Unknown document type"),
    (doc_type_md, doc_type_pdf),
    (doc_type_html, doc_type_txt),
]

submit_cases = run_cases + [
    (doc_type_docx, doc_type_md),
    ("png", "Unknown document type"),
    (doc_type_md, doc_type_pdf),
    ("jpeg", "Unknown document type"),
    ("gif", "Unknown document type"),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    try:
        result = conversion_type(input1)
        print(f"Actual: {result}")
        if result == expected_output:
            print("Pass")
            return True
    except Exception as e:
        print(f"Actual: {str(e)}")
        if str(e) == expected_output:
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
