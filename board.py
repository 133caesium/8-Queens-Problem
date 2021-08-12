import random
class Board:

    def __init__(self, size: int, max_queens: int):
        self.solution = True
        row = 0
        this_board = []
        self.queens = 0
        self.queenCoordinates = []
        while row < size:
            new_row = []
            column = 0
            while column<size:
                #new_row.append(f"[{column},{row}]")
                if (random.randint(0,7)==0 and self.queens<max_queens):
                    new_row.append("[Q]")
                    self.queens += 1
                else:
                    new_row.append(f"[_]")
                column += 1
            this_board.append(new_row)
            row += 1
        self.board = this_board

    def render(self):
        for row in self.board:
            for square in row:
                print(square,end="")
            print("")
        print(f"This board has {self.queens} Queens.")

    def getQueenCoordinates(self):
        x = 0
        y = 0
        size = len(self.board)
        while y < size:
            x = 0
            while x < size:
                square = self.board[y][x]
                if self.board[y][x][1]=="Q":
                    self.queenCoordinates.append((x,y))
                x+=1
            y+=1
        print("Queens are located at: "+str(self.queenCoordinates))

    def checkQueenCaptures(self):
        for queen in self.queenCoordinates:
            this_x = queen[0]
            this_y = queen[1]
            for other_queen in self.queenCoordinates:
                if (this_x==other_queen[0] and this_y==other_queen[1]):
                    None
                    #this is the same queen so ignore
                elif (this_x==other_queen[0]):
                    print(f"The Queen at ({this_x},{this_y}) can capture the Queen at ({other_queen[0]},{other_queen[1]}) vertically")
                    self.solution = False
                elif (this_y == other_queen[1]):
                    print(f"The Queen at ({this_x},{this_y}) can capture the Queen at ({other_queen[0]},{other_queen[1]}) horizontally")
                    self.solution = False

    def isASolution(self):
        if self.solution:
            print(f"This board solves the {self.queens} Queens Problem")
        else:
            print(f"Queens can capture, this is not a solution.")
        return self.solution