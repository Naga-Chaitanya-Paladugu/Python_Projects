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


if __name__ == '__main__':
    for n in range(-1, 102):
        result = None
        if n< 1 or n> 100:
            continue
        if n % 2 == 1:
            result = 'Weird'
        elif n % 2 == 0:
            if n in [2, 3, 4, 5]:
                result = 'Not Weird'
            elif 6 <= n <= 20:
                result = 'Weird'
            else:
                result = 'Not Weird'


        print(f"{result}")
