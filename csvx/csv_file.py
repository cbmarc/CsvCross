"""
Author Marc
"""
import csv

class CsvFile(object):
    """This class loads a CSV file and holds its data"""
    rows = None

    def __init__(self, path):
        """Initializes the class with required stuff"""
        self.__open(path)

    def get_rows(self):
        """Gets rows for all columns"""
        return self.rows

    def __open(self, path):
        """Opens the csv file to work with"""
        with open(path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            lines = list(reader)
            self.rows = [{lines[0][idx]: val for (idx, val) in enumerate(row)} for row in lines[1:]]
