print(bool("False"))  # True

value = "A long string with a few words in it"

# Reverse character order # “ti ni sdrow….A”
print(value[::-1])
# Reverse word order # “it in words...A”
list_value = [word for word in value.split(' ')]
new_list = list_value[::-1]
print(new_list)

new_str = ' '.join(new_list)  # 1
new_str1 = ''
for word in new_list:
    new_str1 += word + ' '
print(new_str1.strip())  # 2
print(new_str)  # 1


def a(v=5):
    if v == 5:
        print("default")
        v = 6
    else:
        print("non def")
        v = 7
    return v


print(a())
print(a())

# Object types in python
# Numbers
# 1234, 3.1415, 999L, 3+4j, Decimal
# Strings
# 'spam', "guido's"
# Lists
# [1, [2, 'three'], 4]
# Dictionaries
# {'food': 'spam', 'taste': 'yum'}
# Tuples
# (1,'spam', 4, 'U')
# Files
# myfile = open('eggs', 'r')
# Other types
# Sets, types, None, Booleans
