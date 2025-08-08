def connect_dicts(dict1, dict2):
    new_dict = {}
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())

    priority_dict = dict2 if sum2 >= sum1 else dict1
    secondary_dict = dict1 if priority_dict is dict2 else dict2

    for key, value in secondary_dict.items():
        if value >= 10:
            if key not in priority_dict:
                new_dict[key] = value

    for key, value in priority_dict.items():
        if value >= 10:
            new_dict[key] = value

    sorted_result = dict(sorted(new_dict.items(), key=lambda item: item[1]))
    return sorted_result


