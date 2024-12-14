import argparse
from random import randint

from fileslib.output import read_file


def main():
    # set up argument parsing
    parser = argparse.ArgumentParser(description='Read a CSV file and print its content')
    parser.add_argument('--file', type=str, required=True, help='Path to the CSV file ')
    args = parser.parse_args()

    # Call the read_file function with the file path
    read_file(args.file)


