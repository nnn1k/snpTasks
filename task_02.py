def coincidence(lst=None, rng=None):
    answer = []
    if not lst or not rng:
        return answer

    for el in lst:
        if type(el) not in (int, float):
            continue
        if rng.start <= el < rng.stop:
            answer.append(el)
    return answer
