def toggle_case(line):
    if line.istitle():
        return line.upper() + "!!!"
    if line.isupper():
        return line.capitalize().rstrip("!")
    if len(line) > 0 and line[1:].islower():
        return line.title()
    return line
