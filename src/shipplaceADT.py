## @file shipplace.py
#  @author Mingnan Su 400016478

from shipADT import *
from pointADT import *
from boardADT import *

## @brief an ADT represents all the ships in board
class ShipPlaceT:

    ## @breif contructor of 5 ships
    #  @param s1 the ship which is going to add
    #  @param s2 the ship which is going to add
    #  @param s3 the ship which is going to add
    #  @param s4 the ship which is going to add
    #  @param s5 the ship which is going to add
    def __init__(self,s1,s2,s3,s4,s5):
        self.ships = [s1,s2,s3,s4,s5]
        temp = BoardT()
        temp.occupied(s1)
        temp.occupied(s2)
        temp.occupied(s3)
        temp.occupied(s4)
        temp.occupied(s5)
        if temp.conflict():
            raise ShipConflict("Ship placement overlapes")

    ## @brief check if shot hits ships
    #  @param pt the shot position
    #  @return true if the shot hits
    def valid (self,p):
        # for every ship in 5 ships
        for ship in self.ships:
            # for every point in ship
            for pt in ship.pts:
                # if there is a match, shot hits
                if (p.x == pt.x) & (p.y == pt.y):
                    return True
        return False

    ## @brief string representation of ships
    def __str__(self):
        r = ""
        for ship in self.ships:
            r = r + str(ship) + "\n"
        return r[:-1]

## @brief An exception class for 
class ShipConflict(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return str(self.value)

# ONLY for TESTING
s1 = ShipT(PointT(9,5),2,"up")
s2 = ShipT(PointT(1,5),3,"down")
s3 = ShipT(PointT(3,3),2,"left")
s4 = ShipT(PointT(3,8),2,"down")
s5 = ShipT(PointT(5,5),2,"right")
ships = ShipPlaceT(s1,s2,s3,s4,s5)
