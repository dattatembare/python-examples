# from functools import wraps


def singleton(class_):
    instances = {}

    # @wraps(class_)    # Need to check whether wraps is useful here
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class MyClass:
    pass
