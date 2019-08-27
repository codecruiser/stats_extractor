import os

from unittest import TestCase

from pandas import MultiIndex

from stats_extractor.data_extractor import DataExtractor


class TestDataImport(TestCase):

    def setUp(self):
        self.de = DataExtractor()
        self.fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')

    def test_excel_data_load(self):
        """
        Loads test excel file with data and checks if data were loaded
        """
        self.de.load_file(
            os.path.join(self.fixture_path, 'archiwum_tab_a_2019.xls'),
            header_rows=2
        )
        self.assertIsInstance(self.de.get_headers(), MultiIndex)
        self.assertEqual(len(self.de.get_headers().levels), 2)

    def test_csv_data_load(self):
        """
        Loads test CSV file with data and checks if data were loaded
        """
        self.de.load_file(
            os.path.join(self.fixture_path, 'archiwum_tab_a_2019.csv'),
            header_rows=2, col_separator=';'
        )
        self.assertIsInstance(self.de.get_headers(), MultiIndex)
        self.assertEqual(len(self.de.get_headers().levels), 2)

    def test_unrecognized_data_load(self):
        """
        Loads test unrecognized file with data and checks if data were loaded
        """
        with self.assertRaises(Exception):
            self.de.load_file(
                os.path.join(self.fixture_path, 'archiwum_tab_a_2019.kjh')
            )
