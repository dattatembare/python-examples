def merge(left, right):
    result = []
    left_point = 0
    right_point = 0

    while left_point < len(left) and right_point < len(right):
        if left[left_point] < right[right_point]:
            result.append(left[left_point])
            left_point += 1
        else:
            result.append(right[right_point])
            right_point += 1
    result.extend(left[left_point:])
    result.extend(right[right_point:])

    return result


def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    mid_point = len(my_list) // 2

    left, right = merge_sort(my_list[:mid_point]), merge_sort(my_list[mid_point:])

    return merge(left, right)


print(merge_sort([8, 6, 7, 4, 2, 1]))
