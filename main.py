
from board import Board


board_row = []

empty_square = "[_]"
queen_square = "[Q]"

#row_initial

def generateABoard():
    test_board = Board(8,8)
    print(test_board)
    test_board.render()
    test_board.getQueenCoordinates()
    test_board.checkQueenCaptures()
    return test_board.isASolution()

if __name__ == '__main__':
    num_tests = 1000
    test_index = 0
    solution_count = 0
    while test_index < num_tests:
        if generateABoard():
            solution_count+=1
        test_index+=1
    print(f"The puzzle was randomly solved in {solution_count} of {num_tests} tests.")