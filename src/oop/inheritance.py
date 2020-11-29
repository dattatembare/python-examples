class Person:
    def __init__(self, name):
        self.name = name

    def identity(self):
        print(f'My name is {self.name}')


class SuperHero(Person):

    def __init__(self, name, hero_name):
        # super(SuperHero, self).__init__(name)
        super().__init__(name)
        self.hero_name = hero_name

    def identity(self):
        # super(SuperHero, self).identity()
        super().identity()
        print(f"...And I'm {self.hero_name}")


p = Person('Datta')
p.identity()
# My name is Datta

s = SuperHero('Dattatraya', 'Supper...')
print(isinstance(s, Person))  # Checking if instance of parent class
s.identity()
# True
# My name is Dattatraya
# ...And I'm Supper...

