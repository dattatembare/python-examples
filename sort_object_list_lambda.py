class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name}: {self.age}'


swara = Person('Swara', 10)
vibha = Person('Vibha', 3)
sonali = Person('Sonali', 30)
datta = Person('Datta', 31)

my_list = [swara, vibha, sonali, datta]
print(my_list)
# Sort by name
my_list.sort(key=lambda p: p.name)  # [Datta: 31, Sonali: 30, Swara: 10, Vibha: 3]
# Sort ny age
my_list.sort(key=lambda p: p.age)  # [Vibha: 3, Swara: 10, Sonali: 30, Datta: 31]

print(my_list)
