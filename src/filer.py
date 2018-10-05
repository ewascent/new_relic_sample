"""module  for managing file interactions"""
from os import path
from sys import argv
from error import InsufficientArguments

def pather(arguments= []):
    _paths = []
    if len(arguments) <= 1:
        raise InsufficientArguments
    elif len(arguments) >= 2:
        for arg in range(1, len(arguments)):
            _file = arguments[arg]
            if path.exists( _file):
                _paths.append(_file)

    return _paths
