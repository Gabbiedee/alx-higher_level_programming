#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_list = sorted(list(a_dictionary.keys()))

    for x in keys_list:
        print("{}: {}".format(x, a_dictionary.get(x)))