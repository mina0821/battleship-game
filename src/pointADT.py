## @file pointADT.py
#  @author Mingnan Su 400016478

class PointT:

    ## @brief constructor of pointT
    #  @param x the x-coor of point
    #  @param y the y-coor of point
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
        if not 0 < x <= 10:
            raise PtOutBonds("Point is not on the board.")
        elif not 0 < y <= 10:
            raise PtOutBonds("Point is not on the board.")

    ## @breif string representation
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

        
## @brief An exception class for PtOutBonds
class PtOutBonds(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return str(self.value)

# ONLY for TESTING
pt = PointT(1,5)
