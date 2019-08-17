def is_prime_num(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(3, num):
            print(i)
            if num % i == 0:
                return False
        return True


prime_nums = [num for num in range(101) if is_prime_num(num) is True]
print(prime_nums)
