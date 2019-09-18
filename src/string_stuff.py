name = "Datta"
lname = "Tembare"
greeting = "Hello! {} {}"

greet = greeting.format(name, lname)
print(greet)  # Hello Datta Tembare

name = "Swara"
greet = greeting.format(name, lname)
print(greet)  # Hello Swara Tembare
