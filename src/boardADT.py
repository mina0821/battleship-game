## @brief boardADT.py
#  @author Mingnan Su 400016478

from pointADT import *
from shipADT import *

## @breif An ADT which represents game board
class BoardT:

    ## @brief constructor of BoardT
    def __init__(self):
        # create an empty board with all 0's
        self.board = [[0,0,0,0,0,0,0,0,0,0] for count in range(10)]

    ## @brief check the state of a point
    #  @param pt the point want to examine
    #  @return return the corresponding state value
    def state (self,pt):
        return self.board[pt.x-1][pt.y-1]
        
    ## @brief let a ship occupied the game board
    #  @param s the ship which is going to place on board
    def occupied(self,s):
        # iterate thorugh all points in ship
        for pt in s.pts:
            # since row 1 represents board[0]
            x = pt.x - 1
            y = pt.y - 1
            # set the corresponding point to 6
            self.board[x][y] = self.board[x][y] + 6

    ## @brief check if two ships in board overlapes
    def conflict(self):
        for row in self.board:
            for item in row:
                if item > 6:
                    return True
        return False
    
    ## @brief check if a ship is sunk in this board
    #  @param s the ship to be check
    #  @return true if the ship is sunk in this board
    def sunk (self,s):
        # all points lie on the ship
        pts = s.pts
        # check if all points equal to 2
        for pt in pts:
            if not self.state(pt) == 2:
                return False
        return True

    ## @brief string representation of the board
    def __str__(self):
        r = ""
        for item in self.board:
            r = r + str(item)+"\n"
        return r[:-1]


#ONLY for TESTING
temp = BoardT()
temp.occupied(ship)
temp.occupied(ship2)

b = BoardT()
