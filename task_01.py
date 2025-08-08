def is_palindrome(input_value):
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    if not isinstance(input_value, str):
        input_value = str(input_value)

    translator = str.maketrans('', '', punctuation + ' ')
    cleaned = input_value.translate(translator).lower()

    print(cleaned == cleaned[::-1])
    return cleaned == cleaned[::-1]

