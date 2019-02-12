from BoardArray import *
from BoardGUI import *
from GameLogic import *

def main():
    board = BoardArray(8)
    visual_board = BoardGUI(8)
    GameLogic(board, visual_board)

main()
