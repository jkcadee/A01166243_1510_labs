def sparse_add(dict1, dict2):
    new_dict = dict()
    for key in dict1:
        if key in dict2:
            new_dict[key] = dict1[key] + dict2[key]
        else:
            new_dict[key] = dict1[key]
    for key in dict2:
        if key not in new_dict:
            new_dict[key] = dict2[key]
    sorted_keys = sorted(new_dict)
    sorted_dict = {}
    for index in sorted_keys:
        if new_dict[index] == 0:
            continue
        sorted_dict[index] = new_dict[index]
    return sorted_dict


print(sparse_add({1: 2, 2: 3, 6: 7}, {1: -2, 3: 4, 4: 4}))

