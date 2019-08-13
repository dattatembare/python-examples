# Merge two dictionaries
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)  # {'a': 1, 'b': 3, 'c': 4}
zz = {**y, **x}
print(zz)  # {'b': 2, 'c': 4, 'a': 1}

# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

xs = sorted(xs.items(), key=lambda x: x[1])
print(xs)
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

import operator

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
xs = sorted(xs.items(), key=operator.itemgetter(1))
print(xs)
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
