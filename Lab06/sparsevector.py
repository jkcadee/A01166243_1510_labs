def sparse_add(dict1, dict2):
    for each_key, each_value in dict1.items() and dict2.items():
        if each_key == each_key:
            updated_vector = dict1[each_key] + dict2[each_key]
            new_sum_dict = {**dict1, **dict2}
            return new_sum_dict
        else:
            return {**dict1, **dict2}


print(sparse_add({'A': 2, 'B': 3}, {'A': 4, 'C': 4}))
