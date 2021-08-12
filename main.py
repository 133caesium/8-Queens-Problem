
from board import Board


board_row = []

empty_square = "[_]"
queen_square = "[Q]"

#row_initial


if __name__ == '__main__':
    test_board = Board(8)
    print(test_board)
    test_board.render()