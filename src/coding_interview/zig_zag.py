"""
Second coding round with Cigna
"""


class ZigZag:

    def convert(self, in_str: str, num_row: int) -> None:
        """
        # Algorithm
        # when x = 0 or interval (num-1) or multiple of intervals -> print chars in all rows (n)
        # when x == y  or x - interval or x - (multiple of intervals) -> print char in that position only
        # Edge and negative cases:
        ## '' str -> print empty str
        ## when num_row = 1 -> print str as is (no zig zag)
        ## when num_row <=0 -> print error message

        :param in_str:
        :param num_row:
        :return: None
        """
        if not in_str or num_row == 1:
            print(in_str)
            return

        if num_row <= 0:
            print(f'Number of rows enetered {num_row} is not valid')
            return

        char_index = 0
        in_str_len = len(in_str)
        interval = num_row - 1  # Using 0 position list so interval is -1

        # Find the positions
        overall_list = []
        for x in range(in_str_len):
            # break the loop when all the chars of string collected
            if char_index >= in_str_len:
                break

            x_position = x if x <= interval else x % interval
            row_list = []
            for y in range(num_row - 1, -1, -1):  # range in revrese order Ex 4 to 1
                if x % interval == 0 or x_position == y:
                    row_list.append(in_str[char_index:char_index + 1])
                    char_index += 1
                else:
                    row_list.append(' ')

            overall_list.append(row_list)

        self.print_zig_zag(num_row, overall_list)

    def print_zig_zag(self, num_row: int, overall_list: list) -> None:
        """
        Print the output in Zig Zag
        :param num_row:
        :param overall_list:
        :return: none
        """
        for row_idx in range(num_row):
            for idx in range(len(overall_list)):
                print(overall_list[idx][row_idx], end=" ")
            print("\n")


z = ZigZag()
# Print zig zag
print('*' * 25)
z.convert('HELLOWORLDANDME', 4)
print('*' * 25)
z.convert('HELLOWORLDANDME', 3)
print('*' * 25)
z.convert('THEROOM', 3)
print('*' * 25)
z.convert('THE', 3)
print('*' * 25)
z.convert('HI', 2)
print('*' * 25)
z.convert('IAMCHECKINGTHEBIGSTRINGWITHBIGNUMBEROFROWSHOPEYOUWOULDLIKEIT', 9)

# Edge and negative test cases
print('*' * 25)
z.convert('I', 1)
print('*' * 25)
z.convert('HI', 1)
print('*' * 25)
z.convert('HELLO', 0)
print('*' * 25)
z.convert('', 0)
print('*' * 25)
z.convert('HELLO', -2)
print('*' * 25)

# OUTPUT:
#
# C:\Users\DattatrayaTembare\PycharmProjects\python-examples\venv\Scripts\python.exe C:/Users/DattatrayaTembare/PycharmProjects/python-examples/test/zig_zag.py
# *************************
# H     O     D
#
# E   W R   N M
#
# L O   L A   E
#
# L     D
#
# *************************
# H   O   L   D
#
# E L W R D N M
#
# L   O   A   E
#
# *************************
# T   O
#
# H R O
#
# E   M
#
# *************************
# T
#
# H
#
# E
#
# *************************
# H
#
# I
#
# *************************
# I               G               M               U
#
# A             I S             U B             O W
#
# M           B   T           N   E           Y   O
#
# C         E     R         G     R         E     U
#
# H       H       I       I       O       P       L
#
# E     T         N     B         F     O         D     T
#
# C   G           G   H           R   H           L   I
#
# K N             W T             O S             I E
#
# I               I               W               K
#
# *************************
# I
# *************************
# HI
# *************************
# Number of rows enetered 0 is not valid
# *************************
#
# *************************
# Number of rows enetered -2 is not valid
# *************************
#
# Process finished with exit code 0
