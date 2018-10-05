"""Define our custom exceptions"""
class Error(Exception):
    """Our sase class for our exceptions"""
    pass

class InsufficientArguments(Error):
    """Raise when expected number of arguments or values is insuffiencctly met"""
    pass

class ArgumentTypeException(Error):
    """Raised when arguments or values are not of the expected type"""
    pass
