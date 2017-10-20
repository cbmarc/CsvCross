# -*- coding: utf-8 -*-
""" Test for CsvFile class in csvx module """
import unittest
from csvx.csv_file import CsvFile

class CsvFileTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_empty_path(self):
        """ test squeleton """
        with self.assertRaises(IOError):
            CsvFile('')


if __name__ == '__main__':
    unittest.main()
