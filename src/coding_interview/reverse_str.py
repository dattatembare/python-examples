# It works by doing [begin:end:step]
print('DATTA'[::-1])

print(''.join(reversed('DATTA')))


def my_rev(my_str):
    str_len = len(my_str)
    new_str = ''
    while str_len != 0:
        new_str += my_str[str_len - 1:str_len]
        str_len -= 1
    return new_str


def rev_str_for(my_str):
    new_str = ''
    for i in range(len(my_str), 0, -1):
        new_str += my_str[i - 1]
    return new_str


print(my_rev('DATTA'))
print(rev_str_for('DATTA'))
