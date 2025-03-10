class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"


# dont touch above this line


def vanity(influencer):
    return influencer.num_bio_links * 5 + influencer.num_selfies

def vanity_sort(influencers):
    return sorted(influencers, key=vanity)


# TESTS

theprimeagen = Influencer(100, 1)
pokimane = Influencer(800, 2)
spambot = Influencer(0, 200)
lane = Influencer(10, 2)
badcop = Influencer(1, 2)

run_cases = [
    ([badcop, lane], [badcop, lane]),
    ([lane, badcop, pokimane], [badcop, lane, pokimane]),
    ([spambot, theprimeagen], [theprimeagen, spambot]),
]

submit_cases = run_cases + [
    ([], []),
    ([lane], [lane]),
    (
        [pokimane, theprimeagen, spambot, badcop, lane],
        [badcop, lane, theprimeagen, pokimane, spambot],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input:\n * {input1}")
    print(f"Expecting: {expected_output}")
    result = vanity_sort(input1)
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
