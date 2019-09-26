def find_first_duplicate_char(my_str):
    for i, char in enumerate(my_str):
        if my_str.find(char) != my_str.rfind(char):
            return char


print(find_first_duplicate_char('Datta'))


def remove_duplicate_chars(my_str):
    new_str = ''
    for i, char in enumerate(my_str):
        if my_str.find(char) == my_str.rfind(char):
            new_str += char
    return new_str


print(remove_duplicate_chars('Dattatray'))
