def main():
    t = input("What time of day is it? ")
    if 7 <= convert(t) <= 8:
        print("breakfast time")
    elif 12 <= convert(t) <= 13:
        print("lunch time")
    elif 18 <= convert(t) <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return (float(hours) + float(minutes)/60)


if __name__ == "__main__":
    main()
