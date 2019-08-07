A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i: i * i for i in A1}
A6 = [[i, i * i] for i in A1]

print(A0)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)


# import this  # --> Print 19 verses called as "Zen of python"
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

def multiplexers():
    return [lambda n: index * n for index in range(4)]


print([m(2) for m in multiplexers()])


# [6, 6, 6, 6]
# The output of the above code is <[6, 6, 6, 6]>. It’s because of the late binding as the value of the variable <index>
# gets looked up after a call to any of multiplexers functions.

###########

def fast(items=[]):
    items.append(1)
    return items


print(fast())  # [1]
print(fast())  # [1, 1]

############
# print(float('Datta'))  # ValueError: could not convert string to float: 'Datta'

my_str = 'abcd'
my_str = my_str[::-1]
print(my_str)  # dcba

my_arr = [1, 2, 3, 4]
my_arr = my_arr[::-1]
print(my_arr)  # [4, 3, 2, 1]

mul = lambda x, y: x * y
print(mul(2, 3))

import datetime

print(datetime.datetime.now())

a = "Datta Tembare"
print(a.split())  # ['Datta', 'Tembare']

b = 'Datta'
print(f'Use of split:: {b.split()}')  # ['Datta']
