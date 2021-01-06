# Square of number
print(3 ** 2)

# Generator expressions
g = (x ** 2 for x in range(10))
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 4
print(next(g))  # 9
print(next(g))  # 16
print(sum(x ** 3 for x in range(10)))  # 2025
print(sum(x ** 3 for x in range(10) if x % 3 == 1))  # 408


# Generator use case
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result


csv_gen = csv_reader("some_csv.txt")  # some_csv with huge number of lines
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")


# Traceback (most recent call last):
#   File "ex1_naive.py", line 22, in <module>
#     main()
#   File "ex1_naive.py", line 13, in main
#     csv_gen = csv_reader("file.txt")
#   File "ex1_naive.py", line 6, in csv_reader
#     result = file.read().split("\n")
# MemoryError

# Use this csv_reader instead
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

# Row count is 64186394
