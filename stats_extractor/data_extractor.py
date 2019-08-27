import os

import pandas as pd


class DataExtractor:

    def __init__(self):
        self.df = None

    def load_file(
        self, filename, col_separator=',', row_separator='\n',
        header_rows=1
    ):
        """
        Simple version of file loading with suffix checking

        :param filename: filename to load
        :param col_separator: optional separator for csv columns
        :param row_separator: optional separator for csv rows
        :param headers: optional number rows of headers
        """
        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            self.df = pd.read_excel(
                filename, header=[i for i in range(header_rows)]
            )
        elif filename.endswith('.csv'):
            try:
                self.df = pd.read_csv(
                    filename, header=[i for i in range(header_rows)],
                    sep=col_separator, delimiter=row_separator
                )
            # must be some bluescreeners created the file
            except UnicodeDecodeError:
                self.df = pd.read_csv(
                    filename, header=[i for i in range(header_rows)],
                    sep=col_separator, delimiter=row_separator,
                    encoding='cp1252'
                )
        else:
            raise Exception(
                "Unrecognized (yet) file extension: {}.".format(
                    filename.split('.')[-1]
                )
            )

    def __iter__(self):
        """
        Iterator for rows in DF.

        :return: row from DataFrame
        """
        for row in self.df.iterrows():
            yield row

    def get_headers(self):
        return self.df.columns

    def visualize_data(self):
        for row in self:
            print(row)