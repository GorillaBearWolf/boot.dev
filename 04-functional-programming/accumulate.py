import functools


def accumulate(doc, sentence):
    if not doc or doc == "":
        return sentence
    return doc + ". " + sentence


def accumulate_first_sentences(sentences, n):
    if not sentences or sentences == []:
        return ""
    if len(sentences) <= n:
        return functools.reduce(accumulate, sentences) + "."
    return functools.reduce(accumulate, sentences[:n]) + "."


# def accumulate(doc, sentence):
#     if doc.split("\n")[0] == sentence:
#         return doc.split("\n")[0]
#     else:
#         return ". ".join(doc, sentence)



# def accumulate_first_sentences(sentences, n):
#     if sentences == []:
#         return ""
#     else:
#         return ". ".join(sentences[:n]) + "."


# Don't edit below this line


def test(sentences, n):
    print("Input:")
    print(f"> n: {n}")
    print("> sentences:")
    for sentence in sentences:
        print(f"  * {sentence}")
    print("-------------------------------------")
    summary = accumulate_first_sentences(sentences, n)
    print("Output:")
    print(summary)
    print("=====================================")


def main():
    test(
        [
            "The world is changed",
            "I feel it in the water",
            "I feel it in the earth",
            "I smell it in the air",
            "Much that once was is lost, for none now live who remember it",
        ],
        3,
    )
    test(
        [
            "It began with the forging of the Great Rings",
            "Three were given to the Elves, immortal, wisest and fairest of all beings",
            "Seven to the Dwarf lords, great miners and craftsmen of the mountain halls",
            "And nine, nine rings were gifted to the race of Men, who above all else desire power",
        ],
        2,
    )
    test([], 0)


main()
