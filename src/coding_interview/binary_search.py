def sort_array(my_list):
    """sort array or bubble array"""

    for j in range(len(my_list) - 1):
        for i in range(len(my_list) - j - 1):
            if my_list[i] > my_list[i + 1]:
                # temp = my_list[i]
                # my_list[i] = my_list[i + 1]
                # my_list[i + 1] = temp
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # equivalent to above 3 lines
    return my_list


print(sort_array(my_list=[52, 25, 27, 72, 81, 18, 35, 13, 8, 5]))


def sort_array_dec(my_list):
    """sort array or bubble array"""

    for j in range(len(my_list) - 1):
        for i in range(len(my_list) - j - 1):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list


print(sort_array_dec(my_list=[52, 25, 27, 72, 81, 18, 35, 13, 8, 5]))


def binary_search_iterative(alist, n):
    """
    Primarry requirement for binary search engine is provided list should be sorted
    """
    slist = sort_array(alist)
    # Alternative sorts
    # slist = sorted(alist)
    # alist.sort() <- return None

    first = 0
    last = len(slist) - 1

    while first <= last:
        middle = (first + last) // 2
        if n == slist[middle]:
            return True
        elif n < slist[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return False


def binary_search_with_index(alist, n):
    slist = sort_array(alist)

    first = 0
    last = len(slist) - 1

    while first <= last:
        middle = (first + last) // 2
        if n == slist[middle]:
            return True, alist.index(n)
        elif n < slist[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return False, None


def binary_search_recursive(slist, n, first, last):
    if first > last:
        return False
    else:
        middle = (first + last) // 2
        if n == slist[middle]:
            return True
        elif n < slist[middle]:
            return binary_search_recursive(slist, n, first=first, last=middle - 1)
        else:
            return binary_search_recursive(slist, n, first=middle + 1, last=last)


my_list = [52, 25, 27, 72, 81, 18, 35, 13, 8, 5]

print(sorted(my_list))
print(my_list[-1])  # last index

print(f'Number found in list {binary_search_iterative(my_list, 27)}')
print(f'Number found in list {binary_search_iterative(my_list, 72)}')
print(f'Number found in list {binary_search_iterative(my_list, 10)}')

print(f'Number found in list {binary_search_with_index(my_list, 27)}')
print(f'Number found in list {binary_search_with_index(my_list, 72)}')
print(f'Number found in list {binary_search_with_index(my_list, 10)}')

my_list = sorted(my_list)
print(f'Number found in list {binary_search_recursive(my_list, 27, 0, len(my_list) - 1)}')
print(f'Number found in list {binary_search_recursive(my_list, 72, 0, len(my_list) - 1)}')
print(f'Number found in list {binary_search_recursive(my_list, 10, 0, len(my_list) - 1)}')
