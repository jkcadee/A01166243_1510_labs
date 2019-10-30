def list_tagger(batch):
    list_length = len(batch)
    batch.insert(0, list_length)
    return batch

# print(list_tagger([0, 1, 2]))

# def cutoff():


def pre(l_string, string2):
    for v in range(0, len(l_string)):
        l_string[v] = string2 + l_string[v]