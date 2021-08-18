import math
import statistics

from board import Board


boards_generated: int = 0
solution_boards = []

def generateABoard(reveal: bool):
    global boards_generated
    global solution_boards
    queens = 8
    size = 8
    test_board = Board(size,queens, reveal)
    boards_generated += 1
    while test_board.queens!=queens:
        test_board = Board(size, queens, reveal)
        boards_generated += 1
    if reveal: test_board.render()
    test_board.getQueenCoordinates()
    test_board.checkQueenCaptures()
    if test_board.isASolution():
        test_board.show_info = True
        solution_boards.append(test_board)
    return test_board.isASolution()


def solve_randomly(num_tests: int, show_results: bool):
    import time
    start_time = time.perf_counter()
    test_time_checks = []
    test_index = 0
    solution_count = 0
    while test_index < num_tests:
        if generateABoard(show_results):
            solution_count+=1
        test_index+=1
        if test_index%100000==0:
            print(str(test_index/1000000)+" million tests.")
        test_time_checks.append(time.perf_counter())
    for board in solution_boards:
        board.show_info = True
        board.render()
    print(f"The puzzle was randomly solved in {solution_count} of {num_tests} tests.")
    print(f"I needed to generate {boards_generated} boards to run {num_tests} tests")
    total_run_time = round(test_time_checks[-1]-start_time,5)
    individual_run_time = []
    previous_time = start_time
    for time in test_time_checks:
        individual_run_time.append(time-previous_time)
        previous_time=time
    avg_time = statistics.mean(individual_run_time)
    test_time_stdev = statistics.stdev(individual_run_time)
    print(f"Total run time is {total_run_time} seconds and SD {test_time_stdev/avg_time}")

def calculate_probability_of_solution():
    possible_squares = 64
    queens = 8
    placed_queens = 0
    possible_boards = 1
    while placed_queens<queens:
        possible_boards = possible_boards * possible_squares
        placed_queens += 1
        possible_squares -= 1
    print(str(possible_boards))


if __name__ == '__main__':
    #solve_randomly(1000000, False)
    solve_randomly(300000000, False)


