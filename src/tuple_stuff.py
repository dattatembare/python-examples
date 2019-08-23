first, second, *rest = (1, 2, 3, 4, 5, 6, 7, 8)
print(first)  # 1
print(second)  # 2
print(rest)  # [3, 4, 5, 6, 7, 8]

first, *rest, last = (1, 2, 3, 4, 5, 6, 7, 8)
print(first)  # 1
print(rest)  # [2, 3, 4, 5, 6, 7]
print(last)  # 8
