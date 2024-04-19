# Imports
from gameAgainstHuman import gameAgainstHuman
from gameAgainstComputer import gameAgainstComputer

# Main Class
class main:
    """
    The tic tac toe is a classic game which is implemented using python in this
    class. This provides user with two options to play - 1. Against human, 2. Against computer
    """
    def __init__(self):
        # Print main heading
        print("TIC TAC TOE")

        # Greet user
        print("\nWelcome!")

        # Ask the two options
        print("\nChoose opponent:")
        print("\t1. Against Human")
        print("\t2. Against Computer (Beta)")
        print("\t3. Quit")

        # Get input
        req = int(input("Choice: "))

        # Enter main event loop
        while req!=3:
            if req == 1:
                # Ask user to choose symbol
                player = input("Choose the symbol: x or o - ")
                # Code to play with human
                gameAgainstHuman()
            elif req == 2:
                player = input("Choose the symbol: x or o - ")
                # Code to play with computer
                gameAgainstComputer(player)
            elif req == 3:
                break
            else:
                print("\nInvalid choice")

            req = int(input("\nChoice: "))


if __name__ == "__main__":
    main()