import random


def main():
    level = get_level()
    points = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        i = 0
        while i < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                i += 1
                pass
            else:
                if answer == z:
                    points += 1
                    break
                elif i < 2:
                    print("EEE")
                    i += 1
                else:
                    print("EEE")
                    print(f"{x} + {y} = {z}")
                    i += 1

    print(f"Score: {points}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in range(1, 4):
                raise ValueError
        except ValueError:
            pass
        else:
            return level


def generate_integer(level):
    while True:
        try:
            if level not in range(1, 4):
                raise ValueError
        except ValueError:
            pass
        else:
            if level == 1:
                return random.randint(0, 9)
            elif level == 2:
                return random.randint(10, 99)
            elif level == 3:
                return random.randint(100, 999)


if __name__ == "__main__":
    main()
