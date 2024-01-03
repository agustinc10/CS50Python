import sys
import validators


def main():
    email = input("What's your email address? ")
    print(is_valid(email))


def is_valid(s):
    return "Valid" if validators.email(s) == True else "Invalid"


if __name__ == "__main__":
    main()
