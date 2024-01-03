while True:
    try:
        f = (input("Fraction: ").split("/"))
        int(f[0]), int(f[1])
        if int(f[0]) > int(f[1]):
            raise Exception
        f = int(f[0]) / int(f[1])
    except (ValueError, ZeroDivisionError, Exception):
        pass
    else:
        break

if f >= 0.99:
    print("F")
elif f <= 0.1:
    print("E")
else:
    print("{:.0%}".format(f))

