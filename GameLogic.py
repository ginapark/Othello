import turtle, math, time
SQUARE = 50
CENTER_Y = 5
CENTER_X = 25
color = "white"
                        
class GameLogic:
    def __init__(self, board, visual_board, is_test=False):
        self.board = board
        self.rows = self.board.rows
        self.gui = visual_board
        self.start_game(is_test)

    ### Signature
    # start_game() :: (Object, Boolean) => Void
    ### Example/Test
    # self.start_game() => Void 
    # (Allows players to click/window remains open until
    # no legal moves left)
    def start_game(self, is_test=False):
        """Allows players to click and enables window to remain open
        until there are no legal moves left"""
        if not is_test:
            self.gui.draw_initial_tiles()

        self.board.insert_initial_positions()
        print("Player's turn")

        if not is_test:
            turtle.onscreenclick(self.click)
            turtle.done()

    ### Signature
    # click() :: (Object, Float, Float, Boolean) => Void
    ### Example/Test
    # self.click() => Void 
    # (Allows players to click/window remains open until
    # no legal moves left)    
    def click(self, x, y, is_test=False):
        """If the click results in a valid move, allows move to be made
        and passses turn over to computer player. If not, allows human 
        player to continue. If there are no valid moves by the human 
        player, passes turn to computer player."""
        row, column = self.get_list_index_positions(x, y)
        x, y = self.get_position_to_draw(x, y)
        color = "black"
        other_color = "white"

        if self.board.valid_move(row, column, color, other_color):
            self.board.make_move(row, column, color)

            if not is_test:
                self.gui.draw_circle(x, y, color)

            self.flip_tiles(row, column, color, other_color, is_test)
            self.computer_move(other_color, color, is_test)
        
        if self.board.best_move(color, other_color) == (None, None):
            if self.board.best_move(other_color, color) == (None, None):
                self.end = True
                self.end_game(is_test)
                return
            print("You have no valid moves. Computer plays again")
            self.computer_move(other_color, color, is_test)        
    
    ### Signature
    # computer_move() :: (Object, String, String, Boolean) => Void
    ### Example/Test
    # self.computer_move() => Void 
 
    def computer_move(self, color, other_color, is_test=False):
        """Computer makes a move based on the position that 
        will flip the most tiles on the current turn. If there
        are no valid moves, passes turn to human player."""
        print("Computer's turn")
        time.sleep(2)
        row, column = self.board.best_move(color, other_color)
        if row == None:
            print("Computer has no valid moves. Play again.")
            print("Player's turn")
            return
        x, y = self.get_draw_from_index(row, column)
        self.board.make_move(row, column, color)

        if not is_test:
            self.gui.draw_circle(x, y, color)

        self.flip_tiles(row, column, color, other_color, is_test)
        print("Player's turn")

    ### Signature
    # computer_move() :: (Object, Float, Float, String, String, Boolean) => Void
    ### Example/Test
    # self.computer_move() => Void 

    def flip_tiles(self, row, column, color, other_color, is_test=False):
        """After a move is made, flips all the tiles that should
        flip colors"""
        coordinates = self.board.get_tiles_to_flip(row, column, color, other_color)
        for position in coordinates:
            self.board.make_move(position[0], position[1], color)
            draw = self.get_draw_from_index(position[0], position[1])

            if not is_test:
                self.gui.draw_circle(draw[0], draw[1], color)

    ### Signature
    # get_position_to_draw() :: (Object, Float, Float) => (Integer, Integer)
    ### Example/Test
    # self.get_position_to_draw(-80.0, -71.0) => (-75, -95)
    # self.get_position_to_draw(0.0, 0.0) =>(25, 5)
    # (Provides a modified x, y position of inputs, adjusting the center
    # the coordinates)

    def get_position_to_draw(self, x, y):
        """Adjusts and centers given inputs and returns result to 
        draw the tile"""
        x = math.floor(x / SQUARE)
        y = math.floor(y / SQUARE)
        return (SQUARE * x) + CENTER_X, (SQUARE * y) + CENTER_Y

    ### Signature
    # get_list_index_positions() :: (Object, Float, Float) => (Integer, Integer)
    ### Example/Test
    # self.get_list_index_positions(-80.0, -71.0) == (0, 3)
    # self.get_list_index_positions(0.0, 0.0) == (2, 1)
    # (Takes x, y positions and returns the index positions to insert the tile in the 
    # board (list of lists data structure)

    def get_list_index_positions(self, x, y):
        """Adjusts the given inputs and returns the index positions to insert the tile
        in the board data structure"""
        row = math.floor(x / SQUARE)
        column = math.floor(y / SQUARE)
        n = self.rows // 2
        y = (1 + (column - n)) * -1
        x = row + n
        return x, y 

    ### Signature
    # get_draw_from_index() :: (Object, Float, Float) => (Integer, Integer)
    ### Example/Test
    # self.get_draw_from_index(0, 3) == (-75, -95)
    # self.get_draw_from_index(2, 1) == (25, 5)
    # Converts index tile positions from the board data structure 
    # to a modified x, y coordinate position for the board_gui to draw the tile  
    def get_draw_from_index(self, x, y):
        """Converts index tile positions from the board data structure 
        to a modified x, y coordinate position for the board_gui to 
        draw the tile  """
        n = self.rows // 2 
        y = ((-1 * y) - 1 + n) * SQUARE
        x = (x - n) * SQUARE
        return self.get_position_to_draw(x, y)
    
    ### Signature
    # end_game() :: (Object, Boolean) => (Integer, Integer)
    ### Example/Test
    # self.end_game() => (27, 37)

    def end_game(self, is_test=False):
        """Counts the number of black and white tiles and 
        prints the winner"""
        computer = 0
        human = 0
        turtle.onscreenclick(None)
        
        for row in self.board.board:
            for tile in row:
                if tile == "black":
                    human += 1
                elif tile == "white":
                    computer += 1

        if not is_test:
            if human > computer:
                player = input("Congratulations! You win with " + str(human) + 
                            " tiles. \n" + "What is your name? \n")
            else: 
                player = input("Sorry, you lose. Computer wins with " + 
                                str(computer) + " tiles. You had " + 
                                str(human) + " tiles.\n" + 
                                "What is your name? \n")
            self.add_to_file(player, str(human))
        print("Thanks for playing!")

        return (human, computer)
    
    ### Signature
    # add_to_file() :: (Object, String, String, String) => Void
    ### Example/Test
    # self.add_to_file() => ("Bob", 37) => Void
    # (Adds the name "Bob" and score 37 to the file)
    def add_to_file(self, name, score, file_path = "scores.txt"):
        """Adds the name and score of the player into the 
        scores file."""
        added = False
        score = int(score)
        file = open(file_path, 'r')
        line_list = file.readlines()
        file = open(file_path, 'w')

        if not line_list:
            file.write(name + " " + str(score) + "\n")

        else:
            for line in  line_list:
                line = line.strip("\n")
                curr = line.split(" ")
                curr_score = int(curr[1])
                if score > curr_score and not added:
                    file.write(name + " " + str(score)+ "\n")
                    file.write(line + "\n")
                    added = True
                else:
                    file.write(line + "\n")
            if not added:
                file.write(name + " " + str(score)+ "\n")
        file.close()       