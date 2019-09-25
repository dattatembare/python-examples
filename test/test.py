def is_palindrome(my_str):
    if not my_str:
        return False

    try:
        str_len = len(my_str)
    except TypeError:
        return False

    half_len = str_len // 2
    for num in range(half_len):
        if my_str[num] != my_str[str_len - num - 1]:
            return False
    return True


print(is_palindrome(10))
