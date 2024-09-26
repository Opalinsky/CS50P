# def Main():
#     players = input("Choose the multiplayer or single-player: ")
#     if not (players == "multiplayer" or players == "single-player"):
#         return print("Pass the valid player type!")
#     difficulty = input("Choose the difficulty level: difficult or casual: ")
#     if not (difficulty == "difficult" or difficulty == "casual"):
#         return print("Pass the valid level type!")
#     if difficulty == "difficult" and players == "multiplayer":
#         recommend("Poker")
#     elif difficulty == "difficult" and players == "single-player":
#         recommend("Klondike")
#     elif difficulty == "casual" and players == "single-player":
#         recommend("Clock")
#     else:
#         recommend("Hearts")
# def recommend(game):
#     print("I recommend you:", game)

# Main()

# def Main():
#     difficulty = input("Difficult or Casual? ")
#     players = input("Single-player or Multiplayer? ")
#     if difficulty == "Difficult":
#         if players == "Multiplayer":
#             Recommend("Poker")
#         else:
#             Recommend("Klondike")
#     else:
#         if players == "Multiplayer":
#             Recommend("Hearts")
#         else:
#             Recommend("Clock")

# def Recommend(game):
#     print("I recommend you", game )

# Main()

def Main():
    difficulty = input("Difficult or Casual? ")
    players = input("Single-player or Multiplayer? ")
    if difficulty == "Difficult":
        if players == "Multiplayer":
            Recommend("Poker")
        elif players == "Single-player":
            Recommend("Klondike")
        else:
            print("Enter valid players")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            Recommend("Hearts")
        elif players == "Single-player":
            Recommend("Clock")
        else:
            print("Enter valid players")
    else:
        print("Enter a valid difficulty")
def Recommend(game):
    print("I recommend you", game )

Main()
