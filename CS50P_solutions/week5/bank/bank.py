def main():
    answear = input("Greeting: ")
    answear = answear.lower().strip()
    value(answear)

def value(greeting):
    points = 0
    if greeting[0] == 'h':
        if greeting[0:5] == 'hello':
            return f"${points}"
            #print("$0")
        else:
            points = 20
            return f"${points}"
            #print("$20")
    else:
        points = 100
        return f"${points}"
        #print("$100")


if __name__ == "__main__":
    main()
