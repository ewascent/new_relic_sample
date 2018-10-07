"""module  for managing file interactions"""
from os import path
import io
import  platform
import mmap
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

def clean_up(raw_data=b'', chunk_size=0):
    """remove control characters and punctuation
    assume we are getting non string input and convert to utf8

    """
    utf8_data = raw_data.decode('utf8')
    punctuation_filter = re.compile('[%s]' % re.escape(punctuation)).sub
        #for chr in utf8_data:
    filter_control_chars = "".join(
        chr for chr in utf8_data
        if unicodedata.category(chr)[0] != "C")
    filter_punctuation_chars = punctuation_filter('', filter_control_chars)
    filter_case = filter_punctuation_chars.lower()
    filter_spacing = ' '.join(filter_case.split())
    return filter_spacing.lower()

def reader(file, mode="r+b", chunk_size=1000):
    """read files, spilt content into three word structs (or tuple threes)
    strips all unicode control characters and punctuation

    ARGUMENTS:
    String file: a path to a file
    String mode:a IO read mode
    Int chunk_size:A valid IO buffering value.  size 0 means whole file
    """
    word_list = []
    words = ""
    if isfile(file) == True:
        with io.open(file, mode, chunk_size) as f:
            for data in f:
                words = words + clean_up(data)
    else:
        raise ArgumentTypeException
##TODO make data a streaming list
    word_list = words.split(' ')
    chunker(word_list, chunk_size = 3)
##TODO: split into triples

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
