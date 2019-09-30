mat = [[1, 2, 3], [4, 5, 6]]
for i in zip(*mat):  # same as zip(list1, list2)
    print(i)
