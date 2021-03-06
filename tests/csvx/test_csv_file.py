# -*- coding: utf-8 -*-
""" Test for CsvFile class in csvx module """
import unittest
from csvx.csv_file import CsvFile

class CsvFileTestSuite(unittest.TestCase):
    """ CsvFile test cases. """

    csv_file = None

    def setUp(self):
        path = 'tests/resources/test_csv_a.csv'
        self.csv_file = CsvFile(path)

    def test_fail_open_empty_path(self):
        """ should fail when initialized with an empty string """
        with self.assertRaises(IOError):
            CsvFile('')

    def test_get_rows(self):
        """should get all rows only with the given columns and its values"""
        rows = self.csv_file.get_rows()
        self.assertGreater(len(rows), 0)
        self.assertEqual(len(rows[0]), 4)

if __name__ == '__main__':
    unittest.main()
