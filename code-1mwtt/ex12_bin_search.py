def bin_search(xs, x):
    # return the least index of an element equal to x sorted x
    low = 0
    high = len(xs)
    while low + 1 < high:
        guess = (low + high) // 2
        if x < xs[guess]:
            high = guess
        else:
            low = guess
    return low

def test(test_case_xs, test_case_x, expected):
    actual = bin_search(test_case_xs, test_case_x)
    if actual == expected:
        print("Passed test for " + test_case_x)
    else:
        print("Didn't pass test for " + test_case_x)
        print("The result was " + str(actual) + " but it should have been " + str(expected))

test([], "x", 0)
test(["code", "learn", "to"], "code", 0)
test(["code", "learn", "to"], "learn", 1)
test(["code", "learn", "to"], "to", 2)


sentence = "A brownish cloud descends every Friday, growing, hovering impressively, jeopardously keeping low, moving nimbly over populated quarters, returning silently to unknown, violently wild xylogenic yttriferous zones."

words = sentence.lower().split(" ")

for i in range(0, len(words)):
    test(words, words[i], i)