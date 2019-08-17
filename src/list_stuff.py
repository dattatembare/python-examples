my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for a, b, c in zip(*[iter(my_list)] * 3):
    print(a, b, c)

a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)

a = [0, 1, 2, 3, 4, 5]
LASTTHREE = slice(-3, None)
print(LASTTHREE)  # slice(-3, None, None)
print(a[LASTTHREE])  # [3, 4, 5]
print(a[-3::])  # [3, 4, 5]

##########################################################
#  Flattening lists:
# Note: according to Python's documentation on sum, itertools.chain.from_iterable is the preferred method for this.
import itertools

a = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a)))  # [1, 2, 3, 4, 5, 6]
print(sum(a, []))  # [1, 2, 3, 4, 5, 6]
