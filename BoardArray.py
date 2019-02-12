import math, time
color = "white"
CARDINAL_COORDINATES = [lambda x, y, i: (x, y - i),
                        lambda x, y, i: (x + i, y - i),
                        lambda x, y, i: (x + i, y),
                        lambda x, y, i: (x + i, y + i),
                        lambda x, y, i: (x, y + i),                            
                        lambda x, y, i: (x - i, y + i),
                        lambda x, y, i: (x - i, y),
                        lambda x, y, i: (x - i, y - i)]
class BoardArray:
    "Creates board data structure to store all moves/game state"
    def __init__(self, n):
        self.rows = n
        self.board = self.create_board(self.rows)
    
    def __str__(self):
        for row in self.board:
            print(row)
        return ""
    
    ### Signature
    # create_board() :: (Object, Integer) => List
    ### Example/Test
    # self.create_board(4) => [['E', 'E', 'E', 'E'], 
    #                        ['E', 'E', 'E', 'E'], 
    #                        ['E', 'E', 'E', 'E'], 
    #                        ['E', 'E', 'E', 'E']]) 

    def create_board(self, n):
        """Creates a List of Lists to represent the n x n game board.
        Each element in the board is intially "E" to represent 
        an empty space. """
        board = [["E" for j in range(n)] for i in range(n)]
        return board

    ### Signature
    # make_move() :: (Object, Integer, Integer, String) => Void
    ### Example/Test
    # self.make_move(0, 0, "white") => Void
    # (Inserts the specified color into the given x, y index position)
    def make_move(self, x, y, color):
        """Inserts the specified color into the given x, y 
        index position"""
        self.board[y][x] = color

    ### Signature
    # insert_initial_positions() :: (Object) => Void
    ### Example/Test
    # self.insert_initial_positions() => Void
    # (Inserts the specified color into the given x, y index position)
    def insert_initial_positions(self):
        """Inserts initial black and white tile positions into the board data
        structure"""
        n = self.rows // 2
        for position in [(n - 1, n, "black"), 
                         (n - 1, n - 1, "white"), 
                         (n, n - 1, "black"), 
                         (n, n, "white")]:
            self.make_move(position[0], position[1], position[2])
    
    ### Signature
    # empty_space() :: (Object, Integer, Integer) => Boolean
    ### Example/Test
    # self.empty_space(3, 3) => False
    # self.empty_space(3, 2) => True

    def empty_space(self, x, y):
        "Checks if the specified position in the board is empty or not"
        if self.board[y][x] == "E":
            return True
        return False
    ### Signature
    # valid_move() :: (Object, Integer, Integer, String, String) => Boolean
    ### Example/Test
    # board.valid_move(3, 2, "black", "white") => True
    # board.valid_move(3, 3, "black", "white") => False
    def valid_move(self, x, y, color, other_color):
        """Returns whether or not a given coordinate is a valid move by 
        checking if there is already a tile there or not and 
        then checking all cardinal directions"""
        if self.empty_space(x, y):
            i = 1
            for direction in CARDINAL_COORDINATES:
                found_other = False
                index_x, index_y = direction(x, y, i)
                while 0 <= index_x < self.rows and 0 <= index_y < self.rows and \
                    self.board[index_y][index_x] != "E":
                    if found_other and self.board[index_y][index_x] == color:
                        return True
                    elif not found_other and self.board[index_y][index_x] == color:
                        break
                    elif self.board[index_y][index_x] == other_color:
                        found_other = True
                    index_x, index_y = direction(index_x, index_y, i)
        return False  
    
    ### Signature
    # get_tiles_to_flip() :: (Object, Integer, Integer, String, String) => List
    ### Example/Test  
    # self.get_tiles_to_flip(3, 2, "black", "white") => [(3, 3)]
    # self.get_tiles_to_flip(3, 5, "white", "black") = >
    # [(3, 4), (3, 3), (3, 2)])
    def get_tiles_to_flip(self, x, y, color, other_color):
        """Returns a list of coordinates of all the tiles that should
        flip colors"""
        i = 1
        found_other = False
        coordinates = []
        for direction in CARDINAL_COORDINATES:
            temp = []
            index_x, index_y = direction(x, y, i)
            while 0 <= index_x < self.rows and 0 <= index_y < self.rows and \
                  self.board[index_y][index_x] != "E":
                if found_other and self.board[index_y][index_x] == color:
                    for item in temp:
                        coordinates.append(item)
                    break 
                elif self.board[index_y][index_x] == other_color:
                    found_other = True
                    temp.append((index_x, index_y))
                index_x, index_y = direction(index_x, index_y, i)   
        return coordinates

    ### Signature
    # best_move() :: (Object, Integer, Integer, String, String) => List
    ### Example/Test  
    # self.best_move("black", "white") => (3, 0)
    # self.best_move("black", "white") => (5, 4)
    def best_move(self, color, other_color):
        """Returns the coordinates of the best move for
        the current turn if they exist. If no moves are 
        possible, returns None"""
        first_found = True
        moves = 0
        coordinates = None, None
        for row in range(self.rows):
            for column in range(self.rows):
                if self.valid_move(column, row, color, other_color):
                    possible = self.get_tiles_to_flip(column, row, color, other_color)
                    if first_found:
                        first_found = False
                        moves = len(possible)
                        coordinates = column, row
                    elif len(possible) > moves:
                        moves = len(possible)
                        coordinates = column, row
        return coordinates
