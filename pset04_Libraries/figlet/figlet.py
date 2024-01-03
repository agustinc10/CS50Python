import random
import sys
from pyfiglet import Figlet

figlet = Figlet()
list = figlet.getFonts()

if len(sys.argv) not in (1, 3):
    sys.exit("Has to be either 0 or 2 commmand-line arguments")
if len(sys.argv) == 3 and (
    sys.argv[1] not in ("-f", "--font") or sys.argv[2] not in list
):
    sys.exit("Invalid usage")


if len(sys.argv) == 1:
    myfont = random.choice(list)
else:
    myfont = sys.argv[2]

figlet.setFont(font=myfont)

s = input("Input: ")
print(f"Output: \n{figlet.renderText(s)}")
