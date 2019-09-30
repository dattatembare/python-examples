"""
for-else or while-else could be used like switch statement in Java
"""
# use of for else
def for_else(my_list):
    for i in my_list:
        if i == 4:
            print("else skiped")
            return
    else:
        print("for and else executed")


for_else([1, 2, 3])
for_else([1, 2, 3, 4, 5])

print('---------------')


# use of while else
def while_else(my_list):
    i = 0
    while len(my_list) >= i:
        if i == 4:
            print("else skiped")
            return  # or break
        i += 1
    else:
        print("while and else executed")


while_else([1, 2, 3])
while_else([1, 2, 3, 4, 5])

print('---------------')


# Use of try except else finally
def try_else(a, b):
    try:
        print(a / b)
        print('try')
    except ZeroDivisionError as e:
        print(f'except {e}')
    else:
        print('else')
    finally:
        print('finally')


try_else(25, 5)
print('---------------')
try_else(25, 0)
