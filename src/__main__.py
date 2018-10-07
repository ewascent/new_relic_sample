"""main is main"""
import sys
from error import InsufficientArguments
from filer import pather
from utilities import setup_logging

__author__ = "ewascent"
__copyright__ = "ewascent"
__license__ = "mit"

def main(_args = None):
    """enter the dragon, is what I imagine the main method saying"""
    try:
        _logger = setup_logging('info')
        if _args == None:
            _args = sys.argv
        files = pather(_args)
        for file in files:
            _logger.info("Recieved path to file: %s", file)
    except InsufficientArguments:
        _logger.warning("Recieved no file input")
        print("Please provide a valid file path.")
        _path = input("Enter a fully qualified path: ")
        _files = ["bogus first entry"]
        _files.append(_path)
        files = pather(_files)
    except:
        _logger.error("Unexpected error: %s", sys.exc_info()[0])
        print("Unexpected error:", sys.exc_info()[0])
        raise

if __name__ == "__main__":
    main(sys.argv)
