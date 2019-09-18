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
