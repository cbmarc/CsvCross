# -*- coding: utf-8 -*-
""" Test for CsvFile class in csvx module """
import unittest
from csvx.csv_file import CsvFile

class CsvFileTestSuite(unittest.TestCase):
    """ CsvFile test cases. """

    def test_fail_open_empty_path(self):
        """ test constructor with empty path """
        with self.assertRaises(IOError):
            CsvFile('')

    def test_get_rows_for_columns(self):
        """ test constructor with good path """
        path = 'tests/test_csv_a.csv'
        csv_file = CsvFile(path)
        rows = csv_file.get_rows_for_columns(['column2', 'price'])
        self.assertGreater(len(rows), 0)

if __name__ == '__main__':
    unittest.main()
