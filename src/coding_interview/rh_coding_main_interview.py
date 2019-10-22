# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# Jafar - White - o
# Aladdin - Black - x
# empty field by .

def o_possible_moves(p, N):
    p_list = []
    for i in range(1, 3):
        # left
        if p[0] - i > 0 or p[1] - i > 0:
            p_list.append([p[0] - i, p[1] - i])
        # right
        if p[0] - i > 0 or p[1] + i < N - 1:
            p_list.append([p[0] - i, p[1] + i])

    return p_list


def solution(B):
    # write your code in Python 3.6
    N = len(B)
    if 2 <= N <= 30:
        o_list = []
        x_list = []
        for i, char_str in enumerate(B):
            # all "return 0" are corner cases, if case is not valid then return 0
            if N != len(char_str):
                return 0

            for j, char in enumerate(char_str):
                if char not in ['X', 'O', '.']:
                    return 0
                else:
                    if char == 'O':
                        o_list.append([i, j])
                    elif char == 'X':
                        x_list.append([i, j])

        if len(o_list) > 1:
            return 0

        # "o" possible moves
        o_moves = o_possible_moves(o_list[0], N)
        # check left side
        left_removed = 0
        if o_moves[0] in x_list:
            left_removed += 1
            if len(o_moves) > 2:
                o_moves_next = o_possible_moves(o_moves[2], N)
                for m in range(1, len(o_moves_next), 2):
                    if o_moves_next[m - 1] in x_list:
                        left_removed += 1

        # check right side
        right_removed = 0
        if o_moves[1] in x_list:
            right_removed += 1
            if len(o_moves) > 3:
                o_moves_next = o_possible_moves(o_moves[3], N)
                for m in range(1, len(o_moves_next), 2):
                    if o_moves_next[m - 1] in x_list:
                        right_removed += 1

        return left_removed if left_removed > right_removed else right_removed

    else:
        return 0


b = [
    "..X...",
    "......",
    "....X.",
    ".X....",
    "..X.X.",
    "...O.."
]
print(solution(b))
