class A:
    def __new__(cls, *args, **kwargs):
        print(object.__new__(cls, *args, **kwargs))

a = A()