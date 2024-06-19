def count_nested_levels(nested_documents, target_document_id, level=1):
    for key in nested_documents:
        print(f"tid={target_document_id},key={key},lvl={level}")
        if target_document_id == key:
            print(f"FOUND ON LEVEL: {level}")
            return level
        else:
            level += 1
            doc_level = count_nested_levels(nested_documents[level], target_document_id, level)
            print(f"dl={doc_level},lvl={level}")
            if doc_level == -1:
                level += doc_level
                continue
            return doc_level
    return -1

run_cases = [
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 1, 1),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 3, 3),
]

submit_cases = run_cases + [
    ({}, 1, -1),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 5, 4),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 10, 5),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 20, -1),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = count_nested_levels(input1, input2)
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
