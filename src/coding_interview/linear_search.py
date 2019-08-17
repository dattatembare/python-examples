def linear_search(alist, n):
    for i in range(len(alist)):
        if alist[i] == n:
            return True
    return False


def linear_search_with_index(alist, n):
    for i in range(0, len(alist)):
        if alist[i] == n:
            return True, i
    return False, None


my_list = [52, 25, 27, 72, 81, 18, 35, 13, 8, 5]

print(f'Number found in list {linear_search(my_list, 27)}')
print(f'Number found in list {linear_search(my_list, 72)}')
print(f'Number found in list {linear_search(my_list, 10)}')

print(f'Number found in list {linear_search_with_index(my_list, 27)}')
print(f'Number found in list {linear_search_with_index(my_list, 72)}')
print(f'Number found in list {linear_search_with_index(my_list, 10)}')
