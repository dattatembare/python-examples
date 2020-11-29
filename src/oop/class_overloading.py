class TestOverload:

    def __init__(self):
        print('inside init')

    def __init__(self, name):
        print(f'name:{name}')

    def __init__(self, name, age):
        print(f"n:{name}, a:{age}")

# i = TestOverload()
# print(i)
# Traceback (most recent call last):
#   File "C:/Users/DattatrayaTembare/PycharmProjects/python-examples/src/oop/class_overloading.py", line 12, in <module>
#     i = TestOverload()
# TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'

# o = TestOverload("Datta")
# print(o)
# Traceback (most recent call last):
#   File "C:/Users/DattatrayaTembare/PycharmProjects/python-examples/src/oop/class_overloading.py", line 9, in <module>
#     o = TestOverload("Datta")
# TypeError: __init__() missing 1 required positional argument: 'age'

o = TestOverload("Datta", 40)
print(o)
# n:Datta, a:40
# <__main__.TestOverload object at 0x0000015E9C4C84A8>


class NewClass:

    def m1(self, m):
        print(m)

    def m1(self, m, l):
        print(m, l)


n = NewClass()
# print(n.m1(1))
# Traceback (most recent call last):
#   File "C:/Users/DattatrayaTembare/PycharmProjects/python-examples/src/oop/class_overloading.py", line 35, in <module>
#     print(n.m1(1))
# TypeError: m1() missing 1 required positional argument: 'l'
print(n.m1(1,2))
# <__main__.TestOverload object at 0x000002370517C5C0>
# 1 2
# None