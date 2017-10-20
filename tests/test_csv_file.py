# -*- coding: utf-8 -*-
import unittest
from csvx.csv_file import CsvFile

class CsvFileTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_empty_path(self):
        """ test squeleton """
        self.assertRaises(FileNotFoundError, CsvFile, '')


if __name__ == '__main__':
    unittest.main()
