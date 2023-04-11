# doctest_myClass.py

class MyClass:
    pass


def unpredictable(obj):
    """Returns a new list containing obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<myClass.MyClass object at 0x...>]
    """

    return [obj]
