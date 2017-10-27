"""
Author Marc
"""
import csv

class CsvFile(object):
    """This class loads a CSV file and holds its data"""
    rows = None
    header = None

    def __init__(self, path):
        """Initializes the class with required stuff"""
        self.__open(path)

    def get_rows(self):
        """Gets rows for all columns"""
        column_indexes = self.__get_columns_index(self.header)
        return self.__get_rows_for_columns(self.rows, column_indexes)

    def get_rows_for_columns(self, columns):
        """Gets the rows with only the given columns"""
        column_indexes = self.__get_columns_index(columns)
        return self.__get_rows_for_columns(self.rows, column_indexes)

    def __get_rows_for_columns(self, rows, column_indexes):
        return [[x for i, x in enumerate(r) if i in column_indexes] for r in rows]

    def __get_columns_index(self, columns):
        return [i for i, x in enumerate(self.header) if x in columns]

    def __open(self, path):
        """Opens the csv file to work with"""
        with open(path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            self.rows = {rows[0]:rows[1] for rows in reader}
