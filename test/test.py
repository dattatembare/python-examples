# string find duplicate chars
# 1. Using list count method
print(list('Datta').count('a'))  # 2
print(list('Datta').count('t'))  # 2
print(list('Datta').count('D'))  # 1
print(list('Datta').count('z'))  # 0
print(list('Datta').count(''))  # 0


# 1. Writing my own algorithm
def find_duplicate(instr: str):
    # create dictionary
    data_dict = {}
    for char in instr:
        count = data_dict.get(char, 0) + 1
        data_dict[char] = count
        if count > 1:
            return True

    return False


print(find_duplicate(""))
print(find_duplicate("ABC"))
print(find_duplicate("DATTA"))

print("Datta Tembare".split())
print("DattaTembare".split())
