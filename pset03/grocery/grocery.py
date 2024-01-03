grocery = {}
while(True):
    try:
        item = input().strip().upper()
        if item not in grocery:
            grocery[item] = 1
        else:
            grocery[item] += 1
    except EOFError:
        break

for item in sorted(grocery):
    print(grocery[item], item)

