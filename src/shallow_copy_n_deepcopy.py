import copy

my_list = [{'fname': 'Datta', 'lname': 'Tembare'}, [1, 2, 3]]
# new_list = my_list.copy() # --> same as copy.copy(my_list)
new_list = copy.deepcopy(my_list)

print(my_list)
print(new_list)
new_list[0]['fname'] = 'Dattatraya'
print(my_list)
print(new_list)
