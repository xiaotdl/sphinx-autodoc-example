class Base(object):
    """
    Base class for all classes.
    """
    pass


class Klass(Base):
    """
    Example class that inherited from Base class.
    """

    def f(self, arg1, arg2):
        """
        Example function that does blabla.

        Args:
            arg1(int): (required) arg1 is used for ...
            arg2(int): (required) arg2 is used for ...
        Returns:
            bool: true on success, false on failure
        returns: Success: True, failure: Raise Error
        """
        return True
