def find_anagrams(word, candidates):
    expected = []
    word_sorted = sorted(word.lower())
    for candidate in candidates:
        candidate_sorted = sorted(candidate.lower())
        if len(word) == len(candidate) and word_sorted == candidate_sorted and word.lower() != candidate.lower():
            expected.append(candidate)

    return expected