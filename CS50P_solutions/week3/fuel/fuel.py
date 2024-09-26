
def main():
    while True:
        try:
            fraction = input("Fraction: ")
            if not "/" in fraction:
                raise ValueError
            for i in range(len(fraction)):
                if fraction[i] == "/":
                    z = i
                    k = z + 1
                    break
            x = int(fraction[0:z])
            y = int(fraction[k:])
            z = (x/y)*100
            z = int(round(z))
            if z > 100:
                raise ValueError
            elif z >= 99:
                z = "F"
                print(z)
                return z
            elif z <= 1:
                z = "E"
                print(z)
                return z
            else:
                print(z,"%", sep="")
            break
        except ValueError:
            print("Value is incorrect")
        except ZeroDivisionError:
            print("You cannot divide by 0")

main()
