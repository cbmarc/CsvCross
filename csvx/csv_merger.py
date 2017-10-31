"""
Author Marc
Since 26/10/2017
"""
class CsvMerger(object):
    """This class merges the given csv files into one"""

    csv_files = None

    def __init__(self, csv_files):
        self.csv_files = csv_files
