from datetime import datetime

while True:
    date = input("Date: ").strip()
    try:
        date = datetime.strptime(date, "%m/%d/%Y")
        break
    except ValueError:
        pass
    try:
        date = datetime.strptime(date, "%B %d, %Y")
        break
    except ValueError:
        pass
print(date.strftime("%Y-%m-%d"))
