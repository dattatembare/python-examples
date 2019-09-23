class MyClass:
    """
    Class method:
    One use people have found for class methods is to create inheritable alternative constructors.
    @classmethod function is callable without instantiating the class, but its definition follows Sub class,
    not Parent class, via inheritance. That’s because the first argument for @classmethod function must always be cls

    Static method:
    @staticmethod function is nothing more than a function defined inside a class. It is callable without instantiating
    the class first. It’s definition is immutable via inheritance.
    Neither self (the object instance) nor cls (the class) is implicitly passed as the first argument.
    They behave like regular python functions except that you can call them from an instance or the class.

    The difference between a static method and a class method is:
    Static method knows nothing about the class and just deals with the parameters(behave like regular function)
    Class method works with the class since its parameter is always the class itself.
    """

    def say():
        """
        it's a way of putting a function into a class (because it logically belongs there), while indicating that it
        does not require access to the class.
        """
        print("Hello")

    def instance_say(self):
        print('Hello')

    @staticmethod
    def static_say():
        print("Hello")

    @classmethod
    def class_say(cls):
        print('Hello')


mc = MyClass()

# mc.say()  # TypeError: say() takes 0 positional arguments but 1 was given
MyClass.say()  # Hello
mc.instance_say()  # Hello
mc.static_say()  # Hello
MyClass.static_say()  # Hello
MyClass.class_say()  # Hello

print(MyClass.say)  # <function MyClass.say at 0x0000023EF9AB8620>
print(mc.instance_say)  # <bound method MyClass.instance_say of <__main__.MyClass object at 0x0000023EF9ABC6A0>>
print(mc.class_say)  # <bound method MyClass.class_say of <class '__main__.MyClass'>>
print(mc.static_say)  # <function MyClass.static_say at 0x0000023EF9AB8730>
