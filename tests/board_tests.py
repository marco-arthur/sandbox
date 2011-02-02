
from board import Board
import unittest

class BoardTest(unittest.TestCase):
    dimValues = (
            (3,3),
            (5,1),
            (1,1))

    def testCreate(self):
        for i in self.dimValues:
            x, y = i
            b = Board(x, y)
            self.assertEqual(b.dimension(), i)
            #print (b.dimension(), i)
        #for
    #testCreate
    def testUse(self):
        val = 'x'
        b = Board(2,2)
        b.set(1,1, val)
        self.assertEqual(b.get(1,1), val)
    #testUse

#BoardTest

if __name__ == "__main__":
    unittest.main()   
