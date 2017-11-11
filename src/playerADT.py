## @file playerADT.py
#  @author Mingnan Su 400016478

from boardADT import *
from pointADT import *
from shipADT import *
from shipplaceADT import *

## @brief an ADT represents the state of a player
class PlayerT:

    ## @brief playerT constructor
    #  @param name the player name
    #  @param ships the placement of 5 ships
    def __init__(self,name,ships):
        self.name = name
        self.ships = ships
        #player unique game board
        self.board = BoardT()
        #player's ship existed
        self.ship_sunk = 0

        #game board information:
        # 0 represents nothing here
        # 1 represents there is a hit, but miss
        # 2 represents there is a hits on the ship
        # 6 represents there is a ship, but no hits
        for ship in ships.ships:
            self.board.occupied(ship)

    ## @brief when player got a shot from enemy
    #  @param shot the shot player receive
    def gotshot(self,shot):
        # actual index smaller than shot coordinates by 1
        x = shot.x - 1
        y = shot.y - 1
        if (self.ships.valid(shot)):
            self.board.board[x][y] = 2
            if self.isSunk():
                self.ship_sunk = self.ship_sunk + 1
        else:
            self.board.board[x][y] = 1

    ## @brief check if the game is over
    #  @return true if the game is over
    def isover(self):
        return self.ship_sunk == 5

    ## @brief check if a ship being sunk
    #  @return true if there is a new ship sunk
    def isSunk(self):
        n = 0
        for ship in self.ships.ships:
            if self.board.sunk(ship):
                n = n + 1
        return n > self.ship_sunk


#ONLY for TESTING
p1 = PlayerT("mina",ships)
p1.gotshot(PointT(3,3))
p1.gotshot(PointT(3,2))
