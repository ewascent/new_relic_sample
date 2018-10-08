"""Unit tests for the filer module"""
from os import path
from os.path import abspath
from os import curdir
import unittest2 as unittest
from error import InsufficientArguments
import filer

class ValidateFiler(unittest.TestCase):
    """Validate the filer module"""
    def test_accepts_args(self):
        """Pather raises with no args"""
        testargs = ["args assumes first element is python file path"]
        expected = 'no love'
        try:
            filer.pather(testargs)
        except InsufficientArguments:
            expected = 'exception returned'
        self.assertEqual('exception returned', expected)

    def test_returns_valid_path(self):
        """Pather returns a valid path from argv"""
        dir_path = path.dirname(path.realpath(__file__))
        bad_path = '/usr/bin/funkypath'
        testargs = [bad_path, dir_path]
        expected = [dir_path]
        actual = filer.pather(testargs)
        self.assertEqual(expected, actual)

    def test_clean_data_punctuation(self):
        """we strip punctuation from input"""
        raw_data = b"A swift!!! raven never flies?"
        expected = "a swift raven never flies"
        actual = filer.clean_up(raw_data)
        self.assertEqual(expected, actual)

    def test_clean_data_simple(self):
        """we strip punctuation from input"""
        raw_data = b"A swift raven never flies"
        expected = "a swift raven never flies"
        actual = filer.clean_up(raw_data)
        self.assertEqual(expected, actual)

    def test_clean_up_control_chars(self):
        """we strip control characters from input"""
        raw_data = b"A \nswift raven \rnever flies"
        expected = "a swift raven never flies"
        actual = filer.clean_up(raw_data)
        self.assertEqual(expected, actual)

    def test_chunker_splits_sentance(self):
        """given a sentance ensure you get the expected number of triples"""
        data = ['one', 'two', 'three', 'four', 'five']
        sut = filer.chunker(data=data, chunk_size=3)
        expected = [('one', 'two', 'three'), ('two', 'three', 'four'), ('three', 'four', 'five')]
        cnt = 0
        for actual in sut:
            self.assertEqual(expected[cnt], actual)
            cnt += 1

    def test_reader(self):
        """does this read and provide a list of words"""
        file = path.join(abspath(curdir), 'data\\simple_data.txt')
        sut = filer.reader(file=file, mode="r+b")
        for triple in sut:
            actual = triple
        expected = ("three", "four", "five")
        self.assertEqual(expected, actual)

    def test_match_maker(self):
        """Test we are making the matches like a pro"""
        tuple1 = ("the", "lonely", "minotaur")
        tuple2 = ("regrets", "some", "choices")
        tuple3 = ("like", "that", "unicorn")
        data = [tuple1, tuple3, tuple3, tuple2, tuple3, tuple2]
        expected = [(tuple3, 3), (tuple2, 2)]
        actual = filer.match_maker(data, 2)
        self.assertEqual(expected, actual)

    def test_outputter(self):
        """test the outputter with a simple file"""
        file = path.join(abspath(curdir), 'data\\a_little_more_data.txt')
        some_collection = filer.reader(file=file, mode="r+b")
        counter = 0
        results = filer.outputter(some_collection, 2)
        expected = ["Result 2 was \"like that unicorn\".", "Result 1 was \"that unicorn the\"."]
        for actual in results:
            self.assertEqual(expected[counter], actual)
            counter += 1
