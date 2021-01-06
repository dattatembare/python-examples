def fib_cal(for_range):
    fib_nums = []
    for num in range(for_range):
        if num == 0:
            fib_nums.append(0)
        elif num == 1 or num == 2:
            fib_nums.append(1)
        else:
            fib_nums.append(fib_nums[num - 2] + fib_nums[num - 1])
    return fib_nums


print(fib_cal(10))
print('-----------')


# Sol 2
def fib_cal2(for_range):
    a, b = 0, 1
    for i in range(for_range):
        print(a, end=',')
        a, b = b, a + b


fib_cal2(10)
print('\n-----------')


def fib_cal_generator(for_range):
    a, b = 0, 1
    for i in range(for_range):
        yield f'{i + 1}:{a}'
        a, b = b, a + b


for i in fib_cal_generator(10):
    print(i, end='')
