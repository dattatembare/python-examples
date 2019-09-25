"""
A histogram is a concept from statistics. It is a graphical display that tells us about the distribution of the samples
involved. They are commonly a picture made from a table with many categories.
The table tells how many samples there are in each category.
"""


def count_ele(seq):
    my_dict = {}
    for i in seq:
        my_dict[i] = my_dict.get(i, 0) + 1
    return my_dict


my_list = [0, 1, 3, 7, 2, 1, 11, 23, 1, 3]
print(count_ele(my_list))
# {0: 1, 1: 3, 3: 2, 7: 1, 2: 1, 11: 1, 23: 1}
