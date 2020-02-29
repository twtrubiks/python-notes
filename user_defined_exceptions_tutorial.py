# ref. https://docs.python.org/3/tutorial/errors.html

# a common practice is to create a base class for exceptions defined by that module,
# and subclass that to create specific exception classes for different error conditions

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

if __name__ == "__main__":
    try:
        raise InputError(expression= 'expression', message= 'This is InputError')
    except InputError as e:
        print('e.expression:', e.expression)
        print('e.message:', e.message)
