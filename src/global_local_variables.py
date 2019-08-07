global_var = "Hello"
global_var_2 = "Hello Datta"


def use_global():
    """
    Use of local and global variables
    :return: None
    """
    local_var = 'Hi'
    # print(global_var_2) UnboundLocalError: local variable 'global_var_2' referenced before assignment
    print(global_var_2)  # Hello Datta
    print(global_var)  # Hello
    print(local_var)  # Hi
    # If want to change global var value
    globals()['global_var'] = 'Hello World!!'
    print(locals())  # {'local_var': 'Hi'}


use_global()
print(f'Outside function- {global_var}')  # Outside function- Hello World!!
print(locals())  # {'__name__': '__main__', '__doc__': None, '__package__': None, '__
# loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000162AA451CF8>, '__spec__': None,
# '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'C:/Users/DattatrayaTembare/PycharmProjects/python-examples/src/global_local_variables.py',
# '__cached__': None, 'global_var': 'Hello World!!', 'global_var_2': 'Hello Datta',
# 'use_global': <function use_global at 0x00000162AA48E2F0>}
