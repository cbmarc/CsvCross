"""
Author Marc
"""
import csv

class CsvFile(object):
    """This class loads and interacts with a particular CSV file"""
    rows = None
    header = None

    def __init__(self, path):
        """Initializes the class with required stuff"""
        self.__open(path)

    def get_rows_for_columns(self, columns):
        """Gets the rows with only the given columns"""
        column_indexes = self.__get_columns_index(columns)
        return self.__get_rows_for_columns(self.rows, column_indexes)

    def __get_rows_for_columns(self, rows, column_indexes):
        new_rows = list()
        for row in rows:
            new_rows.append([x for i, x in enumerate(row) if i in column_indexes])
        return new_rows

    def __get_columns_index(self, columns):
        return [i for i, x in enumerate(self.header) if x in columns]

    def __open(self, path):
        """Opens the csv file to work with"""
        with open(path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            self.rows = list(reader)
            self.header = self.rows[0]
            