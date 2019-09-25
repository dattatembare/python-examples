# 1-100 or first 25 prime numbers

def is_prime_num(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


prime_nums = [num for num in range(101) if is_prime_num(num)]
print(prime_nums)
