def Main():
    answear = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answear = answear.lower().strip()
    if answear == "42" or answear == "forty-two" or answear == "forty two":
        return print("Yes")
    else:
        return print("No")
Main()
