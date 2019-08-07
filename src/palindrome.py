def is_palindrome(my_str: str):
    str_len = len(my_str)
    half_len = int(str_len / 2)
    for i, char in enumerate(my_str[:half_len]):
        if char != my_str[str_len - i - 1:str_len - i]:
            return False
    return True


print(is_palindrome('MOM'))
print(is_palindrome('MADAM'))
print(is_palindrome('ABBA'))
