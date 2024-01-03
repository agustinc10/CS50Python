import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file")
    else:
        try:
            file = open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File does not exist")

    loc = 0
    with open(sys.argv[1]) as file:
        for i in file:
            if i.lstrip().startswith("#") == False and i.isspace() == False:
                loc += 1
    print(loc)


if __name__ == "__main__":
    main()
