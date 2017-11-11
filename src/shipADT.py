## @file shipADT.py
#  @author Mingnan Su 400016478

from pointADT import *

class ShipT:

    ## @breif initilize a ship
    #  @param x the x-coor of initial point
    #  @param y the y-coor of initial point
    #  @param l the length of the ship
    #  @param turn the string direction of the turn
    def __init__(self,p,l,turn):
        # a shipT is a list of points
        self.pts = []
        if (turn == "left"):
            for i in range(0,l):
                temp = PointT(p.x, p.y - i)
                self.pts.append(temp)
        if (turn == "right"):
            for i in range(0,l):
                temp = PointT(p.x, p.y + i)
                self.pts.append(temp)
        if (turn == "up"):
            for i in range(0,l):
                temp = PointT(p.x - i, p.y)
                self.pts.append(temp)
        if (turn == "down"):
            for i in range(0,l):
                temp = PointT(p.x + i, p.y)
                self.pts.append(temp)
        # check for exceptions
        for pt in self.pts:
            if not 0 < pt.x <= 10:
                raise OutOfBond("Ship cannot be place out of bonds")
            elif not 0 < pt.y <= 10:
                raise OutOfBond("Ship cannot be place out of bonds")


    ## @breif string representation of a ship
    def __str__(self):
        pts = self.pts
        r = "["
        for pt in pts:
            r = r + str(pt)+", "
        return r[:-2]+"]"

## @brief An exception class for OutOfBond
class OutOfBond(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return str(self.value)

# ONLY for TESTING
start = PointT(3,1)
ship = ShipT(start,3,"down")
ship2 = ShipT(start,3,"up")
ship3 = ShipT(start,3,"right")
