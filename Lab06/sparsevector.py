# This function only works if there are no leading or trailing zeros if you need to measure the actual length of the
# sparse vector.
import doctest


def sparse_add(dict1, dict2):
    """Return a sorted dictionary (sparse vector) of two combined dictionaries
    >>> sparse_add({}, {})
    {}
    >>> sparse_add({2:3, 4:5}, {2:1, 3:6})
    {2: 4, 3: 6, 4: 5}
    >>> sparse_add({3:5, 6:7}, {1:9, 10:7})
    {1: 9, 3: 5, 6: 7, 10: 7}
    """
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


"""
Return a dictionary with the combined values of two sparse dictionaries, sorted in the correct order.

:param dict1: A dictionary.
:param dict2: A dictionary.
:precondition: Each parameter dictionary must have at least one value in it, and it must be positive.
:postcondition: Return a dictionary, with all the values from the two parameter dictionaries combined into it.
:return: A dictionary with both parameter dictionary's values inside of it.
"""


def main():
    """Run the program"""
    print(sparse_add({1: 2, 2: 3, 6: 7}, {1: 1, 3: 4, 4: 4}))


if __name__ == "__main__":
    main()
    doctest.testmod()
