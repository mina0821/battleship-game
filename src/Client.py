## @file Client.py
#  @author Mingnan Su 400016478

from boardADT import *
from pointADT import *
from shipADT import *
from shipplaceADT import *
from playerADT import *

## @brief An abstracted object that run the game
class Client:

    ## @brief initilize a game
    @staticmethod
    def init(p1,p2):
        Client.p1 = p1
        Client.p2 = p2
        Client.round = 0

    ## @brief one round of the game
    ## @param shot PointT indicates a shot
    @staticmethod
    def play(shot):
        ro = Client.round
        if not Client.p1.isover() or Client.p2.isover():
            if ro % 2 == 0:
                Client.p2.gotshot(shot)
                Client.round = ro + 1
            else:
                Client.p1.gotshot(shot)
                Client.round = ro + 1
              
        
