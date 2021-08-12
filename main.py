
from board import Board


boards_generated: int = 0


def generateABoard():
    global boards_generated
    queens = 5
    size = 8
    test_board = Board(size,queens)
    boards_generated += 1
    while test_board.queens!=queens:
        test_board = Board(size, queens)
        boards_generated += 1
    print(test_board)
    test_board.render()
    test_board.getQueenCoordinates()
    test_board.checkQueenCaptures()
    return test_board.isASolution()


def solve_randomly(num_tests: int):
    test_index = 0
    solution_count = 0
    while test_index < num_tests:
        if generateABoard():
            solution_count+=1
        test_index+=1
    print(f"The puzzle was randomly solved in {solution_count} of {num_tests} tests.")
    print(f"I needed to generate {boards_generated} boards to run {num_tests} tests")


if __name__ == '__main__':
    solve_randomly(1)
