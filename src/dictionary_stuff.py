d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d)
print(d.popitem())
print(d)

# Merge two dictionaries
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)  # {'a': 1, 'b': 3, 'c': 4}
zz = {**y, **x}
print(zz)  # {'b': 2, 'c': 4, 'a': 1}

# How to sort a Python dict by value (== get a representation sorted by value)

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

########################################################

# The get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}


def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")


print(greeting(382))  # "Hi Alice!"
print(greeting(333333))  # "Hi there!"

#  Inverting a dictionary using zip
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(m.items())  # [('a', 1), ('c', 3), ('b', 2), ('d', 4)]
print(dict(zip(m.values(), m.keys())))  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# Inversing a dictionary using dict comprehensions
m1 = {v: k for k, v in m.items()}
print(m1)

# Deleting element from dictionary
print(m.pop('a'))
print(m)
print(m.clear())

seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print(f"New Dictionary : {dict}")

dict = dict.fromkeys(seq, 'null')  # New Dictionary : {'name': None, 'age': None, 'sex': None}
print(f"New Dictionary : {str(dict)}")  # New Dictionary : {'name': 'null', 'age': 'null', 'sex': 'null'}
