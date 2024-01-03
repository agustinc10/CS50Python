import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r".*src=\"https?://(?:www\.)?youtube\.com/embed/(\w+).*", s):
        link = re.sub(r".*src=\"https?://(www\.)?youtube\.com/embed/(\w+).*", r"https://youtu.be/" + matches.group(1), s)
        return link


if __name__ == "__main__":
    main()
