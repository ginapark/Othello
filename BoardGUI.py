import turtle, math, time
SQUARE = 50
CENTER_Y = 5
CENTER_X = 25
TILE_SIZE = 20
color = "white"

class BoardGUI:
    def __init__(self, n):
        self.rows = n
        self.window = turtle.Screen()
        self.draw_board_gui(self.window, n)
        self.turt = turtle.Turtle()

    ### Signature
    # draw_board_gui() :: (Object, Object, Integer) => Void
    ### Example/Test
    # self.draw_board_gui(turtle.Screen(), 4) => Void 
    # (draws othello board with grids)

    def draw_board_gui(self, window, n):
        ''' Function: draw_board
            Parameters: n, an int for # of squares
            Returns: nothing
            Does: Draws an nxn board with a green background
        '''
        window.setup(n * SQUARE + SQUARE, n * SQUARE + SQUARE)
        window.screensize(n * SQUARE, n * SQUARE)
        window.bgcolor('white')

        # Create the turtle to draw the board
        othello = turtle.Turtle()
        othello.penup()
        othello.speed(0)
        othello.hideturtle()

        # Line color is black, fill color is green
        othello.color("black", "forest green")
        
        # Move the turtle to the upper left corner
        corner = -n * SQUARE / 2
        othello.setposition(corner, corner)
    
        # Draw the green background
        othello.begin_fill()
        for i in range(4):
            othello.pendown()
            othello.forward(SQUARE * n)
            othello.left(90)
        othello.end_fill()

        # Draw the horizontal lines
        for i in range(n + 1):
            othello.setposition(corner, SQUARE * i + corner)
            self.draw_lines(othello, n)

        #Draw the vertical lines
        othello.left(90)
        for i in range(n + 1):
            othello.setposition(SQUARE * i + corner, corner)
            self.draw_lines(othello, n)
    
    ### Signature
    # draw_lines() :: (Object, Object, Integer) => Void
    ### Example/Test
    # self.draw_lines(turtle.Turtle(), 4) => Void 
    # (draws othello board lines n * Square length)
    def draw_lines(self, turt, n):
        """Draws the lines of the othello board."""
        turt.pendown()
        turt.forward(SQUARE * n)
        turt.penup()

    ### Signature
    # draw_circle() :: (Object, Float, Float) => Void
    ### Example/Test
    # self.draw_circle(-80.0, -71.0) => Void 
    # (draws tile pieces in indicated (x, y) coordinate)
    def draw_circle(self, x, y, color):
        """Draws tile pieces in indicated (x, y) coordinate after
        checking if the position is valid (if there is already)
        a tile in the space"""
        self.turt.hideturtle()
        self.turt.penup()
        self.turt.speed(0)
        self.turt.setposition(x, y)
        self.turt.pendown()
        self.turt.begin_fill()
        self.turt.fillcolor(color)
        self.turt.circle(TILE_SIZE)
        self.turt.end_fill()
        self.turt.penup()

    ### Signature
    # draw_initial_tiles() :: (Object) => Void
    ### Example/Test
    # self.draw_initial_tiles() => Void 
    # (draws initial black and white tiles to set up game)
    def draw_initial_tiles(self):    
        """Draws initial white and black tiles to set up the game"""
        x = CENTER_X
        y = CENTER_Y

        INITIAL_POSITIONS = [("black", -x, -SQUARE + y),
                             ("white", x, -SQUARE + y),
                             ("black", x, y),
                             ("white", -x, y)]

        for position in INITIAL_POSITIONS:
            self.draw_circle(position[1], position[2], position[0])