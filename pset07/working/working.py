import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search(r"^([\d]|1[0-2])(:[0-5][0-9])?\s(AM|PM)(?:\s+to\s+)([\d]|1[0-2])(:(?:[0-5][0-9]))?\s(AM|PM)$", s):
        if time.group(3) == "AM":
            hours1 = "00" if time.group(1) == "12" else time.group(1).zfill(2)
        else:
            hours1 = "12" if time.group(1) == "12" else str(int(time.group(1)) + 12).zfill(2)

        if time.group(6) == "AM":
            hours2 = "00" if time.group(4) == "12" else time.group(4).zfill(2)
        else:
            hours2 = "12" if time.group(4) == "12" else str(int(time.group(4)) + 12).zfill(2)

        minutes1 = time.group(2) if time.group(2) is not None else ":00"
        minutes2 = time.group(5) if time.group(5) is not None else ":00"

        timef = hours1 + minutes1 + " to " + hours2 + minutes2
        return timef

    else:
         raise ValueError("Invalid time format")


if __name__ == "__main__":
    main()
