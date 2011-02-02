
#
# CONSTANTS
#
EMPTY = ' '

#
# CODE
#

class Board:
    """
    A general Board class to handle the game state.
    """

    def __init__(self, x, y):
        """
        A Board is a grid ( matrix for some folks ) with ranges : x, y
        """
        self.__x = x
        self.__y = y
        self.buildEmpty(x, y)
    #__init__

    def buildEmpty(self, x, y):
        """
        Let place empty matrix
        """
        self.__grade = []

        for i in range(x):
            self.__grade.append( [ EMPTY for j in range(y)] )
        #end for
    #buildEmpty

    def set(self, x, y, value):
        """
        Set the element at Board(x,y) a value
        TODO: exception for x,y out of range
        """
        self.__grade[x][y] = value
    def get(self, x, y):
        """
        Get the value in x, y
        TODO: exception for x, y out of range
        """
        return self.__grade[x][y]
    #get
#Board
