class Board:
    """
    Properties of the board and its display
    """
    def show(self, pos):
        if pos == "new":
            print("   |   |   ")
            print("------------")
            print("   |   |   ")
            print("------------")
            print("   |   |   ")
        else:
            print(" " + pos[7] + " | " + pos[8] + " | " + pos[9] + " ")
            print("------------")
            print(" " + pos[4] + " | " + pos[5] + " | " + pos[6] + " ")
            print("------------")
            print(" " + pos[1] + " | " + pos[2] + " | " + pos[3] + " ")
