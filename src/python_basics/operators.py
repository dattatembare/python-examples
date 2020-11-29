# FLOOR DIVISION OPERATOR
print(10 // 5)  # 2
print(10 // 5.0)  # 2.0
print(10.0 // 5)  # 2.0
print(10.0 // 5.0)  # 2.0


def foo(required, *args, **kwargs):
    print(required)  # print whatever type sent as an input
    if args:
        print(args)  # print tuple
    if kwargs:
        print(kwargs)  # print dictionary


print(foo('Datta'))
# Datta
# None
print(foo('Datta', 1, 2, 3))
# Datta
# (1, 2, 3)
# None
print(foo('Datta', 1, 2, key1='fname', key2='lname'))
# Datta
# (1, 2)
# {'key1': 'fname', 'key2': 'lname'}
# None
