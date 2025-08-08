def combine_anagrams(words_array):
    groups = {}

    for word in words_array:
        sorted_letters = "".join(sorted(word.lower()))

        if sorted_letters not in groups:
            groups[sorted_letters] = []
        groups[sorted_letters].append(word)

    return list(groups.values())


