def func_1():
    print(x)  # 10


x = 10
func_1()
print(x)  # 10

print('--------------')


def func_2():
    # print(y) # UnboundLocalError: local variable 'y' referenced before assignment
    y = 20
    print(y)  # 20


y = 10
func_2()
print(y)  # 10

print('--------------')


def func_3():
    global z
    print(z)  # 10
    z = 20
    print(z)  # 20


z = 10
func_3()
print(z)  # 20

print('--------------')


def func_4():
    a = 10
    print('1..', a)  # 10

    def inner_fucn():
        nonlocal a
        print('2..', a)  # 10
        a = 100
        print('3..', a)  # 100

    print('4..', a)  # 10
    inner_fucn()
    print('5..', a)  # 100


a = 20
func_4()
print('6..', a)  # 20

print('--------------')


def func_4():
    b = 10
    print('1..', b)  # 10

    def inner_fucn():
        global b
        print('2..', b)  # 20
        b = 100
        print('3..', b)  # 100

    print('4..', b)  # 10
    inner_fucn()
    print('5..', b)  # 10


b = 20
func_4()
print('6..', b)  # 100
