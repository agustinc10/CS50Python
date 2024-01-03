import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    txt = re.findall(r"\b[uU][mM]\b", s)
    c = len(txt)
    return c


if __name__ == "__main__":
    main()
