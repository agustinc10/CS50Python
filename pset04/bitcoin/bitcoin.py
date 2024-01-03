import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
else:
    try:
        n = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = r.json()
except (requests.RequestException, json.JSONDecodeError):
    sys.exit("RequestExcemprion occurred")

amount = data["bpi"]["USD"]["rate_float"] * n
print(f"${amount:,.4f}")

