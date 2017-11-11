## @file testGame.py
#  @author Mingnan Su 400016478

import unittest
from boardADT import *
from pointADT import *
from shipADT import *
from shipplaceADT import *
from playerADT import *
from Client import *

class BattleShipTests(unittest.TestCase):

    def setUp(self):
        #game board information:
        # 0 represents nothing here
        # 1 represents there is a hit, but miss
        # 2 represents there is a hits on the ship
        # 6 represents there is a ship, but no hits
        
        self.pt = PointT(1,5)
        self.ship = ShipT(pt,3,"down")
        self.s1 = ShipT(PointT(9,5),2,"up")
        self.s2 = ShipT(PointT(1,5),3,"down")
        self.s3 = ShipT(PointT(3,3),2,"left")
        self.s4 = ShipT(PointT(3,8),2,"down")
        self.s5 = ShipT(PointT(5,5),2,"right")
        self.ships = ShipPlaceT(s1,s2,s3,s4,s5)
        self.b = BoardT()
        self.p1 = PlayerT("mina",self.ships)
        

    def tearDown(self):
        self.pt = None
        self.ship = None
        self.s1 = None
        self.s2 = None
        self.s3 = None
        self.s4 = None
        self.s5 = None
        self.ships = None
        self.b = None
        self.p1 = None

    def test_point(self):
        #test for constructor
        self.assertTrue(self.pt.x == 1 and self.pt.y == 5)
        
        #test for exception
        with self.assertRaises(Exception):
            temp = PointT(-1,5)

    def test_ship(self):
        #test for constructor
        self.assertTrue(self.ship.pts[1].x == 2)
        self.assertTrue(self.ship.pts[2].y == 5)
        
        #test for exception
        with self.assertRaises(Exception):
            temp = ShipT(self.pt,3,"up")

    def test_shipplace(self):
        #test for constructor
        self.assertTrue(self.ships.ships[2].pts[1].y == 2)
        
        #test for exception
        with self.assertRaises(Exception):
            temp = ShipPlaceT(self.ship,self.s2,self.s3,self.s4,self.s5)
            
        #test for valid(point)
        #  test for true
        self.assertTrue(self.ships.valid(PointT(3,2)))
        #  test for false
        self.assertTrue(self.ships.valid(PointT(1,1)) == False)

    def test_board(self):
        #test for constructor
        self.assertTrue(self.b.board[2][3] == 0)
        
        #test for occupied(ship)
        self.b.occupied(self.ship)
        self.assertTrue(self.b.board[2][4] == 6)
        
        #test for state
        self.assertTrue(self.b.state(PointT(3,5)) == 6)
        
        #test for conflict
        #  test for false
        self.assertTrue(self.b.conflict() == False)
        #  test for true
        self.b.occupied(self.s2)
        self.assertTrue(self.b.conflict())
        
        #test for sunk(ship)
        #  test for false
        self.assertTrue(self.b.sunk(self.ship) == False)
        #  test for true
        self.b.board[0][4] = 2
        self.b.board[1][4] = 2
        self.b.board[2][4] = 2
        self.assertTrue(self.b.sunk(self.ship))

    def test_player(self):
        #test for contructor
        self.assertTrue(self.p1.name == "mina")
        self.assertTrue(self.p1.board.board[2][1] == 6)
        
        #test for gotshot(point)
        # shot hits
        self.p1.gotshot(PointT(3,3))
        self.assertTrue(self.p1.board.state(PointT(3,3)) == 2)
        # shot miss
        self.p1.gotshot(PointT(3,1))
        self.assertTrue(self.p1.board.state(PointT(3,1)) == 1)
        
        #test for isover()
        # test for false
        self.assertTrue(self.p1.isover() == False)
        # test for true
        self.p1.ship_sunk = 5
        self.assertTrue(self.p1.isover())
        self.p1.ship_sunk = 0
        
        #test for isSunk()
        # test for false
        self.assertTrue(self.p1.isSunk() == False)
        # test for true
        self.p1.board.board[2][1] = 2
        self.assertTrue(self.p1.isSunk())
        
        #test for a shot which sink a ship
        self.p1.gotshot(PointT(3,2))
        self.assertTrue(self.p1.ship_sunk == 1)

    def test_client(self):
        #define a new player
        self.ships2 = ShipPlaceT(s1,s2,s3,s4,s5)
        self.p2 = PlayerT("mina_clone",ships)
        
        Client.init(self.p1,self.p2)
        #test for init()
        self.assertTrue(Client.p1.board.state(PointT(10,10)) == 0)
        self.assertTrue(Client.p2.board.state(PointT(9,5)) == 6)
        self.assertTrue(Client.round == 0)

        #test for play(point)
        # Game Round one
        Client.play(PointT(3,3))
        print "Round one: p1 shot at (3,3), hits!"
        print Client.p1.board
        print " "
        print Client.p2.board
        self.assertTrue(Client.p2.board.state(PointT(3,3)) == 2)

        # Game Round two
        Client.play(PointT(2,2))
        print "Round two: p2 shot at (2,2), miss!"
        print Client.p1.board
        print " "
        print Client.p2.board
        self.assertTrue(Client.p1.board.state(PointT(2,2)) == 1)


if __name__ == '__main__':
    unittest.main()
