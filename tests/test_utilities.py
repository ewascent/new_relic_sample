#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest2 as unittest
import sys
from utilities import logleveler

class ValidateLogLeveler(unittest.TestCase):
    def test_maps_critical(self):
        """Logleveler maps critical"""
        actual = logleveler('critical')
        expected = 50
        self.assertEqual(expected, actual)
    def test_maps_info(self):
        """Logleveler maps info"""
        actual = logleveler('info')
        expected = 20
        self.assertEqual(expected, actual)
    def test_maps_debug(self):
        """Logleveler maps debug"""
        actual = logleveler('debug')
        expected = 10
        self.assertEqual(expected, actual)
    def test_maps_warn(self):
        """Logleveler maps warn"""
        actual = logleveler('warn')
        expected = 30
        self.assertEqual(expected, actual)
    def test_maps_warning(self):
        """Logleveler maps warning"""
        actual = logleveler('warning')
        expected = 30
        self.assertEqual(expected, actual)
    def test_maps_error(self):
        """Logleveler maps error"""
        actual = logleveler('error')
        expected = 40
        self.assertEqual(expected, actual)
    def test_maps_notset(self):
        """Logleveler maps notset"""
        actual = logleveler('notset')
        expected = 0
        self.assertEqual(expected, actual)
