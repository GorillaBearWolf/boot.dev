def remove_invalid_lines(document):
    return "\n".join(list(filter(lambda line: not line.startswith("-"), document.splitlines(keepends=True))))


# Don't edit below this line


def test(document):
    print("Input:")
    print(document)
    print("-------------------------------------")
    print("Output:")
    print(remove_invalid_lines(document))
    print("=====================================")


def main():
    test(
        """# My Essay
* How we win
- How you lose
* Why you're bad
"""
    )
    test(
        """# The Plan
* Phase 1
- ???
- Profit
Any questions?
"""
    )


main()
