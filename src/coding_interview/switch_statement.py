my_info = {"fname": "Datta",
           "lname": "Tembare",
           "address": "my address"}


def switch_dictionary(my_str):
    return my_info.get(my_str, "Invalid request")


print(switch_dictionary('fname'))  # Datta
print(switch_dictionary('pin'))  # Invalid request


def switch_while(my_str):
    i = 0
    while i == 0:
        if 'fname' == my_str:
            print(my_info.get(my_str))
            break
        elif 'lname' == my_str:
            print(my_info.get(my_str))
        i += 1
    else:
        print('Hope you are doing great!')


switch_while('fname')  # Datta
switch_while('lname')
# Tembare
# Hope you are doing great!

# something can be done using for-else loop too
