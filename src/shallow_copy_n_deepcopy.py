import copy

print(f"{'*' * 10}Shallow copy{'*' * 10}")
my_list = [{'fname': 'Datta', 'lname': 'Tembare'}, [1, 2, 3]]
new_list = my_list.copy()  # --> same as copy.copy(my_list)

print(my_list)
print(new_list)
new_list[0]['fname'] = 'Dattatraya'
new_list[1] = 'List replaced with string'
new_list.append('Added new string')
print(my_list)
print(new_list)
print(f"{'*' * 10}Shallow copy{'*' * 10}")

print(f"{'*' * 10}Deep copy{'*' * 10}")
my_list = [{'fname': 'Datta', 'lname': 'Tembare'}, [1, 2, 3]]
new_list = copy.deepcopy(my_list)

print(my_list)
print(new_list)
new_list[0]['fname'] = 'Dattatraya'
print(my_list)
print(new_list)
print(f"{'*' * 10}Deep copy{'*' * 10}")
