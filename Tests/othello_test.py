from othello import *

def test_create_board():
    board = Board(8)
    assert(board.board == [["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"]])

def test_insert_initial_positions():
    board = Board(8)
    board.insert_initial_positions()
    assert(board.board == [["E", "E", "E", "E", "E", "E", "E", "E"],
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", 'white', 'black', "E", "E", "E"], 
                           ["E", "E", "E", 'black', 'white', "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"]])

def test_valid_move():
    board = Board(8)
    board.insert_initial_positions()    
    assert(board.valid_move(3, 2, "black", "white") == True)
    assert(board.valid_move(3, 3, "black", "white") == False)

def test_make_move():
    board = Board(8)
    board.make_move(0, 0, "white")
    board.make_move(5, 3, "black")  
    assert(board.board[0][0] == "white")
    assert(board.board[3][5] == "black")
    assert(board.board[0][1] == "E")
    assert(board.board == [['white', "E", "E", "E", "E", "E", "E", "E"],
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", 'black', "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"]])    

def test_empty_space():
    board = Board(8)
    board.insert_initial_positions()
    assert(board.empty_space(3, 3) == False)
    assert(board.empty_space(3, 2) == True)

def test_get_tiles_to_flip():
    board = Board(8)
    board.insert_initial_positions()
    flip = board.get_tiles_to_flip(3, 2, "black", "white")
    assert(flip == [(3, 3)])
    board.make_move(3, 2, "black")
    board.make_move(3, 3, "black")
    board.make_move(3, 1, "white")
    flip = board.get_tiles_to_flip(3, 5, "white", "black")
    assert(flip == [(3, 4), (3, 3), (3, 2)])

def test_best_move():
    board = Board(8)
    board.insert_initial_positions()
    MOVES = [(3, 2, "black"), (3, 3, "black"), (3, 1, "white")]
    for turn in MOVES:
        board.make_move(turn[0], turn[1], turn[2])
    assert(board.best_move("white", "black") == (3, 5))

    for turn in board.get_tiles_to_flip(3, 5, "white", "black"):
        board.make_move(turn[0], turn[1], "white")
    board.make_move(3, 5, "black")
    board.make_move(2, 4, "black")
    assert(board.best_move("black", "white") == (3, 0))
    board.make_move(3, 0, "black")
    assert(board.best_move("black", "white") == (5, 4))

def test_start_game():
    board = Board(8)
    test = None
    game = Game(board, test, True)
    assert(game.board.board == [["E", "E", "E", "E", "E", "E", "E", "E"],
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", 'white', 'black', "E", "E", "E"], 
                           ["E", "E", "E", 'black', 'white', "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"], 
                           ["E", "E", "E", "E", "E", "E", "E", "E"]])

def test_click():
    board = Board(8)
    test = None
    game = Game(board, test, True)
    board = Board(4)
    test = None
    game = Game(board, test, True)
    for row in range(game.rows):
        for column in range(game.rows):
            game.board.make_move(row, column, "white")
    game.click(0, 0, True)
    assert(game.board.board == [['white', 'white', 'white', 'white'],
                                ['white', 'white', 'white', 'white'],
                                ['white', 'white', 'white', 'white'],
                                ['white', 'white', 'white', 'white']])

def test_computer_move():
    board = Board(4)
    test = None
    game = Game(board, test, True)

    #Making computer have no available move
    BLACK = [(3, 0), (3, 1), (2, 2), (3, 2), (0, 3), (1, 3), (2, 3)]
    for move in BLACK:
        game.board.make_move(move[0], move[1], "black")
    game.board.make_move(3, 3, "white")
    before_computer_move = []
    before_move = [[game.board.board[row][column] for column in range(game.rows)] \
                    for row in range(game.rows)]
    game.computer_move("white", "black", True)
    assert(game.board.board == before_move)
    
    #Making computer have an available move. Changing (3, 3) to empty.
    game.board.make_move(3, 3, "E")
    game.computer_move("white", "black", True)
    # assert(game.board.board != before_computer_move)
    assert(game.board.board == [['E', 'E', 'E', 'black'],
                                ['E', 'white', 'black', 'black'],
                                ['E', 'black', 'white', 'black'],
                                ['black', 'black', 'black', 'white']])

def test_get_position_to_draw():
    board = Board(4)
    test = None
    game = Game(board, test, True)
    assert(game.get_position_to_draw(-80.0, -71.0) == (-75, -95))
    assert(game.get_position_to_draw(0.0, 0.0) == (25, 5))
    assert(game.get_position_to_draw(-25.0, 25.0) == (-25, 5))

def test_get_list_index_positions():
    board = Board(4)
    test = None
    game = Game(board, test, True)
    assert(game.get_list_index_positions(-80.0, -71.0) == (0, 3))
    assert(game.get_list_index_positions(0.0, 0.0) == (2, 1))
    assert(game.get_list_index_positions(-25.0, 25.0) == (1, 1))

def test_get_draw_from_index():
    board = Board(4)
    test = None
    game = Game(board, test, True)
    assert(game.get_draw_from_index(0, 3) == (-75, -95))
    assert(game.get_draw_from_index(2, 1) == (25, 5))
    assert(game.get_draw_from_index(1, 1) == (-25, 5))

def test_end_game():
    board = Board(4)
    test = None
    game = Game(board, test, True)
    for row in range(game.rows):
        for column in range(game.rows):
            game.board.make_move(row, column, "black")
    assert(game.end_game(True) == (16, 0))
    game.board.make_move(3, 3, "white")
    assert(game.end_game(True) == (15, 1))
