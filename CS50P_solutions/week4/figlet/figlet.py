from pyfiglet import Figlet
import random
import sys
figlet = Figlet()
if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
else:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("wrong command")
    print(sys.argv[1])
    x = sys.argv[1]
    print(x)
    if x != "-f":
        sys.exit
    f = sys.argv[2]
    print(f)
    if not f in figlet.getFonts():
        sys.exit("Not found")
    figlet.setFont(font=f)
str = input("Input: ")
print(figlet.renderText(str))
