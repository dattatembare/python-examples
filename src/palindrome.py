def is_palindrome(my_str: str):
    if my_str is None or my_str == '':
        return False
    str_len = len(my_str)
    half_len = str_len // 2  # int(str_len / 2)
    for i in range(half_len):
        if my_str[i] != my_str[str_len - i - 1]:
            return False
    return True


print(is_palindrome('AA'))
print(is_palindrome('MOM'))
print(is_palindrome('MADAM'))
print(is_palindrome('ABBA'))
print(is_palindrome('RACECAR'))
print(is_palindrome('DATTA'))
print(is_palindrome(''))
print(is_palindrome(None))
