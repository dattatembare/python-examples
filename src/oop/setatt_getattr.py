class Person:
    name = 'Adam'


p = Person()

print('Name is:', p.name)
# setting attribute name to Datta, this will override the old value.
setattr(p, 'name', 'Datta')
print('Name is:', p.name)
# Name is: Adam
# Name is: Datta

# setting an attribute not present
# in Person
setattr(p, 'age', 23)
print('Age is:', p.age)
print(getattr(p, 'name'))
# Age is: 23
# Datta
