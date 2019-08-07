def sort_array(my_list):
    """sort array or bubble array"""

    for j in range(len(my_list)):
        for i in range(j, len(my_list)):
            if my_list[j] > my_list[i]:
                temp = my_list[j]
                my_list[j] = my_list[i]
                my_list[i] = temp
    return my_list


my_list = [52, 25, 27, 72, 81, 18, 35, 13, 8, 5]
print(f'My sorted array: {sort_array(my_list)}')
