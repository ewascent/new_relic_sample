"""main is main"""
import sys
from error import InsufficientArguments
from error import ArgumentTypeException
import filer
from utilities import setup_logging

__author__ = "ewascent"
__copyright__ = "ewascent"
__license__ = "mit"

def main(_args=None):
    """enter the dragon, is what I imagine the main method saying"""
    try:
        _logger = setup_logging('info')
        if _args is None:
            _args = sys.argv
        files = _args
        result_count = 100
        for file in files:
            _logger.info(f"Recieved path to file: {file}")
            results = filer.outputter(some_collection=filer.reader(file),
                                      this_many_results=result_count)
            print(f'Top {result_count} matches for file {file}')
            for result in results:
                print(result)

    except InsufficientArguments:
        _logger.error("Recieved no file input")
        raise
    except ArgumentTypeException:
        _logger.error("Not a valid file path")
        raise
    except:
        _logger.error("Unexpected error: %s", sys.exc_info()[0])
        print("Unexpected error:", sys.exc_info()[0])
        raise

if __name__ == "__main__":
    main(sys.argv)
