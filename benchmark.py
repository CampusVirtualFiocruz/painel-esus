import timeit

setup = """
def original_mock(phrase, gap=2, skip_first=False):
    words = phrase.split()
    if skip_first and len(words)>1:
        return " ".join(
            [
                words[0],
                *[
                    word[:gap] + "".join(["*" for n in word[gap:]])
                    for word in words[1:]
                ],
            ]
        )
    else:
        return " ".join(
            [word[:gap] + "".join(["*" for n in word[gap:]]) for word in words]
        )

def optimized_mock(phrase, gap=2, skip_first=False):
    words = phrase.split()
    if skip_first and len(words)>1:
        return " ".join(
            [
                words[0],
                *[
                    word[:gap] + "*" * len(word[gap:])
                    for word in words[1:]
                ],
            ]
        )
    else:
        return " ".join(
            [word[:gap] + "*" * len(word[gap:]) for word in words]
        )

def optimized_mock_max(phrase, gap=2, skip_first=False):
    words = phrase.split()
    if skip_first and len(words)>1:
        return " ".join(
            [
                words[0],
                *[
                    word[:gap] + "*" * max(0, len(word) - gap)
                    for word in words[1:]
                ],
            ]
        )
    else:
        return " ".join(
            [word[:gap] + "*" * max(0, len(word) - gap) for word in words]
        )

phrase = "Hello world this is a test phrase with multiple words to anonymize."
"""

print("Original:", timeit.timeit("original_mock(phrase, 2, True)", setup=setup, number=100000))
print("Optimized (len(slice)):", timeit.timeit("optimized_mock(phrase, 2, True)", setup=setup, number=100000))
print("Optimized (max):", timeit.timeit("optimized_mock_max(phrase, 2, True)", setup=setup, number=100000))
