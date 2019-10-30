def list_tagger(batch):
    list_length = len(batch)
    batch.insert(0, list_length)
    return batch

# print(list_tagger([0, 1, 2]))


def cutoff(int_list, int2):
    counter = 0
    for v in int_list:
        if v % int2 == 0:
            counter += 1
    return counter


# print(cutoff([0, 1, 2], 2))


def prepender(l_string, string2):
    for v in range(0, len(l_string)):
        l_string[v] = string2 + l_string[v]


# def name_list():


def multiples_of_3(upper_bound):
    every_value = [v for v in range(0, upper_bound)]
    sum_of_multiples = [x for x in every_value if x % 3 == 0]
    sum_of_values = 0
    for i in range(0, len(sum_of_multiples)):
        sum_of_values += sum_of_multiples[i]
    return sum_of_values


print(multiples_of_3(10))