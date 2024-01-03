import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    p = r"([1]?[\d]?[\d]?|[2][0-4][\d]|25[0-5])"
    if re.search("^" + p + r"\." + p + r"\." + p + r"\." + p + "$" , ip, re.IGNORECASE):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
