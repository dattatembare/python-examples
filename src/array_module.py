"""
When to use arrays?
Lists are much more flexible than arrays. They can store elements of different data types including string. Also,
lists are faster than arrays. And, if you need to do mathematical computation on arrays and matrices,
you are much better off using something like NumPy library.
Unless you don't really need arrays (array module may be needed to interface with C code), don't use them.
"""

import array as arr

# a = arr.array('d', [1, 3.5, "Hello"])  # TypeError: must be real number, not str

a = arr.array('d', [1.1, 3.5, 4.5])  # d- double
print(a)  # array('d', [1.1, 3.5, 4.5])
print(a[0])  # 1.1
print(a[-1])
b = arr.array('f', [1.1, 3.5, 4.5])  # f- float
print(b)  # array('f', [1.100000023841858, 3.5, 4.5])
