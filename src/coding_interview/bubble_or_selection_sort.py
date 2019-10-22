"""
Bubble sort or selection sort is less efficient than merge sort, time complexity is O(n^2) in average case.
"""


def sort_array(my_list):
    """sort array or bubble array"""

    for j in range(len(my_list) - 1):
        for i in range(len(my_list) - j - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list


my_list = [52, 25, 27, 72, 81, 18, 35, 13, 8, 5]
print(f'My sorted array: {sort_array(my_list)}')
