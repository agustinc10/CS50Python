import sys
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a .csv file")
    else:
        try:
            file = open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File does not exist")

    menu = []
    with open(sys.argv[1]) as file:
        for row in file:
            pizza, small, large = row.rstrip().split(",")
            row = [pizza, small, large]
            menu.append(row)

    print(tabulate(menu, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
