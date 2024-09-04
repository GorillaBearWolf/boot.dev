def args_logger(*args, **kwargs):
    i = 1
    for arg in args:
        print(f"{i}. {arg}")
        i += 1
    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")


def test(*args, **kwargs):
    args_logger(*args, **kwargs)
    print("========================================")


def main():
    test("Good", "riddance", date_str="01/01/2023")
    test(message="Hello World", to_delete="l")
    test("two", "star-crossed", "lovers")
    test("hi", True, f_name="Lane", l_name="Wagner", age=28)


main()

