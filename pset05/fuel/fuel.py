def main():
    while True:
        try:
            fraction = input("Fraction: ")
            fraction = convert(fraction)
            break
        except (ValueError, ZeroDivisionError, AttributeError):
            continue

    print(gauge(fraction))


def convert(fraction):
    fraction = fraction.split("/")
    f = int(fraction[0]) / int(fraction[1])
    if int(fraction[0]) > int(fraction[1]):
        raise ValueError
    f = (int(fraction[0]) / int(fraction[1])) *100
    return f


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return "{:.0%}".format(percentage/100)


if __name__ == "__main__":
    main()
