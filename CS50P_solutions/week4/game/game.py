import random
while True:
    try:
        limit = int(input("Level: "))
        if limit <= 0:
            raise Exception
        r = random.randrange(1, limit, 1)
    except:
        print("Error")
    else:
        while True:
            try:
                Guess = int(input("Guess: "))
                if Guess < r:
                    print("Too small!")
                elif Guess > r:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
            except:
                print("Error")
        break #to break second outer loop when user guess the
