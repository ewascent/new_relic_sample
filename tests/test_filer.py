"""Unit tests for the filer module"""
import unittest2 as unittest
import sys
from error import InsufficientArguments
from unittest.mock import patch
from unittest.mock import MagicMock
from os import path
from filer import pather

class ValidatePather(unittest.TestCase):

    def test_accepts_args(self):
        """Pather raises with no args"""
        testargs = ["args assumes first element is python file path"]
        expected = 'no love'
        try:
            pather(testargs)
        except InsufficientArguments:
           expected = 'exception returned'
        result = self.assertEqual('exception returned', expected)

    def test_returns_valid_path(self):
        """Pather returns a valid path from argv"""
        dir_path = path.dirname(path.realpath(__file__))
        bad_path = '/usr/bin/funkypath'
        testargs = [bad_path, dir_path]
        sut = pather(testargs)
        expected = [dir_path]
        actual = sut
        result = self.assertEqual(expected, actual)
#try:
#    f = pather(argv)
#    print(f)
#except InsufficientArguments:
#    print("nope")
