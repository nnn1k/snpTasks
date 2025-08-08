def max_odd(array):
    maxx = None
    for el in array:
        if type(el) not in (int, float):
            continue
        if int(el) % 2 == 0:
            continue
        if maxx is None:
            maxx = int(el)
        if el > maxx:
            maxx = int(el)

    return maxx
