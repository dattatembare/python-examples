from filecmp import cmp

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d.popitem())  # ('d', 4)
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# Merge two dictionaries
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)  # {'a': 1, 'b': 3, 'c': 4}
zz = {**y, **x}
print(zz)  # {'b': 2, 'c': 4, 'a': 1}

a = {'x': 1, 'y': 2}
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
zzz = {**x, **y, **a}
print(zzz)
# {'a': 1, 'b': 3, 'c': 4, 'x': 1, 'y': 2}


# How to sort a Python dict by value (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
print(xs.items())
# dict_items([('a', 4), ('b', 3), ('c', 2), ('d', 1)])
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


#############################

def test_dict(value):
    key_value = 'OTHR:1, DRT: 2'
    kv_dict = {kv[0].strip(): kv[1].strip() for kv in [vals.strip().split(':') for vals in key_value.split(',')]}
    return kv_dict.get(value, value)


print(test_dict('OTHR'))
print(test_dict('DRT'))
print(test_dict('123'))


class A:
    num = 10


a = A()

print(a.__dict__)  # {}
print(A.__dict__)
# {'__module__': '__main__', 'num': 10,
# '__dict__': <attribute '__dict__' of 'A' objects>,
# '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}

# Type check
print(type(A))
# <class 'type'>
print(type(a))
# <class '__main__.A'>
print(type(a.__dict__))
# <class 'dict'>
print(type(A.__dict__))
# <class 'mappingproxy'>
print(type(type.__dict__))
# <class 'mappingproxy'>
print(type(A.__dict__['__dict__']))
# <class 'getset_descriptor'>
print(type(type.__dict__['__dict__']))
# <class 'getset_descriptor'>
print(a.__dict__ == A.__dict__['__dict__'].__get__(a))
# True
print(A.__dict__ == type.__dict__['__dict__'].__get__(A))
# True
print(a.__dict__ == type.__dict__['__dict__'].__get__(A)['__dict__'].__get__(a))
# True


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print()

test_dict = {None: 'Test', None: 'Test1', None: 'Test2',
             'name': 'Datta', 'name': 'Dattatraya',
             'lname': 'Tembare'
             }
print(test_dict)
# {None: 'Test2', 'name': 'Dattatraya', 'lname': 'Tembare'}

print(my_dict.items() == test_dict.items())
# False
