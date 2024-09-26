import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if ".csv" not in sys.argv[1]:
            sys.exit("Not a CSV file")
    argument = sys.argv[1]
    getting_list(argument)

def getting_list(argument):
    try:
        with open(argument, "r") as file:
            reader = csv.reader(file)
            table = tabulate(reader, headers='firstrow', tablefmt="grid", numalign="center")
            print(table)
    except FileNotFoundError:
        sys.exit("File does not exist")

main()
