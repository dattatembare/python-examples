def first_recurring_char(myStr):
    for index, char in enumerate(myStr):
        if char in myStr[index + 1:]:
            return char


def recurring_char_arr(myStr):
    return [char for index, char in enumerate(myStr) if char in myStr[index + 1:]]


print(first_recurring_char('DATTA'))
print(recurring_char_arr('DATTA'))


def first_recurring_char_dict(myStr):
    recur = {}
    for char in myStr:
        recur[char] = recur.get(char, 0) + 1
        if recur.get(char) == 2:
            return char

    return None


print(first_recurring_char_dict('DATTA'))  # T
print(first_recurring_char_dict('Python'))  # None
