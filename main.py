from argparse import ArgumentParser

from stats_extractor.data_extractor import DataExtractor

if __file__ == '__main__':
    parser = ArgumentParser(description='Statistics extractor.')
    parser.add_argument(
        'filename', type=str, help='File(s) with statistics.'
    )
    args = parser.parse_args()

    data_extractor = DataExtractor()
    # extracts data from file
    data_extractor.load_file(args.filename)
    data_extractor.visualize_data()
