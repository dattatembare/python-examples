# duck typing is a style of dynamic typing in which an object's current set of methods and properties determines
# the valid semantics, rather than its inheritance from a particular class or implementation of a specific interface.

class Duck:
    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, flap')


class Person:
    def quack(self):
        print("I'm quacking like duck")

    def fly(self):
        print("I'm flying like duck")

    # def bark(self):
    #     print('Bark..')


def quack_and_fly(thing):
    # Pythonic implementation - EAFP Easier to forgiveness, No permission
    try:
        thing.quack()
        thing.fly()
        # thing.bark()
    except AttributeError as e:
        print(e)  # 'Duck' object has no attribute 'bark'


d = Duck()
quack_and_fly(d)
print('---------')
p = Person()
quack_and_fly(p)
