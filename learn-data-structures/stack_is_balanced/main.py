from stack import Stack


def is_balanced(input_str):
    stack = Stack()

    for char in input_str:
        if char is '(':
            stack.push(char)
        elif char is ')':
            if stack.pop() is None:
                return False
    return stack.peek() is None
