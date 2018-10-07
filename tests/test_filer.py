"""Unit tests for the filer module"""
from os import path
import unittest2 as unittest
from error import InsufficientArguments
from filer import pather
from filer import clean_up
from filer import chunker
from filer import reader

class ValidatePather(unittest.TestCase):

    def test_accepts_args(self):
        """Pather raises with no args"""
        testargs = ["args assumes first element is python file path"]
        expected = 'no love'
        try:
            pather(testargs)
        except InsufficientArguments:
            expected = 'exception returned'
        self.assertEqual('exception returned', expected)

    def test_returns_valid_path(self):
        """Pather returns a valid path from argv"""
        dir_path = path.dirname(path.realpath(__file__))
        bad_path = '/usr/bin/funkypath'
        testargs = [bad_path, dir_path]
        expected = [dir_path]
        actual = pather(testargs)
        self.assertEqual(expected, actual)

    def test_clean_data_punctuation(self):
        """we strip punctuation from input"""
        raw_data = "A swift!!! raven never flies?"
        expected = "A swift raven never flies"
        actual = clean_up(raw_data)
        self.assertEqual(expected, actual)

    def test_clean_data_simple(self):
        """we strip punctuation from input"""
        raw_data = "A swift raven never flies"
        expected = "A swift raven never flies"
        actual = clean_up(raw_data)
        self.assertEqual(expected, actual)

    def test_clean_data_control_characters(self):
        """we strip control characters from input"""
        raw_data = "A \nswift raven \rnever flies"
        expected = "A swift raven never flies"
        actual = clean_up(raw_data)
        self.assertEqual(expected, actual)

    def test_chunker_splits_sentance(self):
        """given a sentance ensure you get the expected number of triples"""
        data = ['one','two', 'three', 'four', 'five']
        sut = chunker(data=data, chunk_size=3)
        expected = [('one', 'two', 'three'),('two', 'three', 'four'),('three', 'four', 'five')]
        x = 0
        for actual in sut:
            self.assertEqual(expected[x], actual)
            x += 1

    def test_reader(self):
        """does this read and provide a list of words"""
        data = './data/simple_data.txt'
        actual = reader(data)
        expected = ["one", "two", "three", "four", "five"]
        self.assertEqual(expected, actual)
