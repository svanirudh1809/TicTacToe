# Imports
from board import Board
import random
import time

# Game against computer
class gameAgainstComputer:
    """
    Class with computer intelligence to play against human
    Basic intuition : Start with random spot and always go for the winning set (Greedy choice)
    """
    def __init__(self, player):
        # Create empty list that holds positions
        pos = [" "]*10

        # Show empty board
        Board().show("new")

        # Enter loop
        if player == 'x':
            self.startWithPlayer(pos)
        else:
            self.startWithComputer(pos)

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

    def simulateBoard(self, pos, val):
        board = [" "]*10
        for i in range(10):
            if i in pos:
                board[i] = val
        return board

    def computerPlay(self, self_pos, opponent_pos):
        """
        :param self_pos: is the computer position
        :param opponent_pos: is the player position
        :return:
        """
        # Sleep for 1 sec for naturality
        time.sleep(1)

        # Find available positions
        avail_pos = list( set(list(range(10))).difference(set( self_pos + opponent_pos )) )[1:]

        # Check win states for self and opponent
        for pos in avail_pos:
            # Check for self (computer)
            self_board = self.simulateBoard(self_pos, 1)
            self_board[pos] = 1
            if self.win(self_board):
                spot = pos
                print("Computer: Going for win")
                return spot

            # Check the opponent
            opponent_board = self.simulateBoard(opponent_pos, 2)
            opponent_board[pos] = 22
            if self.win(opponent_board):
                spot = pos
                print("Computer: Stopping you from win")
                return spot

        # Choose randomly if everything is normal
        spot = random.choice(avail_pos)
        print("Computer: Choosing randomly")
        return spot

    def startWithPlayer(self, pos):
        # Empty_positions
        x_pos, o_pos = [], []

        # Enter 9 step loop
        step = 1

        while step <= 9:
            if step % 2 != 0:
                spot = int(input("Player, choose the position to mark : "))
                if 1 <= spot <= 9:
                    if pos[spot] == " ":
                        pos[spot] = 'x'
                        Board().show(pos=pos)
                        step += 1
                        x_pos.append(spot)
                        if self.win(pos):
                            print("Congratulations player! You Won")
                            break
                    else:
                        print("Position not empty")
                else:
                    print("Invalid Choice")
            else:
                print("Thinking.....")
                spot = self.computerPlay(o_pos, x_pos)
                pos[spot] = 'o'
                o_pos.append(spot)
                Board().show(pos)
                if self.win(pos):
                    print("You lost the game! Well tried!")
                    break
                step += 1

        if step == 10:
            print("Game draw! choose 2 to play again")

    def startWithComputer(self, pos):
        # Empty_positions
        x_pos, o_pos = [], []

        # Enter 9 step loop
        step = 1

        while step <= 9:
            if step % 2 == 0:
                spot = int(input("Player, choose the position to mark : "))
                if 1 <= spot <= 9:
                    if pos[spot] == " ":
                        pos[spot] = 'o'
                        Board().show(pos=pos)
                        step += 1
                        o_pos.append(spot)
                        if self.win(pos):
                            print("Congratulations player! You Won")
                            break
                    else:
                        print("Position not empty")
                else:
                    print("Invalid Choice")
            else:
                print("Thinking.....")
                spot = self.computerPlay(x_pos, o_pos)
                pos[spot] = 'x'
                x_pos.append(spot)
                Board().show(pos)
                if self.win(pos):
                    print("You lost the game! Well tried!")
                    break
                step += 1

        if step == 10:
            print("Game draw! choose 2 to play again")