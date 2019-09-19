class MyClass:
    """
    Use any variable name in place of self, that works perfectly.
    """

    def __init__(dt):
        dt.name = "Datta"

    def instance_method(dt):  # dt can be used in place of self, but need to maintain throught the class
        print(dt.name)

    @classmethod
    def class_method(dtcls):  # dtcls can be used in place of cls
        """
        Use of @classmethod decorator and cls is mandatory
        :return:
        """
        print('Here in class method')

    @staticmethod
    def static_method():
        """
        Use of @staticmethod decorator is optional
        :return:
        """
        print('Here in static method')


# calling instance method
datta = MyClass()
datta.instance_method()
# Datta

# calling class method
MyClass.class_method()

# calling static method
MyClass.static_method()
