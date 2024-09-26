def main():
    while True:
        try:
            fraction = input("Fraction: ")
            if not "/" in fraction:
                raise ValueError
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except ValueError:
            print("Value is incorrect")
        except ZeroDivisionError:
            print("You cannot divide by 0")


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if y == 0:  # Sprawdź najpierw dzielenie przez zero
        raise ZeroDivisionError
    if x > y:  # Dopiero potem sprawdzaj czy x > y
        raise ValueError
    z = (x / y) * 100
    z = int(round(z))
    if z > 100:
        raise ValueError
    return z


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
