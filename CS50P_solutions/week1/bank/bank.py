def Main():
    answear = input("Greeting: ")
    answear = answear.lower().strip()
    if answear[0] == 'h':
        if answear[0:5] == 'hello':
            print("$0")
        else:
            print("$20")
    else:
        print("$100")
Main()
