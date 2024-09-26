def main():
    x = get_int("What is x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x #break out of the loop and return the value
        except ValueError:
            pass

main()

