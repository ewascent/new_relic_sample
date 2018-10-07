"""module  for managing file interactions"""
from os import path
from os.path import isfile
from itertools import islice
import unicodedata
import re
from string import punctuation
from error import InsufficientArguments
from error import ArgumentTypeException

def pather(arguments= []):
    """test paths for validity

    ARGUMENTS:
    List<String> arguments: list pf valid file paths
    """
    _paths = []
    if len(arguments) <= 1:
        raise InsufficientArguments
    elif len(arguments) >= 2:
        for arg in range(1, len(arguments)):
            _file = arguments[arg]
            if path.exists( _file):
                _paths.append(_file)

    return _paths

def clean_up(raw_data):
    """remove control characters and punctuation"""
    punctuation_filter = re.compile('[%s]' % re.escape(punctuation)).sub
    data_sans_control_chars = "".join(
        chr for chr in raw_data
        if unicodedata.category(chr)[0] != "C")
    clean_data = punctuation_filter('', data_sans_control_chars)
    return clean_data

def reader(file):
    """read files, spilt content into three word structs (or tuple threes)
    strips all unicode control characters and punctuation

    ARGUMENTS:
    String file: a path to a file
    """
    word_list = []
    if isfile(file) == False:
        raise ArgumentTypeException
    with open(file) as _file:
        clean_data = clean_up(_file)
        for line in clean_data:
            for word in line.split():
                word_list.append(word)
##TODO make data a streaming list
##TODO: split into triples
#
    return word_list


#TODO
def chunker(data, chunk_size = 3):
    """method that takes a file and breaks it into a sliding window (of width n) over data from the iterable
    give a list of [1,2,3,4,5], it will return [(1,2,3), (2,3,4), (3,4,5)]

    USAGE:
    ivals = chunker([1,2,3,4,5])
    next(ivals)

    ARGUMENTS:
    data: a data source
    size: width of the window
    """
    it = iter(data)
    result = tuple(islice(it, chunk_size))
    if len(result) == chunk_size:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

# TODO: implement matching algorythm
# REF https://docs.python.org/2/library/collections.html#collections.Counter
