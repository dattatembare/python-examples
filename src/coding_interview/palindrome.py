def is_palindrome(my_str: str):
    if not my_str:  # OR if my_str is None or my_str == '':
        return False

    try:
        str_len = len(my_str)
    except TypeError:
        return False

    half_len = str_len // 2  # OR int(str_len / 2)
    for i in range(half_len):
        if my_str[i] != my_str[str_len - i - 1]:
            return False
    return True


print(is_palindrome('A'))  # True
print(is_palindrome('AA'))  # True
print(is_palindrome('AAA'))  # True
print(is_palindrome('MOM'))  # True
print(is_palindrome('MADAM'))  # True
print(is_palindrome('ABBA'))  # True
print(is_palindrome('RACECAR'))  # True
print(is_palindrome('DATTA'))  # False
print(is_palindrome(''))  # False
print(is_palindrome(None))  # False
print(is_palindrome(10))  # False
