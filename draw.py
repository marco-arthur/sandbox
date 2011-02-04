#
# IMPORTS
#

#
# CONSTANTS
#

CELL_DIMENSION = (3,1)
BLANK = ' '

#
# CODE
#

class Draw:
    """
    Draw the class to handle console drawing.
    """
    def __init__(self, board, screen):
        """
        We need a screen (where to print) and a board (what to print)
        """
        self.__board  = board
        self.__screen = screen
        self.__column = '|' # column char
        self.__line   = '_' # line char
    #__init__

    def board(self, pos):
        """
        Draw a board clean
        @pos : The (x,y) coordinates of the leftmost corner
        ----> x
        |
        |y
            (0,0)
            *---------------------------
            |                           |
            |  (x, y)                   |
            |   *--- ---                |
            |   |   |   |               |
            |    --- ---                |
            |   |   |   |               |
            |    --- ---                |
            *---------------------------
        """
        x,y = pos
        self.__boardpos = pos # save the board position in screen
        cursor = self.screen.cursor()
        saved  = cursor.getPos()
        width, height   = board.dimension()
        cwidth, cheight = CELL_DIMENSION
        cursor.go(x,y) # Star Point
        # Proceed as a line printer
        for lin in range(0, height*cheight - 1):
            for col in range(0, width*cwidth - 1):
                # calculate in cell
                h_ = lin % (cheight+1)
                w_ = col % (cwidth +1)
                if h_ == 0:
                    if w_ == 0:
                        char = BLANK
                    else:
                        char = self.__line
                else:
                    if w_ == 0:
                        char = self.__column
                    else:
                        char = BLANK
                # end calculation
            cursor.go(x+lin, y+col)
            cursor.put(char)
            #end inner loop
        #end outer loop
        cursor.go(saved.line, saved.column) # Restore cursor Pos
    #board

    def incell(self, val, pos):
        """
        Try to draw a value in a cell
        @val : the value
        @pos : position in board
        @return : nothing
        """
        if len(val) > 1:
            return "Error"
        cursor = self.__screen.cursor()
        cwidth, cheight = board.dimension()
        # Calculate the place
        x_ = (pos.x - 1)*(cwidth + 1) + self.__boardpos[0]
        y_ = (pos.y - 1)*(cheight + 1) + self.__boardpos[1]
        # try to center value
        x_ += cwidth/2
        y_ += cheight/2
        # End calculation
        cursor.go(x_, y_)
        cursor.put(val)
    #incell
#End of Draw
