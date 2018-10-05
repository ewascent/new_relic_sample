"""main is main"""
import sys
import error

def __main__():
    """enter the dragon, is what I imagine the main method saying"""
    if len(sys.argv) == 1:
        raise error.InsufficientArguments
    while True:
        try:
            ## TODO: add logical entry point
            break
        except InsufficientArguments:
            print("Please provide a valid file path.")
            _path = input("Enter a fully qualified path: ")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
