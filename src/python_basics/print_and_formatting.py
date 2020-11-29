import os

print(f"{'*' * 10}Execute the command in a subshell{'*' * 10}")
for i in range(2, 6):
    input_string = "python --version " + str(i)
    os.system(input_string)
print(f"{'*' * 10}Execute the command in a subshell{'*' * 10}")

print(f"{'*' * 10}Use of format{'*' * 10}")
name = "Datta"
lname = "Tembare"
greeting = "Hello! {} {}"

greet = greeting.format(name, lname)
print(greet)  # Hello Datta Tembare

name = "Swara"
greet = greeting.format(name, lname)
print(greet)  # Hello Swara Tembare
print(f"{'*' * 10}Use of format{'*' * 10}")

# format
point = {'x': 4, 'y': -5}
print('{x} {y}'.format(**point))  # 4 -5

"""
The only difference is that, the str.format(**mapping) copies the dict whereas str.format_map(mapping) 
makes a new dictionary during method call. This can be useful if you are working with a dict subclass.
"""
point = {'x': 4, 'y': -5}
print('{x} {y}'.format_map(point))  # 4 -5

point = {'x': 4, 'y': -5, 'z': 0}
print('{x} {y} {z}'.format_map(point))  # 4 -5 0

# Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)  # ('I could eat ', 'bananas', ' all day')

# Fills the string with a specified number of 0 values at the beginning
txt = "50"
x = txt.zfill(10)
print(x)  # 0000000050

#################
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "this is string example....wow!!!"
print(str.translate(trantab))
#################

a = 10
# print(f'something {(result:=a+2)}') # python3.8
print(f'something {(a + 2)}')
print(f'something {a + 2}')
print('something {a}'.format(a=10 + 2))
print('something {}'.format(a+2))
