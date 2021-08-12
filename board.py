class Board:

    def __init__(self, size: int):
        row = 0
        this_board = []
        while row < size:
            new_row = []
            column = 0
            while column<size:
                new_row.append(f"[{column},{size-row-1}]")
                column += 1
            this_board.append(new_row)
            row += 1
        self.board = this_board

    def render(self):
        for row in self.board:
            for square in row:
                print(square,end="")
            print("")



