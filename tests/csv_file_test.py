# -*- coding: utf-8 -*-
""" Test for CsvFile class in csvx module """
import unittest
from context import CsvFile

class CsvFileTestSuite(unittest.TestCase):
    """ CsvFile test cases. """

    def test_fail_open_empty_path(self):
        """ should fail when initialized with an empty string """
        with self.assertRaises(IOError):
            CsvFile('')

    def test_get_rows_for_columns(self):
        """ should get all rows only with the given columns and its values """
        path = 'tests/test_csv_a.csv'
        csv_file = CsvFile(path)
        rows = csv_file.get_rows_for_columns(['column2', 'price'])
        self.assertGreater(len(rows), 0)

if __name__ == '__main__':
    unittest.main()
