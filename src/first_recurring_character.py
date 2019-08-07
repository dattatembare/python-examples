def first_recurring_char(myStr):
    for index, char in enumerate(myStr):
        if char in myStr[index + 1:]:
            return char


def recurring_char_arr(myStr):
    return [char for index, char in enumerate(myStr) if char in myStr[index + 1:]]


print(first_recurring_char('DATTA'))
print(recurring_char_arr('DATTA'))
