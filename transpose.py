from functools import reduce
from itertools import zip_longest


def transpose(text):
    return '\n'.join(
        reduce(
            lambda columns, t: [
                a.ljust(t[0] if b else 0) + b
                for a, b in zip_longest(
                    columns,
                    t[1],
                    fillvalue=''
                )
            ],
            enumerate(text.split('\n')),
            []
        )
    )

text = "The longest line.\nA long line.\nA longer line.\nA line."
expected = "TAAA\nh   \nelll\n ooi\nlnnn\nogge\nn e.\nglr\nei \nsnl\ntei\n .n\nl e\ni .\nn\ne\n."

result = transpose(text)
print("Result:\n", result)
print("Expected:\n", expected)
print("Match:", result == expected)