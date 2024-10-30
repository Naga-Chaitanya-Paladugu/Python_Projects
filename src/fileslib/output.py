import csv


def read_file(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file) # DictReader reads each file as dictionary
        for row in reader:
            print(row) #Iterates over each row and prints each one individually
