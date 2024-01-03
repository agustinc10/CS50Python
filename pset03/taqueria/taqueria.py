def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    t = 0
    while (True):
        try:
            item = input("Item: ").title()
            if item not in menu:
                raise Exception
            t += menu[item]
            print("Total:", "${:.2f}".format(t))
        except EOFError:
            print()
            return 0
        except Exception:
            pass

if __name__ == "__main__":
    main()
