import sys
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if ".py" not in sys.argv[1]:
            sys.exit("wrong command")
    argument = sys.argv[1]
    counter = count_lines(argument)
    print(counter)

def count_lines(argument):
    counter = 0
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        for line in lines:
            stripped_line = line.strip()

            if not stripped_line:
                continue

            if stripped_line.startswith("#"):
                continue

            counter += 1

    return counter

if __name__ == "__main__":
    main()
