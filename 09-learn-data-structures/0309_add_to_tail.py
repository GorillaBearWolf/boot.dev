class LinkedList:
    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node



    # don't touch below this line

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val


run_cases = [
    ("Bow", ["Sword", "Bow"]),
    ("Axe", ["Sword", "Bow", "Axe"]),
    ("Staff", ["Sword", "Bow", "Axe", "Staff"]),
]

submit_cases = run_cases + [
    ("Spear", ["Sword", "Bow", "Axe", "Staff", "Spear"]),
    ("Dagger", ["Sword", "Bow", "Axe", "Staff", "Spear", "Dagger"]),
]


def test(linked_list, input, expected_state):
    print("---------------------------------")
    print(f"Linked List: {linked_list}")
    print(f"Adding to tail: {input}")
    print(f"Expecting: {expected_state}")
    linked_list.add_to_tail(Node(input))
    try:
        result = linked_list_to_list(linked_list)
    except Exception as e:
        result = f"Error: {e}"
    print(f"Actual: {result}")
    if result == expected_state:
        print("Pass")
        return True
    print("Fail")
    return False


def linked_list_to_list(linked_list):
    result = []
    for node in linked_list:
        result.append(node.val)

    return result


def main():
    passed = 0
    failed = 0
    linked_list = LinkedList()
    linked_list.add_to_tail(Node("Sword"))
    for test_case in test_cases:
        correct = test(linked_list, *test_case)
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
