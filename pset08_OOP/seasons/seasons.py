from datetime import date
import inflect
import re
import sys


p = inflect.engine()

def main():
    print(calculate_time(input("Date of Birth: ")))


def calculate_time(s):
    if birth := re.search(r"^([1][9][0-9][0-9]|[2][0][0-1][0-9]|[2][0][2][0-3])-([0][1-9]|[1][0-2])-([0][1-9]|[1-2][0-9]|[3][0-1])$", s):
        b = date(int(birth.group(1)), int(birth.group(2)), int(birth.group(3)))
        time = date.today() - b
        minutes = time.total_seconds() / 60
        minutes = p.number_to_words(minutes).capitalize().replace("and ", "").replace("point zero", "minutes")

        return minutes
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
