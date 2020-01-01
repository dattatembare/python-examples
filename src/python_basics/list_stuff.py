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

# return list with max sum
data = [[1, 2, 3, 4], [1, 2, 3, 3], [1, 1], [3, 3, 3, 3, 3, 3]]
print(max(data, key=sum))
# [3, 3, 3, 3, 3, 3]

my_str_is_list = 'String is list of sequences'
for seq in my_str_is_list:
    print(seq, end='')  # String is list of sequences

for seq in my_str_is_list.split(' '):
    print(seq, end='')  # Stringislistofsequences

for seq in my_str_is_list.split(' '):
    print(seq, end=' ')  # String is list of sequences

print('')
x = range(10)
print(x)
print(type(x))

a_list = [1, 2, 3, 4, 5]
nums = ','.join(map(str, a_list))
print(nums)  # 1,2,3,4,5
print(reversed(a_list))  # c<list_reverseiterator object at 0x000001547A85DC88>
print(list(reversed(a_list)))  #[5, 4, 3, 2, 1]

my_str = "Datta"
print([my_str].count('Datta'))  # 1
print([my_str].count('D'))  # 0
