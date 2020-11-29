from math import sqrt


def isPrime(num: int) -> bool:
    # print('inside isPrime')
    if num < 2:
        return False
    # for i in range(2, num // 2):  # // -> floor division operator - return int
    for i in range(2, int(sqrt(num))):  # // square root is closest matching point
        if num % i == 0:
            return False
    return True


# if __name__ == '__main__':
#     for i in range(1, 101):
#         if isPrime(i):
#             print(i)

# num = 7
# t1 = threading.Thread(target=isPrime, args=(num,))
# t1.start()

# l = [l for l in range(1, 10)]
# print(l)

my_set = {7, 8, 1, 2, 2, 2, 3, 5}
print(my_set)
for i in my_set:
    print(i)
