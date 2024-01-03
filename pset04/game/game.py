from random import randint

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            raise ValueError
    except ValueError:
        pass
    else:
        break

m = 1
r = randint(m, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1 or guess > level:
            raise ValueError
    except ValueError:
        continue
    if guess < r:
        print("Too small!")
        m = guess
    elif guess > r:
        print("Too large!")
        level = guess
    else:
        print("Just right!")
        break
