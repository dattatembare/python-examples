class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
         __call__ method in a class is triggered when the instance of a class is called
        :param args:
        :param kwargs:
        :return:
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        # If you want to run __init__ every time the class is called, add
        # else:
        #     cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]


class Logger(object):
    __metaclass__ = Singleton


# Or in Python3

class Logger(metaclass=Singleton):
    pass
