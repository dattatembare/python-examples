# EAFP - Eaiser to Forgiveness, No permission

my_list = [1, 2, 3, 4, 5]

# Non pythonic
# if len(my_list) >= 5:
#     print(my_list[5])
# else:
#     print('Index does not exist')

# Pythonic
try:
    print(my_list[5])
except:
    print('Index does not exist')

print('---------------------------------')

import os

my_file = "/path/to/my/file.txt"

# Race condition (non pythonic)
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print("File can't be accessed")

# # No race condition (pythonic)
try:
    f = open(my_file)
except IOError as e:
    print("File can't be accessed")
else:
    with f:
        print(f.read())
