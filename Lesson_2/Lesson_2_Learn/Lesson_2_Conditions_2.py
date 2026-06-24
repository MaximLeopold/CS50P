#Goal is to build a  game recommendation system

#We collect data from the user 
difficulty = input("Do you prefer difficult or casual games?")
players = input("Do you prefer single or multiplayer games?")


def main():
    if difficulty == "difficult":
        if players == "multiplayer":
            recommend("poker")
        elif players == "single":
            recommend("Klondike")
        else:
            recommend("solitaire")
    elif difficulty == "casual":
        if players == "multiplayer":
            recommend("hearts")
        else:
            recommend("clock")
    else:
        print("Enter a valid difficulty: choose difficult or casual")
       

#We define a recommendation function - we want it to use the data we collected 
def recommend(game):
    print(f"You would like {game}") 

#Call the function 
main() 