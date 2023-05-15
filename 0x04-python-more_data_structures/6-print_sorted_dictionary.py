#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        dic_keys = a_dictionary.items()
        sorted_dict = sorted(dic_keys)
        return (dict(sorted_dict))
    return (0)