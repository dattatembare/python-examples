my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for a, b, c in zip(*[iter(my_list)] * 3):
    print(a, b, c)
