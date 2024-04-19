# Imports
from board import Board

# Game against human
class gameAgainstHuman:
    """
    Class with algorithm to show and multiplayer mode
    """
    def __init__(self):
        # Create an empty list to store values
        pos = [" "]*10

        # Show empty board
        Board().show("new")

        # Loop until 9 steps
        step = 1

        while step <= 9:
            # player x starts always
            if step % 2 != 0:
                spot = int(input("Player x, choose the position to mark : "))
                if 1 <= spot <= 9:
                    if pos[spot] == " ":
                        pos[spot] = 'x'
                        Board().show(pos=pos)
                        step += 1
                        if self.win(pos):
                            print("Congratulations player x! You Won")
                            break
                    else:
                        print("Position not empty")
                else:
                    print("Invalid Choice")
            else:
                spot = int(input("Player o, choose the position to mark : "))
                if 1 <= spot <= 9:
                    if pos[spot] == " ":
                        pos[spot] = 'o'
                        Board().show(pos=pos)
                        step += 1
                        if self.win(pos):
                            print("Congratulations player o! You Won")
                            break
                    else:
                        print("Position not empty")
                else:
                    print("Invalid Choice")

        if step == 10:
            print("Game draw! Choose 1 to play again")

    def win(self, pos):
        if ((pos[7] == pos[8] == pos[9] != " ") or
            (pos[4] == pos[5] == pos[6] != " ") or
            (pos[1] == pos[2] == pos[3] != " ") or
            (pos[7] == pos[4] == pos[1] != " ") or
            (pos[8] == pos[5] == pos[2] != " ") or
            (pos[9] == pos[6] == pos[3] != " ") or
            (pos[7] == pos[5] == pos[3] != " ") or
            (pos[9] == pos[5] == pos[1] != " ")) :
            return True
        return False

