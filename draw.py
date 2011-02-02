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

    def board(self, x, y):
        """
        Draw a board.
        @x : The x coordinate of the leftmost corner
        @y : The y coordinate of the leftmost corner
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
        cursor = self.screen.cursor()
        saved  = cursor.getPos()
        width, height     = board.dimension()
        c_width, c_height = CELL_DIMENSION
        cursor.go(x,y) # Star Point
        # Proceed as a line printer
        for lin in range(0, height*c_height - 1):
            for col in range(0, width*c_width - 1):
                # calculate in cell
                h_ = lin % (c_height+1)
                w_ = col % (c_width +1)
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
    #End of Board()

#End of Draw
