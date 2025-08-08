def count_words(string: str):
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    for char in string:
        if char in punctuation:
            string = string.replace(char, '')
    answer = {}
    for word in string.lower().split():
        if not answer.get(word):
            answer[word] = 1
        else:
            answer[word] += 1

    print(answer)
    return answer

