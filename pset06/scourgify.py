import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") == False or sys.argv[2].endswith(".csv") == False:
        sys.exit("Not a .csv file")
    else:
        try:
            file = open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("Could not read ", sys.argv[1])

    students = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].replace('"', "").split(", ")
            students.append({"first": first, "last": last, "house": row["house"]})

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in range(len(students)):
            writer.writerow(
                {
                    "first": students[student]["first"],
                    "last": students[student]["last"],
                    "house": students[student]["house"],
                }
            )


if __name__ == "__main__":
    main()
