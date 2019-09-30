my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for a, b, c in zip(*[iter(my_list)] * 3):
    print(a, b, c)

a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)  # 1 [2, 3, 4] 5

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

print(f"{'*' * 10} Using print method arguments {'*' * 10}")
for i in range(3):
    print(i + 1, end='')
print('Above print statement will continue with this line')
print(f"{'*' * 10} Using print method arguments {'*' * 10}")

print(f"{'*' * 10} Even numbers {'*' * 10}")
even_nums = [num for num in range(2, 100, 2)]
print(even_nums)
print(f"{'*' * 10} Even numbers {'*' * 10}")

print(f"{'*' * 10} Transposing a Matrix {'*' * 10}")
mat = [[1, 2, 3], [4, 5, 6]]
for i in zip(*mat):  # same as zip(list1, list2)
    print(i)
print(f"{'*' * 10} Transposing a Matrix {'*' * 10}")

print(f"{'*' * 10} Reverse list {'*' * 10}")
dt_list = ['D', 'A', 'T', 'T', 'A']
print(dt_list.reverse())  # None
print(dt_list)  # ['A', 'T', 'T', 'A', 'D']
print(f"{'*' * 10} Reverse list {'*' * 10}")

import sys

gen = (i for i in range(100000))
print(f'Size (in bytes) aquired by generator {sys.getsizeof(gen)}')
li = [i for i in range(100000)]
print(f'Size (in bytes) aquired by list {sys.getsizeof(li)}')

dt_list = ['D', 'A', 'T', 'T', 'A']
print(dt_list.count('T'))
