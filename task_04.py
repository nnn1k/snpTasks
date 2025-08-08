def sort_list(lst):
    if not lst:
        return []
    minn, maxx = lst[0], lst[0]
    minn_index, maxx_index = [], []
    for i, el in enumerate(lst):
        if el == minn:
            minn_index.append(i)
        if el == maxx:
            maxx_index.append(i)
        if el < minn:
            minn = el
            minn_index = [i]
        if el > maxx:
            maxx = el
            maxx_index = [i]

    for i in minn_index:
        lst[i] = maxx
    for i in maxx_index:
        lst[i] = minn
    lst.append(minn)
    return lst
