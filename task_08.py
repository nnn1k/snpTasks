def multiply_numbers(inputs=None):
    if inputs is None:
        return None

    multiply = None

    for el in str(inputs):
        if el not in "0123456789":
            continue
        if multiply is None:
            multiply = int(el)
        else:
            multiply *= int(el)
    print(multiply)
    return multiply
