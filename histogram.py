def count_ele(seq):
    my_dict = {}
    for i in seq:
        my_dict[i] = my_dict.get(i, 0) + 1
    return my_dict


my_list = [0, 1, 3, 7, 2, 1, 11, 23, 1, 3]
print(count_ele(my_list))
