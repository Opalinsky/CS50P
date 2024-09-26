names = []

with open("name.txt") as file:
    for line in sorted(file):
        print("hello, ", line.rstrip())

for name in sorted(names, reverse = True):
    print(f"hello, {name}")
