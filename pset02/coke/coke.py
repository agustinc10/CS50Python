x = 50
while x > 0:
    print("Amount Due:", x)
    c = input("Insert coin: ")
    while c not in ("5", "10", "25"):
        print("Amount Due:", x)
        c = input("Insert coin: ")
    x -= int(c)

print("Change Owed:", abs(x))
