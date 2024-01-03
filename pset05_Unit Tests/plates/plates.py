import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 1 < len(s) < 7 and twoletters(s) and s.isalnum() and not_zero(s) and ending(s):
        return True
    else:
        return False


def twoletters(s):
    return True if s[0].isalpha() and s[1].isalpha() else False


def not_zero(s):
    x = re.findall(r"\d", s)
    if not x:
        return True
    elif x[0] != "0":
        return True
    else:
        return False


def ending(s):
    x = re.split(r"\d+", s)
    return True if len(x) == 1 or x[1].isalpha() == False else False


if __name__ == "__main__":
    main()
